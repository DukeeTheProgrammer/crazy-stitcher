from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    no_of_items_available_items = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="static/store/images/category_pics")
    description = models.TextField(default="No Description")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=False)
    pic_url = models.ImageField(upload_to="store/static/store/images/")
    quantity = models.IntegerField(default=0)
    description = models.TextField(default="No description for this product")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(datetime.utcnow)

    def __str__(self):
        return self.name

class Review(models.Model):
    username = models.CharField(max_length=200, default="Anonymous User")
    review = models.TextField(max_length=400)
    date = models.DateField(default=datetime.utcnow)
