from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Movie, Location, LocationComment, Genre
from accounts.models import User
from .serializers import (
                MovieSerializer,
                LocationSerializer,
                LocationCommentSerializer,
                GenreSerializer,
            )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# from rest_framework.decorators import api_view


class GenreList(APIView):
    """
    List all Genre
    """
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)



class LocationList(APIView):
    """
    List all about particular Movie, or create Location about Movie
    """
    def get_object(self, movie_pk):
        try:
            return Location.objects.filter(movie_id=movie_pk)
        except Location.DoesNotExist:
            raise Http404
    
    def get(self, request, movie_pk):
        locations = self.get_object(movie_pk)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    def post(self, request, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)


class MovieList(APIView):
    """
    Get List
    """
    def get(self, request):
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class MovieDetail(APIView):
    """
    Get Particular Movie
    """
    def get(self, request, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LocationCommentList(APIView):
    """
    Get Comment with Location, Create Comment on Location
    """
    def get_object(self, loc_pk):
        try:
            return LocationComment.objects.filter(location_id=loc_pk)
        except LocationComment.DoesNotExist:
            raise Http404

    def get(self, request, loc_pk):
        loc_comments = self.get_object(loc_pk)
        serializer = LocationCommentSerializer(loc_comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, loc_pk):
        location = get_object_or_404(Location, pk=loc_pk)
        serializer = LocationCommentSerializer(data=request.data)

        # 임시 유저 발급
        temp_user = User()
        temp_user.username = 'han'
        temp_user.password = 'han'
        temp_user.save(self)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(location=location, user=temp_user)
            return Response(serializer.data)

        
