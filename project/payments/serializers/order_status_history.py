from rest_framework import serializers

from project.payments.models.order_status_history import OrderStatusHistory


class OrderStatusHistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusHistory
        fields = "__all__"


class OrderStatusHistoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusHistory
        fields = "__all__"
