from project.payments.models.order import Order
from project.payments.utils.mongodb_manager import MongoDbManager
from project.payments.utils.sharding_target_decorator import sharding_target
from project.payments.schemas.order import (
    OrderRequestSerializer,
    OrderResponseSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class OrderService:
    @staticmethod
    def read_order(order_id: int) -> Order:
        mongo_db_manager = MongoDbManager()
        order = mongo_db_manager.get_order_from_collection(order_id)

        if not order:
            return Response(
                {"error": f"Order with id {order_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = OrderResponseSerializer(order)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @sharding_target
    def create_order(user_id: int, data: dict) -> None:
        serializer = OrderRequestSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    @sharding_target
    def update_order(order_id: int, data: dict) -> None:
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with id {order_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = OrderRequestSerializer(order, data=data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @sharding_target
    def delete_order(order_id: int) -> None:
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with id {order_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
