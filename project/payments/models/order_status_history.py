from django.db import models
from project.payments.models.order import Order


class OrderStatusHistory(models.Model):
    """주문 상태 기록 모델입니다.

    :param status: 상태
    :type status: str
    :param timestamp: 타임스탬프
    :type timestamp: datetime.datetime
    """

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="status_histories"
    )
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
