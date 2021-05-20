from rest_framework import serializers
from .models import User
from movies.models import LocationComment
from movies.serializers import GenreSerializer, MovieSerializer, LocationSerializer, LocationCommentSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=LocationComment.objects.all())

    # M:N ========================================================
    # User - Genre
    like_genres = GenreSerializer(read_only=True, many=True)
    # User - LikeLocation
    like_locations = LocationSerializer(read_only=True, many=True)
    # User - LikeComment
    like_comments = LocationCommentSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'like_genres', 'like_locations', 'like_comments' )