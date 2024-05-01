from django.db import models

from project.payments.models.user import User

payment_methods = {
    "CARD": "카드결제",
    "CASH": "현금결제",
    "POINT": "포인트결제",
}


class OrderPayMethod(models.Model):
    """주문 결제 방법 모델입니다.

    :param user: 사용자
    :type user: User
    :param payment_method: 결제 방법
    :type payment_method: str
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=payment_methods.items())
