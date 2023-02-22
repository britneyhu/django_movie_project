from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Count
from django.db import connection 
from django.urls import path
import random
from django.db.models import Q
from django.http import HttpResponse
from .forms import *
from collections import Counter
from django.views.generic.edit import UpdateView


# Create your views here.

    #most frequent function
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def display_home(request):
    return render(request, 'home.html')

def display_movies(request):
    movie_objects = Movie.objects.all().order_by('-rating')
    context = {
        'movie_objects': movie_objects
    }
    return render(request, "movies.html", context)

def display_directors(request):
    class Director_object:
        def __init__(self, director, num_movies, movies, most_genre, most_actor, avg_rating, image):
            self.director = director
            self.num_movies = num_movies
            self.movies = movies
            self.most_genre = most_genre
            self.most_actor = most_actor
            self.avg_rating = avg_rating
            self.image = image
        def __repr__(self):
            return self.director
    #director objects list
    director_objects = []
    #all director names
    directors = Movie.objects.distinct('director').values_list('director', flat=True)
    #most genre
    genre_list = []
    most_genre_list = []
    for i in directors:
        genre_list.append(list(Movie.objects.filter(director__exact=i).values_list('genre', flat=True)))
    for i in genre_list:
        most_genre_list.append(most_frequent(i))
    #most actor
    actor_list = []
    most_actor_list = []
    for i in directors:
        actor_list.append(list(Movie.objects.filter(director__exact=i).values_list('star1', 'star2')))
    for i in actor_list:
        most_actor_list.append(most_frequent(i))
    #all movies of each director
    movies_list = []
    for i in directors:
        movies_list.append(list((Movie.objects.filter(director__exact=i).values_list('title', flat=True))))
    #avg_rating
    rating_list = []
    avg_rating_list = []
    for i in directors:
        rating_list.append(list(Movie.objects.filter(director__exact=i).values_list('rating', flat=True)))
    for i in rating_list:
        avg_rating_list.append(round((sum(i) / len(i)), 1))
    #image
    image_list = []
    for i in directors:
        image_list.append(list(Movie.objects.distinct().filter(director__exact=i).values_list('directorimage', flat=True)))
    #making objects and appending to director_objects list
    for i in range(len(directors)):
        director = directors[i]
        num_movies = len(movies_list[i])
        movies = movies_list[i]
        most_genre = most_genre_list[i]
        most_actor = most_actor_list[i]
        avg_rating = avg_rating_list[i]
        image = image_list[i]
        director_objects.append(Director_object(director, num_movies, movies, most_genre, most_actor, avg_rating, image))
    director_objects.sort(key=lambda director: director.avg_rating, reverse=True)

    context = {
        'director_objects': director_objects,
        'all_objects': Movie.objects.all()
    }
    return render(request, "directors.html", context)

def display_genres(request):
    action_objectsall=Movie.objects.extra(where=["genre='Action'"])[:10]
    action_objects=random.sample(list(action_objectsall), 5)
    
    comedy_objectsall=Movie.objects.extra(where=["genre='Comedy'"])[:10]
    comedy_objects=random.sample(list(comedy_objectsall), 5)
    
    dramacomedy_objectsall=Movie.objects.extra(where=["genre='Drama Comedy'"])[:10]
    dramacomedy_objects=random.sample(list(dramacomedy_objectsall), 5)
    
    drama_objectsall=Movie.objects.extra(where=["genre='Drama'"])[:10]
    drama_objects=random.sample(list(drama_objectsall), 5)
    
    dramamystery_objectsall=Movie.objects.extra(where=["genre='Drama Mystery'"])[:10]
    dramamystery_objects=random.sample(list(dramamystery_objectsall), 5)
    
    dramaromance_objectsall=Movie.objects.extra(where=["genre='Drama Romance'"])[:10]
    dramaromance_objects=random.sample(list(dramaromance_objectsall), 5)
    
    feelgood_objectsall=Movie.objects.extra(where=["genre='Feel Good'"])[:10]
    feelgood_objects=random.sample(list(feelgood_objectsall), 5)
    
    horror_objectall=Movie.objects.extra(where=["genre='Horror'"])[:10]
    horror_objects=random.sample(list(horror_objectall), 5)
    
    scifidystopia_objectsall=Movie.objects.extra(where=["genre='Sci-Fi Dystopia'"])[:10]
    scifidystopia_objects=random.sample(list(scifidystopia_objectsall), 5)
    
    series_objectsall=Movie.objects.extra(where=["genre='Series'"])[:10]
    series_objects=random.sample(list(series_objectsall), 5)
    
    superhero_objectsall=Movie.objects.extra(where=["genre='Superhero'"])[:10]
    superhero_objects=random.sample(list(superhero_objectsall), 5)
    
    thriller_objectsall=Movie.objects.extra(where=["genre='Thriller'"])[:10]
    thriller_objects=random.sample(list(thriller_objectsall), 5)
    
    context = {'action_objects': action_objects,
    'comedy_objects': comedy_objects,
    'dramacomedy_objects': dramacomedy_objects,
    'drama_objects': drama_objects,
    'dramamystery_objects': dramamystery_objects,
    'dramaromance_objects': dramaromance_objects,
    'feelgood_objects': feelgood_objects,
    'horror_objects': horror_objects,
    'scifidystopia_objects': scifidystopia_objects,
    'series_objects': series_objects,
    'superhero_objects': superhero_objects,
    'thriller_objects': thriller_objects,
    }
    return render(request, "genres.html", context)

