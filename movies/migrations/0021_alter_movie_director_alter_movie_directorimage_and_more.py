# Generated by Django 4.1.5 on 2023-02-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_movie_directorimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directorimage',
            field=models.ImageField(blank=True, default='', upload_to='images/directors'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movieimage',
            field=models.ImageField(blank=True, default='', upload_to='images/titles/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='star1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='star2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='timeswatched',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
