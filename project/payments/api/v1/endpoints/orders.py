from rest_framework.views import APIView
from project.payments.services.order_service import OrderService


class OrderView(APIView):
    def get(self, request, order_no=None):
        return OrderService.read_order(request.data.get("user_id"), order_no)

    def post(self, request):
        return OrderService.create_order(request.data)

    def put(self, request, pk=None):
        return OrderService.update_order(
            pk, request.data, order_no=request.data.get("order_no", "")
        )

    def delete(self, request, pk=None):
        return OrderService.delete_order(
            pk, request.data.get("user_id"), order_no=request.data.get("order_no", "")
        )
