from django.contrib import admin
from .models import Category, Car

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', 'price', 'category', 'is_published', 'image')
    search_fields = ('make', 'model', 'category__name')
    list_filter = ('is_published',)
    fields = ('make', 'model', 'year', 'price', 'category', 'is_published', 'image')  # Добавлено поле изображения

admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)
