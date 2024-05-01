from django.db import models


class SellerSummary(models.Model):
    """판매자 요약 정보를 나타내는 모델입니다.

    :param name: 판매자 이름
    :type name: str
    :param address: 판매자 주소
    :type address: str
    """

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
