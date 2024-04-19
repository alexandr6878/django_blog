from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Content(models.Model):
    nameofchanel = models.CharField(max_length=30)
    films = models.IntegerField()
    views = models.IntegerField()

class Auditory(models.Model):
    nameofchanel = models.CharField(max_length=30)
    subscribers = models.IntegerField()
    likes = models.IntegerField()

class Post(models.Model):
    tittle = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete = models.CASCADE,)
