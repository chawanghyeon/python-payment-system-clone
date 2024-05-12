from django.db.models import Model
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: APIView, obj: Model
    ) -> bool:
        # 읽기 권한 요청이 들어오면 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자(request.user)가 객체의 user와 동일한지 확인
        return obj.user_id == request.data.get("user_id")
