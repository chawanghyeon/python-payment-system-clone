from rest_framework import routers

from project.payments.api.v1.endpoints.orders import OrderView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"orders/(?P<order_no>\w+)", OrderView, basename="orders")

urlpatterns = router.urls
