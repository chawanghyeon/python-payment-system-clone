from rest_framework import serializers
from project.payments.models.order_pay_method import OrderPayMethod


class OrderPayMethodCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayMethod
        fields = "__all__"


class OrderPayMethodReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayMethod
        fields = "__all__"
