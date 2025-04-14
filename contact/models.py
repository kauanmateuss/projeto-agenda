from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, blank=True) # blank = True é pra dizer se o campo é opcional
    email = models.EmailField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)   # esse timezone.now vai colocar a data automaticamente
    description = models.TextField(blank=True)