from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Movie
from .serializer import MovieSerializer, MovieOrderSerializer
from rest_framework.pagination import PageNumberPagination
from users.permissions import IsAdminAccount
import ipdb


# Create your views here.
class MoviesView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminAccount]

    def get(self, req):
        movies = Movie.objects.all()
        pages = self.paginate_queryset(movies, req)
        serializer = MovieSerializer(pages, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, req):
        self.check_object_permissions(req, obj=None)
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)
        return Response(serializer.data, 201)


class MoviesDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminAccount]

    def get(self, req, movie_id):
        self.check_object_permissions(req, obj=None)
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, 200)

    def delete(self, req, movie_id):
        self.check_object_permissions(req, obj=None)
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=204)


class MoviesOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, req, movie_id):
        movie_find = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie_find, user=req.user)
        return Response(serializer.data, 201)
