from django.db import models


class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.G,
    )
    synopsis = models.TextField(blank=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    order = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="order_movies",
    )


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movies_ordered",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_ordered_movies",
    )
