from django.contrib import admin
from .models import Category


# Register your models here.
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'slug']
    prepopulated_fields = {'slug': ('name',)}
