# Generated by Django 4.1.6 on 2023-02-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movie_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(null=True),
        ),
    ]
