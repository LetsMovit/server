from django.urls import path, include
from . import views
# JWT 인증을 위한 import 
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    #JWT 인증관련 url
    path('api-token-auth/', obtain_jwt_token),     # first
    path('api-token-refresh/', refresh_jwt_token), # refresh
    path('api-token-verify/', verify_jwt_token),   # verify another place
]
