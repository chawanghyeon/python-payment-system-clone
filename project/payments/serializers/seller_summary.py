from rest_framework import serializers
from project.payments.models.seller_summary import SellerSummary


class SellerSummaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerSummary
        fields = "__all__"


class SellerSummaryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerSummary
        fields = "__all__"
