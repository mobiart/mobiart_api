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
            product_obj = Product.objects.filter(pk=request.data["product_id"]).get()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            bookmark = Bookmark.objects.filter(product=product_obj).filter(user=profile_obj).get()
            bookmark.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            if str(e) == "Bookmark matching query does not exist.":
                bookmark = Bookmark.objects.create(product=product_obj,user=profile_obj)
                return Response(status=status.HTTP_202_ACCEPTED)

            return Response({"err":str(e)})        
    


@api_view(['GET',])
def bookmarks(request):
    try:
        
        profile_obj = Profile.objects.filter(pk=request.GET["user_id"]).get()
    except Exception as e:
        return Response({"error":str(e)})

    try:
        bookmarks = Bookmark.objects.filter(user=profile_obj).get()
        
        bookmarks_json =[{"id":1,"name":"1980s street-art","details":"I will perform 1980s-style street art for any home-owner that wants so spice-up their house with some beautiful art.","price_upon_request":False,"price":0.0,"thumbnail":"https://thumbs-prod.si-cdn.com/6E3HqsOY5S_e05bqDnZ-HKdd8Ek=/fit-in/1072x0/https://public-media.si-cdn.com/filer/9f/5d/9f5d258f-cd88-467a-83f6-f123b0bced6b/graffiti_artist_in_greece.jpg","active":True,"user":1}]

        return Response(bookmarks_json)

    except Exception as e:
        
        return Response({"error":str(e)})
        
@api_view(['POST',])
def me(request):
    data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
    profile = Profile.objects.filter(pk=data["id"]).get()
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

