from email.policy import default
from time import timezone
from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="images/", max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    key_features = models.TextField()
    specification = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    actual_price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", max_length=100)
    is_stock = models.BooleanField(default=True)
    product_code = models.CharField(max_length=255, unique=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-created_at']


    def __str__(self):
        return self.name
