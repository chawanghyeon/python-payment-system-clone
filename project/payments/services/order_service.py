from project.payments.models.order import Order
from project.payments.utils.sharding_target_decorator import sharding_target
from project.payments.schemas.order import (
    OrderRequestSerializer,
    OrderResponseSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class OrderService:
    @classmethod
    def read_order(cls, order_id: int) -> Order:
        sharding_key = cls.get_sharding_key(order_id)
        shard = cls.get_shard(sharding_key)
        return shard.read_order(order_id)

    @classmethod
    @sharding_target
    def create_order(cls, user_id, data) -> None:
        serializer = OrderRequestSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @classmethod
    @sharding_target
    def update_order(cls, order_id: int, amount: float) -> None:
        sharding_key = cls.get_sharding_key(order_id)
        shard = cls.get_shard(sharding_key)
        shard.update_order(order_id, amount)

    @classmethod
    @sharding_target
    def delete_order(cls, order_id: int) -> None:
        sharding_key = cls.get_sharding_key(order_id)
        shard = cls.get_shard(sharding_key)
        shard.delete_order(order_id)
