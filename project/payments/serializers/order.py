from typing_extensions import override
from rest_framework import serializers
from project.payments.models.charge_line import ChargeLine
from project.payments.models.delivery import Delivery
from project.payments.models.line_item import LineItem
from project.payments.models.order import Order
from project.payments.models.order_memo import OrderMemo
from project.payments.models.order_pay_method import OrderPayMethod
from project.payments.models.order_status_history import OrderStatusHistory
from project.payments.models.seller_summary import SellerSummary
from project.payments.serializers.charge_line import ChargeLineCreateSerializer
from project.payments.serializers.delivery import DeliveryCreateSerializer
from project.payments.serializers.line_item import LineItemCreateSerializer
from project.payments.serializers.order_memo import OrderMemoCreateSerializer
from project.payments.serializers.order_pay_method import OrderPayMethodCreateSerializer
from project.payments.serializers.seller_summary import SellerSummaryCreateSerializer
from django.db import transaction


class OrderCreateSerializer(serializers.ModelSerializer):
    order_pay_method = OrderPayMethodCreateSerializer()
    order_memo = OrderMemoCreateSerializer()
    delivery = DeliveryCreateSerializer()
    line_items = LineItemCreateSerializer(many=True)
    seller_summary = SellerSummaryCreateSerializer()
    charge_lines = ChargeLineCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
        exclude = ("order_status_history",)

    @transaction.atomic
    @override
    def save(self, **kwargs):
        order_pay_method = self.validated_data.pop("order_pay_method")
        order_memo = self.validated_data.pop("order_memo")
        delivery = self.validated_data.pop("delivery")
        line_items = self.validated_data.pop("line_items")
        seller_summary = self.validated_data.pop("seller_summary")
        charge_lines = self.validated_data.pop("charge_lines")

        order_pay_method = OrderPayMethod.objects.create(**order_pay_method)
        order_memo = OrderMemo.objects.create(**order_memo)
        delivery = Delivery.objects.create(**delivery)
        seller_summary = SellerSummary.objects.create(**seller_summary)

        order = Order.objects.create(
            order_pay_method=order_pay_method,
            order_memo=order_memo,
            delivery=delivery,
            seller_summary=seller_summary,
            **self.validated_data
        )

        LineItem.objects.bulk_create(
            [LineItem(order=order, **line_item) for line_item in line_items]
        )

        ChargeLine.objects.bulk_create(
            [ChargeLine(order=order, **charge_line) for charge_line in charge_lines]
        )

        OrderStatusHistory.objects.create(
            order=order, status=OrderStatusHistory.Status.ORDERED
        )

        return order


class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderUpdateSerializer(serializers.ModelSerializer):
    order_pay_method = OrderPayMethodCreateSerializer(required=False)
    order_memo = OrderMemoCreateSerializer(required=False)
    delivery = DeliveryCreateSerializer(required=False)
    line_items = LineItemCreateSerializer(many=True, required=False)
    seller_summary = SellerSummaryCreateSerializer(required=False)
    charge_lines = ChargeLineCreateSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = (
            "order_pay_method",
            "order_memo",
            "delivery",
            "line_items",
            "seller_summary",
            "charge_lines",
        )
