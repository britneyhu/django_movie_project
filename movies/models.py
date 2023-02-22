from django.db import models
import uuid

# Create your models here.



class Movie(models.Model):
    title = models.CharField(default='no title', max_length = 500, blank=True)
    director = models.CharField(default='no director', max_length = 500, blank=True)
    genre = models.CharField(default='', max_length = 500, blank=True)
    year = models.PositiveSmallIntegerField(default=0000, blank=True, null=True)
    star1 = models.CharField(default='no star', max_length = 500, blank=True)
    star2 = models.CharField(default='no star', max_length = 500, blank=True)
    rating = models.PositiveSmallIntegerField(default=00, blank=True, null=True)
    timeswatched = models.PositiveSmallIntegerField(default=00, blank=True, null=True)
    movieimage = models.ImageField(default='images/default/default_movie.jpg', upload_to='images/titles/', blank=True)
    directorimage = models.ImageField(default='images/default/default_director.jpg', upload_to='images/directors', blank=True)


    def __str__(self):
        return self.title