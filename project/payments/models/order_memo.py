from django.db import models

from project.payments.models.user import User


class OrderMemo(models.Model):
    """주문 메모 모델입니다.

    :param user: 주문 메모를 작성한 사용자
    :type user: User
    :param memo: 주문 메모 내용
    :type memo: str
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memo = models.TextField()
