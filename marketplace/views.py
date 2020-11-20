from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return JsonResponse({"200":"Marketplace app works!"}, safe=True)