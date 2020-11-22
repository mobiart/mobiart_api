from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Product, Image

class ProductSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField('get_id')

    def get_id(self, instance):
        id = instance.pk
        return id

    class Meta:
        model = Product
        fields = ["name","details","price","active"]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'