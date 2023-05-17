from cgi import print_exception
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    image = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=200)
    shipping = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category_id = models.IntegerField()
    featured = models.BooleanField()
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
