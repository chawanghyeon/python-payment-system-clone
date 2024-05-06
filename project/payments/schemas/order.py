from rest_framework import serializers
from project.payments.models.order import Order


class OrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
