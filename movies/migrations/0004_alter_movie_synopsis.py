# Generated by Django 4.1.6 on 2023-02-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_order_movieorder_movie_movieorder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(),
        ),
    ]
