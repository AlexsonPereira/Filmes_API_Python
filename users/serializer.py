from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField(required=True)
    birthdate = serializers.DateField(required=False)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField()
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)
