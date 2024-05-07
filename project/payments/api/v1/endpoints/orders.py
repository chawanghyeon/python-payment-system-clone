from rest_framework.views import APIView
from project.payments.services.order_service import OrderService


class OrderView(APIView):
    def get(self, request, pk=None):
        return OrderService.read_order(pk, user_id=request.user.id)

    def post(self, request):
        return OrderService.create_order(request.data, user_id=request.user.id)

    def put(self, request, pk=None):
        return OrderService.update_order(pk, request.data, user_id=request.user.id)

    def delete(self, request, pk=None):
        return OrderService.delete_order(pk, user_id=request.user.id)
