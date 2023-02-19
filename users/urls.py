from django.urls import path
from .views import UsersView
from rest_framework_simplejwt import views

urlpatterns = [
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("users/", UsersView.as_view()),
]
