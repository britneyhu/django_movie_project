"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include

from movies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', display_movies, name="movies"),
    path('directors/', display_directors),
    path('genres/', display_genres),
    path('home/', display_home),
    path('', display_home),
    path('stats/', display_stats),
    path('movies/<int:id>', display_moviedetails, name='movie-detail'),
    path('directors/<str:director>', display_directordetails),
    path('search/', search, name='search'),
    path('categories/', display_category_results, name='display_category_results'),
    path('addmovie/', add_movie, name="add_movie"),
    path('movies/<int:id>/edit/', edit_movie, name='edit_movie')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
