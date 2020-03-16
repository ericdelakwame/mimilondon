from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Customer, Staff
)


admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Staff)



