from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, BookmarkSerializer
from .models import Profile
from django.shortcuts import render, get_object_or_404
import jwt
from django.conf import settings
from marketplace.models import Bookmark, Product

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
def bookmark(request):
    if request.method == "POST":
        try:
            user_data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
            profile_obj = Profile.objects.filter(user_id=user_data["user_id"]).get()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            product_obj = Product.objects.filter(pk=request.data["product_id"])
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            bookmark = Bookmark.objects.filter(product=product_obj,user=user_obj).get()
            bookmark.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            if str(e) == "Profile matching query does not exist.":
                bookmark = Bookmark.objects.create(product=product_obj,user=user_obj)
                return Response(status=status.HTTP_202_ACCEPTED)

            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
    


@api_view(['POST',])
def bookmarks(request):
    try:
        user_data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
        profile_obj = Profile.objects.filter(user_id=user_data["user_id"]).get()
    except Exception as e:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    try:
        bookmarks = Bookmark.objects.filter(profile=profile_obj).get()
        serializer = BookmarkSerializer(data=bookmark,many=True)
        return Response(serializer.data)
    except Exception as e:
        
        return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['POST',])
def me(request):
    data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
    profile = Profile.objects.filter(pk=data["id"]).get()
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

