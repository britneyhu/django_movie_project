import django
django.setup()
import pandas as pd
from movies.models import *
import os
import shutil
from statistics import mode
from collections import Counter
#movieData.xlsx
#/Users/britn/movieproject/src/movie_images


def importtitles(excel_file, movie_image_folder, director_image_folder):
    df_movies = pd.read_excel(excel_file)
    movie_folder = movie_image_folder
    director_folder = director_image_folder
    folderlist = os.listdir(movie_folder)
    movies = []
    for index, row in df_movies[0:128].iterrows():
        movies.append(row['title'])
        movies.append(row['director'])
        movies.append(row['genre'])
        movies.append(row['year'])
        movies.append(row['star1'])
        movies.append(row['star2'])
        movies.append(row['rating'])
        movies.append(row['timeswatched'])
        movies.append("images/titles/"+ row['title']+'.jpg')
        shutil.copy(movie_folder+'/'+row['title']+'.jpg', '/Users/britn/movieproject/src/media/images/titles')
        movies.append("images/directors/"+ row['director']+'.jpg')
        shutil.copy(director_image_folder+'/'+row['director']+'.jpg', '/Users/britn/movieproject/src/media/images/directors')
    for i in range(0, len(movies), 10):
        m = Movie(title=movies[i], director=movies[i+1], genre =movies[i+2], year=movies[i+3], star1=movies[i+4], star2=movies[i+5], rating=movies[i+6], timeswatched=movies[i+7], movieimage=movies[i+8], directorimage=movies[i+9])
        m.save()

importtitles('Movie Data.xlsx', '/Users/britn/movieproject/src/movie_images', '/Users/britn/movieproject/src/director_images')

# def most_frequent(List):
#     occurence_count = Counter(List)
#     return occurence_count.most_common(1)[0][0]


# def importdirectors(excel_file, image_folder):
#     df_movies = pd.read_excel(excel_file)
#     folder = image_folder
#     directors = []
#     for index, row in df_movies[0:128].iterrows():
#         directors.append(row['director'])

#         titles = []
#         new_titles = []
#         titles.append(row['title'])
#         i = str(titles[0]).split(', ')
#         for x in i:
#             new_titles.append(x)
#         directors.append(len(new_titles))
#         directors.append(row['title'])

#         genres = []
#         new_genres = []
#         genres.append(row['genres'])
#         i = str(genres[0]).split(', ')
#         for x in i:
#             new_genres.append(x)
#         directors.append(most_frequent(new_genres))

#         stars = []
#         new_stars = []
#         stars.append(row['stars'])
#         i = str(stars[0]).split(', ')
#         for x in i:
#             new_stars.append(x)
#         directors.append(most_frequent(new_stars))

#         ratings = []
#         new_ratings = []
#         ratings.append(row['rating'])
#         i = str(ratings[0]).split(', ')
#         for x in i:
#             new_ratings.append(int(x))
#         avg = round((sum(new_ratings) / len(new_ratings)), 1)
#         directors.append(avg)

#         directors.append("images/directors/"+ row['director']+'.jpg')
#         shutil.copy(folder+'/'+row['director']+'.jpg', '/Users/britn/movieproject/src/media/images/directors')
    
#     for i in range(0, len(directors), 7):
#         m = Director(director=directors[i], num_movies=directors[i+1], titles =directors[i+2], most_genre=directors[i+3], most_actor=directors[i+4], avg_rating=directors[i+5], image=directors[i+6])
#         m.save()

# importdirectors('Director Data.xlsx','/Users/britn/movieproject/src/director_images')