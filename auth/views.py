from django.shortcuts import render
from django.http import JsonResponse
  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import request


from profile_manager.models import Profile
from profile_manager.serializers import ProfileSerializer

@api_view(["GET",])
def index(request):
    if request.method == "GET":
        URL = "https://graph.facebook.com/v9.0/oauth/access_token?client_id=281582256624404&redirect_uri=https%3A%2F%2Fmilsugi.tech%2Fapi%2Fauth&oq=redirect_uri%3Dhttps%3A%2F%2Fmilsugi.tech%2Fapi%2Fauth&client_secret=6b0fce6ce450d741fcccbd2d8167b906&code="+request.GET["code"]
        r = requests.get(url=URL)
        token = r.json()["access_token"]

        r=requests.get(url="https://graph.facebook.com/me?access_token="+access_token)
        uid = r.json()["id"]

        try:
            profile = Profile.objects.filter(user_id=id).get()
            serializer = ProfileSerializer(profile)
            return Response({"jwt":jwt.encode(serializer.data, settings.SECRET_KEY, algorithm='HS256')})


        except Exception as e:
            if str(e) == "Profile matching query does not exist.":
                profile = Profile.objects.create(uid=request.POST["id_token"],access_token=name,email=user_data["email"],platform="apple")
                profile.save()

                serializer = ProfileSerializer(profile)
                return Response({"jwt":jwt.encode(serializer.data, settings.SECRET_KEY, algorithm='HS256')})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
