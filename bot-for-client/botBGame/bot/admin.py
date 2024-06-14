from django.contrib import admin

# Register your models here.
# bot/admin.py
from django.contrib import admin
from .models import Admin, Client

admin.site.register(Admin)
admin.site.register(Client)
