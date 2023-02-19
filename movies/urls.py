from django.urls import path
from .views import MoviesView, MoviesDetailsView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", MoviesDetailsView.as_view()),
]
