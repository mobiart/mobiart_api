from django.db import models


class Product(models.Model):
    user = models.ForeignKey('profile_manager.Profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    price_upon_request = models.BooleanField(default = False)
    price = models.FloatField()
    active = models.BooleanField(default = False)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField()

class Bookmark(models.Model):
    user = models.ForeignKey('profile_manager.Profile', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
