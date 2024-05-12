from rest_framework import serializers

from project.payments.models.charge_line import ChargeLine


class ChargeLineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeLine
        fields = "__all__"


class ChargeLineReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeLine
        fields = "__all__"
