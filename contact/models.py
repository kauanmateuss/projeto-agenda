from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name



class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, blank=True) # blank = True é pra dizer se o campo é opcional
    email = models.EmailField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)   # esse timezone.now vai colocar a data automaticamente
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)    


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'