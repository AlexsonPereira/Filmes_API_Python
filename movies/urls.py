from django.urls import path
from .views import MoviesView, MoviesDetailsView, MoviesOrderView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", MoviesDetailsView.as_view()),
    path("movies/<int:movie_id>/orders/", MoviesOrderView.as_view()),
]
