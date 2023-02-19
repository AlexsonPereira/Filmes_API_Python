from django.urls import path
from .views import UsersView, UsersDetailsView
from rest_framework_simplejwt import views


urlpatterns = [
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("users/", UsersView.as_view()),
    path("users/<int:user_id>/", UsersDetailsView.as_view()),
]
