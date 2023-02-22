# Generated by Django 4.1.5 on 2023-01-19 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_delete_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=500)),
                ('num_movies', models.CharField(max_length=500)),
                ('titles', models.CharField(max_length=500)),
                ('most_genre', models.CharField(max_length=500)),
                ('most_actor', models.CharField(max_length=500)),
                ('avg_rating', models.CharField(max_length=500)),
                ('image', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
