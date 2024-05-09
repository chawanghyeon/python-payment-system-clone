from django.db import models

from project.payments.models.seller_summary import SellerSummary
from project.payments.models.charge_line import ChargeLine
from project.payments.models.order_pay_method import OrderPayMethod
from project.payments.models.order_memo import OrderMemo
from project.payments.models.order_status_history import OrderStatusHistory
from project.payments.models.delivery import Delivery
from project.payments.models.line_item import LineItem


class Order(models.Model):
    """주문 모델입니다.

    :param user_id: 주문을 한 사용자
    :type user_id: int
    :param order_no: 주문 번호
    :type order_no: str
    :param order_datetime: 주문 일시
    :type order_datetime: datetime
    :param order_pay_method: 주문 결제 방식
    :type order_pay_method: OrderPayMethod
    :param order_memo: 주문 메모
    :type order_memo: OrderMemo
    :param delivery: 배달 정보
    :type delivery: Delivery
    :param seller_summary: 판매자 요약 정보
    :type seller_summary: SellerSummary
    """

    user_id = models.BigIntegerField()
    order_no = models.CharField(max_length=255)
    order_datetime = models.DateTimeField(auto_now_add=True)
    order_pay_method = models.OneToOneField(OrderPayMethod, on_delete=models.CASCADE)
    order_memo = models.OneToOneField(OrderMemo, on_delete=models.CASCADE)
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    seller_summary = models.OneToOneField(SellerSummary, on_delete=models.CASCADE)
