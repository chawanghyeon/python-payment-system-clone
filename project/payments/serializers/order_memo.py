from rest_framework import serializers
from project.payments.models.order_memo import OrderMemo


class OrderMemoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMemo
        fields = "__all__"


class OrderMemoReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMemo
        fields = "__all__"