def display_stats(request):
    highestratedall=Movie.objects.all().order_by('-rating')[:10]
    highestrated=random.sample(list(highestratedall), 5)
    highestratedimage= random.choice(highestrated)

    mostrewatched=Movie.objects.all().order_by('-timeswatched')[:5]
    mostrewatchedimage= random.choice(mostrewatched)

    mostrecentall=Movie.objects.all().order_by('-year')[:10]
    mostrecent=random.sample(list(mostrecentall), 5)
    mostrecentimage= random.choice(mostrecentall)

    class Director_object:
        def __init__(self, director, avg_rating):
            self.director = director
            self.avg_rating = avg_rating
        def __repr__(self):
            return self.director
    director_objects = []
    directors = Movie.objects.distinct('director').values_list('director', flat=True)
    rating_list = []
    avg_rating_list = []
    for i in directors:
        rating_list.append(list(Movie.objects.filter(director__exact=i).values_list('rating', flat=True)))
    for i in rating_list:
        avg_rating_list.append(round((sum(i) / len(i)), 1))
    for i in range(len(directors)):
        director = directors[i]
        avg_rating = avg_rating_list[i]
        director_objects.append(Director_object(director, avg_rating))
    director_objects.sort(key=lambda director: director.avg_rating, reverse=True)
    highestrateddirector=random.sample(director_objects[:10], 5)
    highestrateddirectorimage= random.choice(highestrateddirector)
    

    context = {
        'highestrated': highestrated,
        'highestratedimage': highestratedimage,
        'mostrewatched': mostrewatched,
        'mostrewatchedimage': mostrewatchedimage,
        'mostrecent': mostrecent,
        'mostrecentimage': mostrecentimage,
        'highestrateddirector': highestrateddirector,
        'highestrateddirectorimage': highestrateddirectorimage,
    }
    return render(request, "stats.html", context)

def display_moviedetails(request, id=None):
    movie = get_object_or_404(Movie, id=id)
    context = {
        'movie':movie,
    }
    return render(request, "moviedetails.html", context)

def display_directordetails(request, director=None):
    director = director
    class Director_object:
        def __init__(self, director, num_movies, movies, most_genre, most_actor, avg_rating, image):
            self.director = director
            self.num_movies = num_movies
            self.movies = movies
            self.most_genre = most_genre
            self.most_actor = most_actor
            self.avg_rating = avg_rating
            self.image = image
        def __repr__(self):
            return self.director
    #all movies
    movies = list(Movie.objects.filter(director__exact=director).values_list('title', flat=True))
    #num movies
    num_movies = len(movies)
    #most genre
    most_genre=most_frequent(list(Movie.objects.filter(director__exact=director).values_list('genre', flat=True)))
    #most actor
    actor_list = []
    most_actor_list = []
    actor_list.append(list(Movie.objects.filter(director__exact=director).values_list('star1', 'star2')))
    for i in actor_list:
        most_actor_list.append(most_frequent(i))
    most_actor=most_actor_list
    #avg rating
    avg_rating = round((sum(list(Movie.objects.filter(director__exact=director).values_list('rating', flat=True))) / len(list(Movie.objects.filter(director__exact=director).values_list('rating', flat=True)))), 1)
    #image
    image = Movie.objects.distinct().filter(director__exact=director).values_list('directorimage', flat=True)
    image = image[0]
    #make object
    director_object = Director_object(director, num_movies, movies, most_genre, most_actor, avg_rating, image)

    context = {
        'director_object':director_object,
    }
    return render(request, "directordetails.html", context)

