# Generated by Django 4.1.5 on 2023-02-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_delete_director_alter_movie_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama/Comedy', 'Drama/Comedy'), ('Drama', 'Drama'), ('Drama/Mystery', 'Drama/Mystery'), ('Drama/Romance', 'Drama/Romance'), ('Feel Good', 'Feel Good'), ('Horror', 'Horror'), ('Sci-Fi/Dystopia', 'Sci-Fi/Dystopia'), ('Series', 'Series'), ('Superhero', 'Superhero'), ('Thriller', 'Thriller')], default='', max_length=500),
        ),
    ]
