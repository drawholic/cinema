from django.contrib.auth.models import User
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_fullname()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    cast = models.ManyToManyField(Actor)
    description = models.TextField()
    stream_start = models.DateField()
    stream_end = models.DateField()
    tickets = models.IntegerField(default=60)
    price = models.FloatField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return  self.movie.title
