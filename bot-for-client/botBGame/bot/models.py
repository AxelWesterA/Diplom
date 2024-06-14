from django.db import models

# Create your models here.
# bot/models.py
from django.db import models

class Admin(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    available = models.BooleanField(default=True)

class Client(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    assigned_admin = models.ForeignKey(Admin, null=True, blank=True, on_delete=models.SET_NULL)
