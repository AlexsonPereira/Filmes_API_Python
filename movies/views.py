from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Movie
from .serializer import MovieSerializer


# Create your views here.
class MoviesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, 200)

    def post(self, req):
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)
        return Response(serializer.data, 201)


class MoviesDetailsView(APIView):
    def get(self, req, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        Response(movie)

    def delete(self, req, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=204)
