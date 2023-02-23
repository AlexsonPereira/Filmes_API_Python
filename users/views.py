from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.permissions import IsOwnerOrAdminAccount
from users.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
import ipdb

# Create your views here.
class UsersView(APIView):
    def post(self, req):
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)

    def get(self, req):
        serializer = UserSerializer(req.user)
        return Response(serializer.data, 200)


class UsersDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdminAccount]

    def get(self, req, user_id):
        user_find = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, obj=user_find)
        serializer = UserSerializer(user_find)
        return Response(serializer.data, 200)

    def patch(self, req, user_id):
        user_find = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, obj=user_find)
        serializer = UserSerializer(user_find, req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200)
