from rest_framework import serializers
from .models import User, Profile
from movies.models import LocationComment
from movies.serializers import MovieSerializer, LocationSerializer, LocationCommentSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = ('id', 'username', 'password', 'email', )
        read_only = ('password', )
    

class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Profile
        fields = '__all__'
        read_only = ('image','like_genres', 'like_locations', 'comments')
