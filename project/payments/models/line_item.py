from django.db import models

from project.payments.models.order import Order


class LineItem(models.Model):
    """주문 항목 모델입니다.


    :param product_id: 상품 ID
    :type product_id: int
    :param item_name: 항목 이름
    :type item_name: str
    :param quantity: 수량
    :type quantity: int
    :param price: 가격
    :type price: int
    """

    product_id = models.BigIntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
