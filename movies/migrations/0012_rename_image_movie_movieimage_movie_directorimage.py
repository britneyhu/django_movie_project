# Generated by Django 4.1.5 on 2023-01-24 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image',
            new_name='movieimage',
        ),
        migrations.AddField(
            model_name='movie',
            name='directorimage',
            field=models.ImageField(default='', upload_to='images/directors/'),
        ),
    ]