def search(request):
    results = []
    if request.method == 'GET':
        query = request.GET.get('search', None)
        if query:
            results = Movie.objects.filter(Q(title__icontains=query)| Q(director__icontains=query) | Q(genre__icontains=query) | Q(year__icontains=query) | Q(star1__icontains=query) | Q(star2__icontains=query) | Q(rating__icontains=query) | Q(timeswatched__icontains=query))
    return render(request, 'search.html', {'query': query, 'results': results})

def display_category_results(request):
    class Director_object:
        def __init__(self, director, num_movies, movies, most_genre, most_actor, avg_rating, image):
            self.director = director
            self.num_movies = num_movies
            self.movies = movies
            self.most_genre = most_genre
            self.most_actor = most_actor
            self.avg_rating = avg_rating
            self.image = image
        def __repr__(self):
            return self.director
    #director objects list
    director_objects = []
    #all director names
    directors = Movie.objects.distinct('director').values_list('director', flat=True)
    #most genre
    genre_list = []
    most_genre_list = []
    for i in directors:
        genre_list.append(list(Movie.objects.filter(director__exact=i).values_list('genre', flat=True)))
    for i in genre_list:
        most_genre_list.append(most_frequent(i))
    #most actor
    actor_list = []
    most_actor_list = []
    for i in directors:
        actor_list.append(list(Movie.objects.filter(director__exact=i).values_list('star1', 'star2')))
    for i in actor_list:
        most_actor_list.append(most_frequent(i))
    #all movies of each director
    movies_list = []
    for i in directors:
        movies_list.append(list((Movie.objects.filter(director__exact=i).values_list('title', flat=True))))
    #avg_rating
    rating_list = []
    avg_rating_list = []
    for i in directors:
        rating_list.append(list(Movie.objects.filter(director__exact=i).values_list('rating', flat=True)))
    for i in rating_list:
        avg_rating_list.append(round((sum(i) / len(i)), 1))
    #image
    image_list = []
    for i in directors:
        image_list.append(list(Movie.objects.distinct().filter(director__exact=i).values_list('directorimage', flat=True)))
    #making objects and appending to director_objects list
    for i in range(len(directors)):
        director = directors[i]
        num_movies = len(movies_list[i])
        movies = movies_list[i]
        most_genre = most_genre_list[i]
        most_actor = most_actor_list[i]
        avg_rating = avg_rating_list[i]
        image = image_list[i]
        director_objects.append(Director_object(director, num_movies, movies, most_genre, most_actor, avg_rating, image))
    director_objects.sort(key=lambda director: director.avg_rating, reverse=True)

    results = []
    highest_rated = []
    if request.method == 'GET':
        query = request.GET.get('search', None)
        if query:
            results = Movie.objects.filter(Q(title__icontains=query)| Q(director__icontains=query) | Q(genre__icontains=query) | Q(year__icontains=query) | Q(star1__icontains=query) | Q(star2__icontains=query) | Q(rating__icontains=query) | Q(timeswatched__icontains=query))
            highest_rated = Movie.objects.all().order_by('-rating')
            most_rewatched=Movie.objects.all().order_by('-timeswatched')
            most_recent=Movie.objects.all().order_by('-year')
            highest_rated_director=director_objects
    return render(request, 'categories.html', {'query': query, 'results': results, 'highest_rated': highest_rated, 'most_rewatched': most_rewatched, 'most_recent':most_recent, 'highest_rated_director': highest_rated_director,})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movie-detail', movie.id)
        else:
            print(form.errors)
    form = MovieForm()
    return render(request, "addmovie.html", {"form": form,})

def edit_movie(request, id):
    movie = Movie.objects.get(id=id)
    print(movie.title, movie.director, movie.genre, movie.star1, movie.star2, movie.year, movie.timeswatched, movie.rating, movie.movieimage, movie.directorimage)
    
    if request.method == "POST" and "delete" in request.POST:
        movie.delete()
        return redirect('movies')
    elif request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-detail', movie.id)
        else:
            print(form.errors)
    form = MovieForm(instance=movie)
    return render(request, "editmovie.html", {"form": form, "year": movie.year})
