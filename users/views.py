from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from project.pagination import CustomPageNumberPagination

from .models import User
from .permissions import MyPermissions, IsOwner
from .serializer import UserSerializer


class UserViewRegister(APIView):
    def post(self, request: Request) -> Response:
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        return Response(user.data, status.HTTP_201_CREATED)


class UserViewGet(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyPermissions]

    def get(self, request: Request) -> Response:
        user_data = User.objects.all()
        result_page = self.paginate_queryset(user_data, request, view=self)
        user = UserSerializer(result_page, many=True)

        return self.get_paginated_response(user.data)


class UserViewOwner(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request: Request, user_id: int) -> Response:
        user_data = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user_data)
        user = UserSerializer(user_data)

        return Response(user.data)