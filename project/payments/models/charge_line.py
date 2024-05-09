from django.db import models

from project.payments.models.order import Order


class ChargeLine(models.Model):
    """주문에 대한 청구 항목을 나타냅니다.

    :param order: 청구 항목이 속한 주문입니다.
    :type order: Order
    :param description: 청구에 대한 간단한 설명입니다.
    :type description: str
    :param amount: 청구 금액입니다.
    :type amount: int
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
