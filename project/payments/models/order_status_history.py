from django.db import models
from project.payments.models.order import Order


class OrderStatusHistory(models.Model):
    """주문 상태 기록 모델입니다.

    :param order: 상태가 변경된 주문
    :type order: Order
    :param status: 상태
    :type status: str
    :param timestamp: 타임스탬프
    :type timestamp: datetime.datetime
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
