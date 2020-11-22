from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Product, Image

class ProductSerializer(serializers.ModelSerializer):

    pid = serializers.SerializerMethodField('get_pid')

    def get_pid(self, instance):
        pid = instance.pk
        return pid

    class Meta:
        model = Product
        fields = ["name","details","price","active"]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'