from django.db import models


class ChargeLine(models.Model):
    """주문에 대한 청구 항목을 나타냅니다.

    :param description: 청구에 대한 간단한 설명입니다.
    :type description: str
    :param amount: 청구 금액입니다.
    :type amount: Decimal
    """

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description


class Test(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name
