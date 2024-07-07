# api/models.py

from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True)

class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    movies = models.ManyToManyField(Movie)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# # api/models.py

# from django.contrib.auth.models import User
# from django.db import models

# class Collection(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()

# class Movie(models.Model):
#     collection = models.ForeignKey(Collection, related_name='movies', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     genres = models.CharField(max_length=255)
#     uuid = models.CharField(max_length=36)
