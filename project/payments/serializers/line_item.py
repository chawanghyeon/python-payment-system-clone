from rest_framework import serializers
from project.payments.models.line_item import LineItem
from project.payments.serializers.line_item_option import LineItemOptionCreateSerializer


class LineItemCreateSerializer(serializers.ModelSerializer):
    line_item_options = LineItemOptionCreateSerializer(many=True)

    class Meta:
        model = LineItem
        fields = "__all__"


class LineItemReadSerializer(serializers.ModelSerializer):
    line_item_options = LineItemOptionCreateSerializer(many=True)

    class Meta:
        model = LineItem
        fields = "__all__"
