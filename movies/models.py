from django.db import models

from ..accounts.models import User

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=50)
    like_users = models.ManyToManyField("accounts.User", symmetrical=True, related_name='like_genres')


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    trailer_path = models.TextField()
    genres = models.ManyToManyField("movies.Genre", symmetrical=True, related_name='movies')


class Location(models.Model):
    like_users = models.ManyToManyField("accounts.User", symmetrical=True, related_name='like_locations')
    movie_title = models.ForeignKey("movies.movie", on_delete=models.CASCADE, related_name='locations')
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()


class LocationComment(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='comments')
    like_users = models.ManyToManyField("accounts.User", symmetrical=True, related_name='like_comments')
    location = models.ForeignKey("movies.Location", on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    # img = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
