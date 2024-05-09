from rest_framework import serializers
from project.payments.models.line_item_option import LineItemOption


class LineItemOptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItemOption
        fields = "__all__"


class LineItemOptionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItemOption
        fields = "__all__"
