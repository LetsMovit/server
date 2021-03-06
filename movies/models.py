from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    vote_average = models.FloatField()
    movie_id = models.IntegerField()
    # trailer_path = models.TextField()
    genres = models.ManyToManyField("movies.Genre", related_name='movies')


class Location(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_locations')
    movie = models.ForeignKey("movies.movie", on_delete=models.PROTECT,db_constraint=False, related_name='locations')
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, default='media/defaultIMG.gif')
    img_url = models.URLField(max_length=1000)


class LocationComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=True, related_name='like_comments')
    location = models.ForeignKey("movies.Location", on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="comments")
    # created_at = models.DateTimeField(auto_now_add=True)

# class CommentImage(models.Model):
#     location = models.OneToOneField("movies.LocationComment", on_delete=models.CASCADE, related_name='comment_img')
#     image = models.ImageField(upload_to='uploads', blank=True)
