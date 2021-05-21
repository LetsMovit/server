from rest_framework import serializers

from .models import Movie, Location, LocationComment, Genre
from accounts.models import User
# from accounts.serializers import UserSerializer

# try:
#     from accounts.serializers import UserSerializer
# except ImportError:
#     import sys
#     UserSerializer = sys.modules[__package__ + '.UserSerializer']

''' 1. accounts.serializers에 있는 Serializer 가져오기 '''
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, queryset=LocationComment.objects.all())

#     # M:N ========================================================
#     # User - Genre
#     like_genres = GenreSerializer(read_only=True, many=True)
#     # User - LikeLocation
#     like_locations = LocationSerializer(read_only=True, many=True)
#     # User - LikeComment
#     like_comments = LocationCommentSerializer(read_only=True, many=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'like_genres', 'like_locations', 'like_comments' )

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # Movie - Genre =  M:N
    genres = GenreSerializer(read_only=True, many=True)
    # locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())


    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('genres', 'locations', )



class LocationSerializer(serializers.ModelSerializer):
    # M:N  Location - LikeUsers
    # like_users = UserSerializer(read_only=True, many=True)
    # location_comments = serializers.PrimaryKeyRelatedField(many=True, queryset=LocationComment.objects.all())

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('movie', 'like_users', )


class LocationCommentSerializer(serializers.ModelSerializer):
    # M:N 
    # like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = LocationComment
        fields = '__all__'
        read_only_fields = ('location', 'like_users', 'user', )
