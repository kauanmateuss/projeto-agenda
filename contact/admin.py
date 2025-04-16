from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Definindo os campos que aparecem
    list_display = 'id', 'first_name', 'last_name', 'phone'
    # Ordenando os contatos
    ordering = '-id',   # Ordenado com id decrescente

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',