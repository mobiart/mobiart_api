from django.shortcuts import render
from django.http import JsonResponse
  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from profile_manager.models import Profile
from profile_manager.serializers import ProfileSerializer

@api_view(["POST",])
def index(request):
    if request.method == "POST":
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
