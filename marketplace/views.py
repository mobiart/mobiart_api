from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer,ImageSerializer
from .models import Product,Image
from profile_manager.models import Profile 

import jwt

@api_view(['GET',"POST","PUT","DELETE"])
def product(request):
    if request.method == "GET":
        product_id = request.GET["product_id"]
        try:
            product = Product.objects.filter(pk=product_id).get()
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "POST":
        product_data = request.data

        try:
            user_data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
            profile = Profile.objects.filter(user_id=user_data["user_id"]).get()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


        serializer = ProductSerializer(data=product_data,many=False)
        if serializer.is_valid():
            try:
                product = Product.objects.create(name=request.data["name"],details=request.data["details"],active=request.data["active"],user=profile.pk)
                product.save()
                return Response(status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors)

    elif request.method == "DELETE":
        try:
            user_data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
            profile = Profile.objects.filter(user_id=user_data["user_id"]).get()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            product_id = request.data["product_id"]
            product = Product.objects.filter(pk=product_id).filter(user=profile.pk).get()
            product.delete()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    elif request.method == "PUT":
        try:
            user_data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
            profile = Profile.objects.filter(user_id=user_data["user_id"]).get()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            product_id = request.data["product_id"]
            product = Product.objects.filter(pk=product_id).filter(user=profile.pk).get()
            serializer.save()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)




@api_view(['GET',])
def products(request):

    filters = request.GET["filters"]
    products = Product.objects.all()[filters["start"]:filters["start"]+filters["size"]]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET',"POST","PUT","DELETE"])
def image(request):
    if request.method == "POST":
        try:
            user_data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
            profile_obj = Profile.objects.filter(user_id=user_data["user_id"]).get()
            product_obj = Product.objects.filter(profile=profile_obj,pk=request.data["product_id"]).get()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            serializer = ImageSerializer(data=request.data,many=False)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)            

    if request.method == "GET":
        try:
            product_id = request.GET["product_id"]
            product_obj = Product.objects.filter(pk=product_id).get()
            images = Image.objects.filter(product=product_obj).get()

            serializer = ImageSerializer(data=images,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

    if request.method == "DELETE":
        try:
            user_data = jwt.decode(request.data['jwt'].encode("UTF-8"), settings.SECRET_KEY, algorithm='HS256')
            profile_obj = Profile.objects.filter(user_id=user_data["user_id"]).get()
            product_obj = Product.objects.filter(profile=profile_obj,pk=request.data["product_id"]).get()
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
           image = Image.objects.filter(pk=request.data["image_id"]).get()
           image.delete()
        except Exception as e:
            return Response(status=status.HTTP_200_OK) 