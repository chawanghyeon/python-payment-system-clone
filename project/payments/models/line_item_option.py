from django.db import models

from project.payments.models.line_item import LineItem


class LineItemOption(models.Model):
    """주문 항목 옵션 모델입니다.

    :param lineitem: 이 옵션에 연결된 주문 항목
    :type lineitem: LineItem
    :param option_name: 옵션의 이름
    :type option_name: str
    :param extra_cost: 추가 비용
    :type extra_cost: Decimal
    """

    lineitem = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=255)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)