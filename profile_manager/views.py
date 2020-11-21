from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile
import jwt
from django.conf import settings

@api_view(['GET', 'DELETE'])
def index(request):
    if request.method == 'GET':
        user_id=request.GET["user_id"]
        profiles = Profile.objects.filter(pk=user_id).get()
        serializer = ProfileSerializer(profiles, many=False)

        return Response(serializer.data)

    if request.method == 'DELETE':
        data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
        profile = Profile.objects.filter(pk=data["id"]).get()
        profile.delete()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['POST',])
def me(request):
    data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
    profile = Profile.objects.filter(pk=data["id"]).get()
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

