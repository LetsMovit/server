from rest_framework import serializers
from .models import User, Profile
from movies.models import LocationComment
from movies.serializers import GenreSerializer, MovieSerializer, LocationSerializer, LocationCommentSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
<<<<<<< HEAD
        # fields = ('username', 'password', 'email')
        fields = ('username', 'password', 'email',)
        read_only = ('like_genres', 'like_locations', 'like_comments', 'comments',)
=======
        fields = ('username', 'password')
        # read_only = ('profile', )



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only = ('like_genres', 'like_locations', 'comments')
>>>>>>> 8a298e5062449e3aaae14c47373ec2d2e0ac6826
