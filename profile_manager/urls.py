from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('bookmark',views.bookmark),
    path('bookmarks,',views.bookmarks),
    path('@me/', views.me)

]
