from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name= 'movies'
urlpatterns = [
    path('home', views.display_home),
    path('movies', views.display_movies, name="movies"),
    path('director', views.display_directors),
    path('genres', views.display_genres),
    path('', views.display_home),
    path('stats', views.display_stats),
    path('movies/<int:id>', views.display_moviedetails, name='movie-detail'),
    path('directors/<str:director>', views.display_directordetails),
    path('search/', views.search, name='search'),
    path('categories/', views.display_category_results, name='display_category_results'),
    path('addmovie/', views.add_movie, name="add_movie"),
    path('movies/<int:id>/edit/', views.edit_movie, name="edit_movie")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
