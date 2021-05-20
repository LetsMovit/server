from rest_framework import serializers
from .models import User, Profile
from movies.models import LocationComment
from movies.serializers import GenreSerializer, MovieSerializer, LocationSerializer, LocationCommentSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
<<<<<<< HEAD
<<<<<<< HEAD
        # fields = ('username', 'password', 'email')
        fields = ('username', 'password', 'email',)
        read_only = ('like_genres', 'like_locations', 'like_comments', 'comments',)
=======
        fields = ('username', 'password')
        # read_only = ('profile', )

=======
>>>>>>> 2c605ecb9fe7594a39ef6aecee46449ddddc8390

        # fields = ('username', 'password', 'email')
        fields = ('username', 'password', 'email',)
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only = ('like_genres', 'like_locations', 'comments')
<<<<<<< HEAD
>>>>>>> 8a298e5062449e3aaae14c47373ec2d2e0ac6826
=======
>>>>>>> 2c605ecb9fe7594a39ef6aecee46449ddddc8390
