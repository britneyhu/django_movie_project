import django
django.setup()
from  movies.models import *
from django.db import connection
from django.urls import path
from django.db.models import Count
import random
from django.shortcuts import render, get_object_or_404
from collections import Counter


#director_objects = Movie.objects.distinct().values('director', 'directorimage')

#director_objects = Movie.objects.all()

# with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM movies_movie")
#         result_list = cursor.fetchall()
# queryset = Movie.objects.bulk_create([Movie(*row) for row in result_list])
# urls = []
# for i in queryset:
#     urls.append = path("media", i.directorimage.url)

# results = Movie.objects.annotate(total=Count('director')).distinct()
# for result in results:
#     print(result.director, result.total)

# unique_instances = Movie.objects.values('director').distinct()
# model_instances = [Movie(**item) for item in unique_instances]
# model_queryset = Movie.objects.bulk_create(model_instances)
# print(model_queryset)

# results = Movie.objects.order_by('director')
# for result in results:
#     print(result.genre)

# action_objects=Movie.objects.distinct('genreimage').get(genreimage='images/genres/Thriller.jpg')

# print(action_objects.genreimage)

#action_objects=Movie.objects.extra(where=["genre='Action'"])[:5]
# action_objects=Movie.objects.all().values()
# print(type(action_objects))

# query_genres=Movie.objects.distinct('genre').values_list('genre', flat=True)
# print(list(query_genres))

# for i in list(query_genres):
    


# action_objects=Movie.objects.extra(where=["genre='Action'"])[:5]
# action_image=Movie.objects.distinct('genreimage').extra(where=["genreimage='images/genres/Action.jpg'"])

# director_objects = Director.objects.values('avg_rating').order_by('-avg_rating')
# for i in director_objects:
#     print(i)

# highestratedall=Movie.objects.all().order_by('-rating')[:10]
# highestrated=random.choices(highestratedall, k=5)
# print(highestrated)

# movie = get_object_or_404(Movie, id=769)
# print(movie.director)

# all_directors = Movie.objects.distinct('director').values_list('director', flat=True)

# director_dictionary ={
#     "director":[], 
#     "num_movies":[],
#     "movies":[],
#     "most_genre":[],
#     "most_actor":[],
#     "avg_rating":[],
# }

# for i in all_directors:
#     director_dictionary["director"].append(i)

#     director_dictionary["movies"].append(Movie.objects.filter(director__exact=i).values_list('title'))

# for i in director_dictionary:
#     print(director_dictionary['director'], '\n')


# for i in Director.objects.all():
#     print(i.titles)


# #director class
# class Director_object:
#     def __init__(self, director, num_movies, movies, most_genre, most_actor, avg_rating, image, id):
#         self.director = director
#         self.num_movies = num_movies
#         self.movies = movies
#         self.most_genre = most_genre
#         self.most_actor = most_actor
#         self.avg_rating = avg_rating
#         self.image = image
#         self.id = id

#     def __repr__(self):
#         return self.director

# #most frequent function
# def most_frequent(List):
#     occurence_count = Counter(List)
#     return occurence_count.most_common(1)[0][0]


# #director objects list
# director_objects = []


# #all director names
# directors = Movie.objects.distinct('director').values_list('director', flat=True)


# #most genre
# genre_list = []
# most_genre_list = []

# for i in directors:
#     genre_list.append(list(Movie.objects.filter(director__exact=i).values_list('genre', flat=True)))
# for i in genre_list:
#     most_genre_list.append(most_frequent(i))



# #most actor
# #all number of movies
# actor_list = []
# most_actor_list = []

# for i in directors:
#     actor_list.append(list(Movie.objects.filter(director__exact=i).values_list('star1', 'star2')))
# for i in actor_list:
#     most_actor_list.append(most_frequent(i))


# #all movies of each director
# movies_list = []

# for i in directors:
#     movies_list.append(list((Movie.objects.filter(director__exact=i).values_list('title', flat=True))))


# #avg_rating
# rating_list = []
# avg_rating_list = []

# for i in directors:
#     rating_list.append(list(Movie.objects.filter(director__exact=i).values_list('rating', flat=True)))
# for i in rating_list:
#     avg_rating_list.append(round((sum(i) / len(i)), 1))


# #image
# image_list = []
# for i in directors:
#     image_list.append(list(Movie.objects.distinct().filter(director__exact=i).values_list('directorimage', flat=True)))


# #id
# id_list = []
# for i in directors:
#     id_list.append(list(Movie.objects.distinct().filter(director__exact=i).values_list('id', flat=True)))



# #making objects and appending to director_objects list
# for i in range(len(directors)):
#     director = directors[i]
#     num_movies = len(movies_list[i])
#     movies = movies_list[i]
#     most_genre = most_genre_list[i]
#     most_actor = most_actor_list[i]
#     avg_rating = avg_rating_list[i]
#     image = image_list[i]
#     id = id_list[i]
#     director_objects.append(Director_object(director, num_movies, movies, most_genre, most_actor, avg_rating, image, id))

# director_objects.sort(key=lambda director: director.avg_rating, reverse=True)

# #printing director_objects list
# for i in director_objects:
#     print(i.id)

# # for i in Movie.objects.all():
# #     print(i.directorimage)


director = "David Lynch"
class Director_object:
    def __init__(self, director, num_movies, movies, most_genre, most_actor, avg_rating, image, id):
        self.director = director
        self.num_movies = num_movies
        self.movies = movies
        self.most_genre = most_genre
        self.most_actor = most_actor
        self.avg_rating = avg_rating
        self.image = image
        self.id = id

    def __repr__(self):
        return self.director

#most frequent function
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

movies = list(Movie.objects.filter(director__exact=director).values_list('title', flat=True))

num_movies = len(movies)

most_genre=most_frequent(list(Movie.objects.filter(director__exact=director).values_list('genre', flat=True)))

most_actor_list=[]
for i in list(Movie.objects.filter(director__exact=director).values_list('star1', 'star2')):
    for x in i:
        most_actor_list.append(x)
most_actor = most_frequent(most_actor_list)

avg_rating = round((sum(list(Movie.objects.filter(director__exact=director).values_list('rating', flat=True))) / len(list(Movie.objects.filter(director__exact=director).values_list('rating', flat=True)))), 1)

image = Movie.objects.distinct().filter(director__exact=director).values_list('directorimage', flat=True)
image = image[0]

id = Movie.objects.distinct().filter(director__exact=director).values_list('id', flat=True)
id = id[0]

director_object = Director_object(director, num_movies, movies, most_genre, most_actor, avg_rating, image, id)

print(director_object.director)
print(director_object.num_movies)
print(director_object.movies)
print(director_object.most_genre)
print(director_object.most_actor)
print(director_object.avg_rating)
print(director_object.image)
print(director_object.id)