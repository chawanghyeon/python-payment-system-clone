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

    class Status:
        ORDERED = "ORDERED"
        PAYMENT_COMPLETED = "PAYMENT_COMPLETED"
        PREPARING = "PREPARING"
        DELIVERING = "DELIVERING"
        DELIVERED = "DELIVERED"
        CANCELED = "CANCELED"

    status_choices = [
        (Status.ORDERED, "주문됨"),
        (Status.PAYMENT_COMPLETED, "결제 완료"),
        (Status.PREPARING, "준비 중"),
        (Status.DELIVERING, "배송 중"),
        (Status.DELIVERED, "배송 완료"),
        (Status.CANCELED, "취소됨"),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=status_choices)
    timestamp = models.DateTimeField(auto_now_add=True)
