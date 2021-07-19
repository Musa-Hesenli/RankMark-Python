from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.CategoryModel)

@admin.register(models.Hotels)
class RestaurantModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
