from django.db import models
from marketplace.models import Product

class Profile(models.Model):
    access_token = models.TextField()
    user_id = models.CharField(max_length=30)
    platform = models.CharField(max_length=30)
    subscribed = models.BooleanField(default=True)