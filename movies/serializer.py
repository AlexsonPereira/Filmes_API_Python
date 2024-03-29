from rest_framework import serializers

from movies.models import Movie, MovieOrder, RatingChoices


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, default=None)
    rating = serializers.ChoiceField(choices=RatingChoices, default=RatingChoices.G)
    synopsis = serializers.CharField(required=False, allow_null=True)
    added_by = serializers.EmailField(read_only=True, source="user.email")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, read_only=True, source="movie.title")
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.EmailField(read_only=True, source="user.email")
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
