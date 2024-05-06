from rest_framework.views import APIView
from project.payments.services.order_service import OrderService


class OrderView(APIView):
    def get(self, request):
        return OrderService.read_order(request.query_params.get("order_id"))

    def post(self, request):
        return OrderService.create_order(request.user.id, request.data)

    def put(self, request, pk):
        return OrderService.update_order(pk, request.data)

    def delete(self, request, pk):
        return OrderService.delete_order(pk)
