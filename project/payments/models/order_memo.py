from django.db import models


class OrderMemo(models.Model):
    """주문 메모 모델입니다.

    :param user_id: 주문 메모를 작성한 사용자
    :type user_id: int
    :param memo: 주문 메모 내용
    :type memo: str
    """

    user_id = models.BigIntegerField()
    memo = models.TextField()
