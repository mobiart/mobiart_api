from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('image/',views.image),
    path('thumbnail/',views.thumbnail),
    path('product/',views.product),
    path('products/',views.products),
    path('image/',views.image)
]
