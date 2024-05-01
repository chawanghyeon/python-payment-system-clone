from django.db import models


class User(models.Model):
    """사용자 모델입니다.

    :param name: 사용자 이름
    :type name: str
    :param email: 사용자 이메일
    :type email: str
    :param password: 사용자 비밀번호
    :type password: str
    :param phone_number: 사용자 전화번호
    :type phone_number: str
    :param is_customer: 고객 여부 (기본값: True)
    :type is_customer: bool
    :param is_delivery_partner: 배송 파트너 여부 (기본값: False)
    :type is_delivery_partner: bool
    :param created_date: 생성일시 (자동 생성)
    :type created_date: datetime.datetime
    :param updated_date: 업데이트일시 (자동 업데이트)
    :type updated_date: datetime.datetime
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    is_customer = models.BooleanField(default=True)
    is_delivery_partner = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
