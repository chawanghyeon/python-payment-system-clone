from django.db import models


payment_methods = {
    "CARD": "카드결제",
    "CASH": "현금결제",
    "POINT": "포인트결제",
}


class OrderPayMethod(models.Model):
    """주문 결제 방법 모델입니다.

    :param user_id: 사용자
    :type user_id: int
    :param payment_method: 결제 방법
    :type payment_method: str
    """

    user_id = models.BigIntegerField()
    payment_method = models.CharField(max_length=50, choices=payment_methods.items())
