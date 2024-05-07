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
    :param total_amount: 주문의 총 금액
    :type total_amount: DecimalField
    :param order_datetime: 주문이 생성된 일시
    :type order_datetime: datetime.datetime
    :param accept_datetime: 주문이 수락된 일시
    :type accept_datetime: datetime.datetime
    :param arrive_datetime: 주문이 도착한 일시
    :type arrive_datetime: datetime.datetime
    :param order_pay_method: 주문의 결제 방법
    :type order_pay_method: OrderPayMethod
    :param order_memo: 주문의 메모
    :type order_memo: OrderMemo
    :param order_status_history: 주문의 상태 변경 이력
    :type order_status_history: OrderStatusHistory
    :param delivery: 주문의 배송 정보
    :type delivery: Delivery
    :param line_items: 주문의 상품 목록
    :type line_items: ManyToManyField(LineItem)
    :param seller_summary: 주문의 판매자 요약 정보
    :type seller_summary: SellerSummary
    :param charge_lines: 주문의 청구 항목 목록
    :type charge_lines: ManyToManyField(ChargeLine)
    """

    user_id = models.BigIntegerField()
    total_amount = models.IntegerField()
    order_datetime = models.DateTimeField(auto_now_add=True)
    accept_datetime = models.DateTimeField()
    arrive_datetime = models.DateTimeField()
    order_pay_method = models.ForeignKey(OrderPayMethod, on_delete=models.SET_NULL)
    order_memo = models.ForeignKey(OrderMemo, on_delete=models.SET_NULL)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL)
    line_items = models.ManyToManyField(LineItem)
    seller_summary = models.ForeignKey(SellerSummary, on_delete=models.SET_NULL)
    charge_lines = models.ManyToManyField(ChargeLine)
