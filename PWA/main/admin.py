from django.contrib import admin
from .models import menu



class MenuAdmin(admin.ModelAdmin):
    list_display = ("item","price")

# Register your models here.
admin.site.register(menu, MenuAdmin)
