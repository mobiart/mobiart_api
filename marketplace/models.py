from django.db import models
from profile_manager.models import Profile

class Product(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    active = models.BooleanField(default = False)

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField()

class Bookmark(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
