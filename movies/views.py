from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Movie, Location, LocationComment
from accounts.models import User
from accounts.serializers import UserSerializer
from .serializers import (
                MovieSerializer,
                LocationSerializer,
                LocationCommentSerializer,
                # CommentImageSerializer,
                # GenreSerializer,
            )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.parsers import FileUploadParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class GenreList(APIView):
    """
    List all Genre
    """
    # def get(self, request):
    #     genres = Genre.objects.all()
    #     serializer = GenreSerializer(genres, many=True)
    #     return Response(serializer.data)


class LocationListAll(APIView):
    """
    Get all Locations
    """
    def get(self, *args):
        locations = get_list_or_404(Location)
        serializer = LocationSerializer(locations, many=True)
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
        print(locations)
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
        # print(request.data)
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
    authentication_classes = (JSONWebTokenAuthentication,)
    """
    Get Comment with Location, Create Comment on Location
    """
    def get(self, request, loc_pk):
        loc_comments = LocationComment.objects.filter(location_id=loc_pk).prefetch_related('user')
        # location_id=loc_pk
        # users = []
        # for comment in loc_comments:
        #     users.append(UserSerializer(data=User.objects.filter(username=comment.user)))
        serializer = LocationCommentSerializer(loc_comments, many=True)

        return Response(serializer.data)
    
    def post(self, request, loc_pk, format=None):
        print(request)
        print(request.data)
        print(request.FILES)
        location = get_object_or_404(Location, pk=loc_pk)
        serializer = LocationCommentSerializer(data=request.data)
        
        
        if serializer.is_valid():
            serializer.save(location=location, user=request.user)
            return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
class LocationLikeList(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    """
    Get Like Status, count, Post add or remove Like
    """
    def get(self, request, loc_pk):
        location = get_object_or_404(Location, pk=loc_pk)

        if request.user in location.like_users.all():
            isClicked = True
        else:
            isClicked = False
        
        context = {
            'isClicked': isClicked,
            'like_cnt': len(location.like_users.all())
        }
        return Response(context)

    def post(self, request, loc_pk):
        location = get_object_or_404(Location, pk=loc_pk)
        print(location)
        
        if request.user in location.like_users.all():
            print(1111111111111111111)
            location.like_users.remove(request.user)
            isClicked = False
        else:
            print(2222222222222222222)
            location.like_users.add(request.user)
            isClicked = True
        
        context = {
            'isClicked': isClicked,
            'like_cnt': len(location.like_users.all())
        }
        return Response(context)

    
# class CommentImageList(APIView):
#     parser_classes = [FileUploadParser]

#     def post(self, request, filename, format=None):
#         image = request.data['image']
        