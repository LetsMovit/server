from django.shortcuts import render

from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny



@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    user_serializer = UserSerializer(data=request.data)
    # profile_serializer = ProfileSerializer()
    profile_serilaizer = ProfileSerializer()
    # print(profile_serilaizer.user)
    profile = Profile()

	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if user_serializer.is_valid():
        user = user_serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        selectUser = User.objects.filter(username=user)
        profile = Profile.objects.create(user_id=selectUser[0].id)
        print(profile)
    
    # if profile_serilaizer.is_valid():
    #     profile_serilaizer.save(user_id=)

    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(user_serializer.data, status=status.HTTP_201_CREATED)