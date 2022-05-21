from django.contrib import admin
from .models import ToDoList
from .models import Product

# Register your models here.

admin.site.register(ToDoList)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)

