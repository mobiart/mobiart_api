from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Profile
from marketplace.models import Bookmark 

class ProfileSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')
    phone = serializers.SerializerMethodField('get_phone')


    def get_username(self, instance):
        id = instance.user_id
        return "Dragos Criste"

    def get_email(self, instance):
        return "dragoscrite@gmail.com"

    def get_phone(self, instance):
        return "0722343889901"

    class Meta:
        model = Profile
        fields = '__all__'

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fileds = '__all__'