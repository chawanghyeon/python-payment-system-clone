from django.urls import include, path

from project.payments.api.v1.router import urlpatterns as payments_v1_urls

urlpatterns = [
    path("v1/", include(payments_v1_urls)),
]
