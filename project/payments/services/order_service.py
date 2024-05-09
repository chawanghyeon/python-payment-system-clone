from project.payments.models.order import Order
from project.payments.utils.mongodb_manager import MongoDbManager
from project.payments.utils.sharding_target_decorator import sharding_target
from project.payments.serializers.order import (
    OrderCreateSerializer,
    OrderReadSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class OrderService:
    @staticmethod
    def read_order(user_id: int, order_id: int) -> Order:
        mongo_db_manager = MongoDbManager()
        try:
            order = mongo_db_manager.get_order(user_id, order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with id {order_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = OrderReadSerializer(order)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @sharding_target
    def create_order(user_id: int, data: dict) -> None:
        serializer = OrderCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    @sharding_target
    def update_order(user_id: int, order_id: int, data: dict) -> None:
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with id {order_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = OrderCreateSerializer(order, data=data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @sharding_target
    def delete_order(user_id: int, order_id: int) -> None:
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with id {order_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
