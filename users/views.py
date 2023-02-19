from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

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
