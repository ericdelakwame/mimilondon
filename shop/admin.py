from django.contrib import admin
from .models import (
    SubCategory, Category, Product, Size, Color
)


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)


