from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password
import ipdb
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(User.objects.all(), "username already taken."),
        ],
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(User.objects.all(), "email already registered."),
        ],
    )
    birthdate = serializers.DateField(required=False)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                setattr(instance, key, make_password(value))
            else:
                setattr(instance, key, value)

        instance.save()
        return instance
