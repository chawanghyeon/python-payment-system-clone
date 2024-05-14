from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from project.payments.services.order_service import OrderService


class OrderView(APIView):
    def get(self, request: Request, order_no: str | None = None) -> Response:
        return OrderService.read_order(request.data.get("user_id"), order_no)

    def post(self, request: Request) -> Response:
        return OrderService.create_order(request.data)

    def put(self, request: Request, order_no: str | None = None) -> Response:
        return OrderService.update_order(order_no, request.data)

    def delete(self, request: Request, order_no: str | None = None) -> Response:
        return OrderService.delete_order(order_no)
