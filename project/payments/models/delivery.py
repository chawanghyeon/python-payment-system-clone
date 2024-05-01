from django.db import models

from project.payments.models.user import User


class Delivery(models.Model):
    """사용자에게 전달된 배송을 나타냅니다.

    :param user: 주문을 한 사용자
    :type user: User
    :param regional_code: 배송에 대한 지역 코드
    :type regional_code: Decimal
    :param delivery_address: 배송이 이루어지는 주소
    :type delivery_address: str
    :param delivery_status: 배송 상태입니다.
    :type delivery_status: str
    :param name: 배송 이름
    :type name: str
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regional_code = models.DecimalField(max_digits=10, decimal_places=0)
    delivery_address = models.CharField(max_length=255)
    delivery_status = models.CharField(max_length=50, default="Pending")
    name = models.CharField(max_length=255)
