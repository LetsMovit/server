from rest_framework import serializers
from .models import User, Profile
from movies.models import Genre, Movie, Location, LocationComment
from movies.serializers import LocationCommentSerializer, MovieSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('movie', 'like_users', )

class LocationCommentSerializer(serializers.ModelSerializer):
    # M:N 
    # like_users = UserSerializer(read_only=True, many=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = LocationComment
        fields = ('image', 'rank', 'content', 'title', )
        read_only_fields = ('location', 'like_users', 'user' )

class MovieSerializer(serializers.ModelSerializer):
    # Movie - Genre =  M:N
    genres = GenreSerializer(read_only=True, many=True)
    # locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())

    class Meta:
        model = Movie
        fields = ('id', 'genres', 'title', 'overview', 'poster_path', 'backdrop_path', 'vote_average', 'movie_id', )
        read_only_fields = ('locations', )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
     # M:N ========================================================
    # User - Genre
    like_genres = GenreSerializer(read_only=True, many=True)
    # User - LikeLocation
    like_locations = LocationSerializer(read_only=True, many=True)
    # User - LikeComment
    like_comments = LocationCommentSerializer(read_only=True, many=True)
    comments = LocationCommentSerializer(read_only=True, many=True)

    class Meta:
        model = User

        fields = ('id', 'username', 'password', 'email', 'comments','like_genres', 'like_locations', 'like_comments', )
        read_only = ('password', 'like_genres' )
    

class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('image', 'user', )
        read_only = ('image','like_genres', 'like_locations', 'comments')
