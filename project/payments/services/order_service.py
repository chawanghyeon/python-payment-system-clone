from project.payments.models.order import Order
from project.payments.utils.mongodb_manager import MongoDbManager
from project.payments.utils.sharding_target_decorator import sharding_target
from project.payments.serializers.order import (
    OrderCreateSerializer,
    OrderReadSerializer,
    OrderUpdateSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from project.payments.utils.try_except_decorator import try_except


class OrderService:
    @staticmethod
    @try_except
    def read_order(user_id: int, order_id: int) -> Order:
        mongo_db_manager = MongoDbManager()
        order = mongo_db_manager.get_order(user_id, order_id)

        serializer = OrderReadSerializer(order)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @sharding_target
    @try_except
    def create_order(user_id: int, data: dict) -> None:
        serializer = OrderCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    @sharding_target
    @try_except
    def update_order(user_id: int, order_id: int, data: dict) -> None:
        order = Order.objects.get(id=order_id)
        serializer = OrderUpdateSerializer(order, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @sharding_target
    @try_except
    def delete_order(user_id: int, order_id: int) -> None:
        order = Order.objects.get(id=order_id)
        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
