from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('genre/', views.GenreList.as_view(), name='genre'),
    path('<int:movie_pk>/locations/', views.LocationList().as_view(), name='locations'),
    path('<int:movie_pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('<int:loc_pk>/comments/', views.LocationCommentList.as_view(), name='locate_comment'),
    path('<int:loc_pk>/like/', views.location_like, name='location_like'),
    # path('<int:cmt_pk>/comment/', views.comment_like, name='comment_like'),
]
