from django.db import models


class LineItem(models.Model):
    """주문 항목 모델입니다.

    :param item_name: 항목 이름
    :type item_name: str
    :param quantity: 수량
    :type quantity: int
    :param price: 가격
    :type price: Decimal
    :param lineitem_options: 항목 옵션들
    :type lineitem_options: ManyToManyField("LineItemOption")
    """

    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
    lineitem_options = models.ManyToManyField("LineItemOption")
