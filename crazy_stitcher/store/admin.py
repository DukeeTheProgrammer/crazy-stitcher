from django.contrib import admin
from .models import Product, Category, Review
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)

