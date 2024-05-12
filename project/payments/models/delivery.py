from django.db import models

DELIVERY_STATUS = [
    ("Pending", "Pending"),
    ("Preparing", "Preparing"),
    ("Shipping", "Shipping"),
    ("Delivered", "Delivered"),
    ("Canceled", "Canceled"),
]


class Delivery(models.Model):
    """사용자에게 전달된 배송을 나타냅니다.

    :param regional_code: 배송에 대한 지역 코드
    :type regional_code: int
    :param delivery_address: 배송이 이루어지는 주소
    :type delivery_address: str
    :param delivery_status: 배송 상태입니다.
    :type delivery_status: str
    """

    regional_code = models.IntegerField()
    delivery_address = models.CharField(max_length=255)
    delivery_status = models.CharField(
        max_length=50, default="Pending", choices=DELIVERY_STATUS
    )
