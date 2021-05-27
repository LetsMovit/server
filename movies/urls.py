from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('genre/', views.GenreList.as_view(), name='genre'),
    path('locations/', views.LocationListAll.as_view(), name='location_all'),
    path('<int:movie_pk>/locations/', views.LocationList().as_view(), name='locations'),
    path('<int:movie_pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('<int:loc_pk>/comments/', views.LocationCommentList.as_view(), name='locate_comment'),
    path('<int:comment_pk>/comment_detail/', views.LocationCommentDetail.as_view(), name='locate_comment'),
    path('<int:loc_pk>/like/', views.LocationLikeList.as_view(), name='location_like'),
    # path('<int:comment_pk>/image', views.CommentImageList.as_view(), name='comment_image'),
]