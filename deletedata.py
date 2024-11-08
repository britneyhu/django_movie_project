import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie.settings")
django.setup()
from movies.models import *

def delete_all():
    Movie.objects.all().delete()

folder1 = '/Users/britneyhu/Movie Library/django_movie_project/media/images/titles'
folderlist1 = os.listdir(folder1)

folder2 = '/Users/britneyhu/Movie Library/django_movie_project/media/images/directors'
folderlist2 = os.listdir(folder2)

user = input('Delete all objects in Movies? (y/n)')
if user == 'y' or 'n' or 'Y' or 'N':
    delete_all()
    for i in folderlist1:
        item = folder1+'/'+i
        os.remove(item)
    for i in folderlist2:
        item = folder2+'/'+i
        os.remove(item)
    print('Objects deleted from database.')
else:
    print("Must enter 'y' or 'n'.")


