from django.contrib import admin
from .models import User_data, Customer
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(User_data)
admin.site.register(Customer)