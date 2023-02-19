# Generated by Django 4.1.6 on 2023-02-19 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movieorder_movie_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='order',
            field=models.ManyToManyField(related_name='order_movies', through='movies.MovieOrder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movieorder',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies_ordered', to='movies.movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieorder',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_ordered_movies', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]