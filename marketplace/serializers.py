from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Product, Image

class ProductSerializer(serializers.ModelSerializer):

    thumbnail = serializers.SerializerMethodField('get_thumbnail')


    def get_thumbnail(self, instance):
        product_obj = Product.objects.filter(pk=instace.pk)
        thumbnail = Image.objects.filter(product=product_obj).get()[0]

        return thumbnail


    class Meta:
        model = Product
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'