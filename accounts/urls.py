from django.urls import path, include
from . import views
# JWT 인증을 위한 import 
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<str:username>/profile/', views.ProfileList.as_view(), name='profile'),

    #JWT 인증관련 url
    path('api-token-auth/', obtain_jwt_token),

    # path('api-token-refresh/', refresh_jwt_token), # refresh
    # path('api-token-verify/', verify_jwt_token),   # verify another place
]
