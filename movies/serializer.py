from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    rating = serializers.CharField(max_length=20)
    synopsis = serializers.CharField()
    added_by = serializers.EmailField(read_only=True, source="user.email")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrder(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.EmailField()
    buyed_at = serializers.DateTimeField(read_only=True)
