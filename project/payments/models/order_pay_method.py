from django.db import models

from project.payments.models.order import Order


class OrderPayMethod(models.Model):
    """주문 결제 방법 모델입니다.

    :param card: 카드 결제 여부
    :type card: bool
    :param card_receipt: 카드 영수증 발급 여부
    :type card_receipt: bool
    :param cash: 현금 결제 여부
    :type cash: bool
    :param amount_paid: 결제 금액
    :type amount_paid: int
    """

    card = models.BooleanField(default=False)
    card_receipt = models.BooleanField(default=False)
    cash = models.BooleanField(default=False)
    amount_paid = models.IntegerField()
