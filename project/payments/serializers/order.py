from rest_framework import serializers
from project.payments.models.order import Order
from project.payments.serializers.charge_line import ChargeLineCreateSerializer
from project.payments.serializers.delivery import DeliveryCreateSerializer
from project.payments.serializers.line_item import LineItemCreateSerializer
from project.payments.serializers.order_memo import OrderMemoCreateSerializer
from project.payments.serializers.order_pay_method import OrderPayMethodCreateSerializer
from project.payments.serializers.seller_summary import SellerSummaryCreateSerializer


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


class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
