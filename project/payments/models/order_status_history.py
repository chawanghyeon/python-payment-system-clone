from django.db import models


class OrderStatusHistory(models.Model):
    """주문 상태 기록 모델입니다.

    :param status: 상태
    :type status: str
    :param timestamp: 타임스탬프
    :type timestamp: datetime.datetime
    """

    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
