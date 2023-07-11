from django.contrib import admin
from .models import Finch

# Register your models here.

class FinchAdminConfig(admin.ModelAdmin):
	list_display = ('id', 'name', 'colors', 'diet')
	ordering = ('id',)


admin.site.register(Finch, FinchAdminConfig)
