# Generated by Django 4.1.5 on 2023-02-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_movie_genreimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='avg_rating',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='director',
            name='num_movies',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
