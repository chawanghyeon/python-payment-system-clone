from rest_framework import serializers
from project.payments.models.delivery import Delivery


class DeliveryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"


class DeliveryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"
