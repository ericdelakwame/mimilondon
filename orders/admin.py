from django.contrib import admin
from .models import Order, OrderItem
from django.contrib.gis.admin import OSMGeoAdmin


admin.site.register(Order, OSMGeoAdmin)
admin.site.register(OrderItem)
