from django.contrib import admin
from .models import ToDoList
from .models import Product, Staff

# Register your models here.

admin.site.register(ToDoList)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'age')


admin.site.register(Product, ProductAdmin)
admin.site.register(Staff, StaffAdmin)


