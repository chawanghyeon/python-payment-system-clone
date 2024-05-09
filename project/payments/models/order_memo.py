from django.db import models


class OrderMemo(models.Model):
    """주문 메모 모델입니다.

    :param memo: 주문 메모 내용
    :type memo: str
    """

    memo = models.TextField()
