from django.db import models


payment_methods = {
    "CARD": "카드결제",
    "CASH": "현금결제",
    "POINT": "포인트결제",
}


class User(models.Model):
    # 사용자 정보를 저장하기 위한 모델
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    is_customer = models.BooleanField(default=True)
    is_delivery_partner = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Order(models.Model):
    # 주문 정보를 저장하기 위한 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_datetime = models.DateTimeField(auto_now_add=True)
    accept_datetime = models.DateTimeField()
    arrive_datetime = models.DateTimeField()
    order_pay_method = models.ForeignKey("OrderPayMethod", on_delete=models.SET_NULL)
    order_memo = models.ForeignKey("OrderMemo", on_delete=models.SET_NULL)
    order_status_history = models.ForeignKey(
        "OrderStatusHistory", on_delete=models.SET_NULL
    )
    delivery = models.ForeignKey("Delivery", on_delete=models.SET_NULL)
    line_items = models.ManyToManyField("LineItem")
    seller_summary = models.ForeignKey("SellerSummary", on_delete=models.SET_NULL)
    charge_lines = models.ManyToManyField("ChargeLine")


class OrderMemo(models.Model):
    # 주문에 대한 메모를 저장하기 위한 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memo = models.TextField()


class Delivery(models.Model):
    # 유저의 배송 정보를 저장하기 위한 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regional_code = models.DecimalField(max_digits=10, decimal_places=0)
    delivery_address = models.CharField(max_length=255)
    delivery_status = models.CharField(max_length=50, default="Pending")
    name = models.CharField(max_length=255)


class OrderPayMethod(models.Model):
    # 주문에 대한 결제 방법을 저장하기 위한 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=payment_methods.items())


class LineItem(models.Model):
    # 주문에 대한 각 품목명(메뉴)을 저장하기 위한 모델
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lineitem_options = models.ManyToManyField("LineItemOption")


class SellerSummary(models.Model):
    # 판매자의 주문 요약을 저장하기 위한 모델
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class ChargeLine(models.Model):
    # 결제내역을 저장하기 위한 모델
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class LineItemOption(models.Model):
    # 메뉴 옵션을 저장하기 위한 모델
    lineitem = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=255)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class OrderStatusHistory(models.Model):
    # 주문 상태 변경 이력을 저장하기 위한 모델
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
