from django.contrib import admin
from .models import Finch, Feeding

# Register your models here.

class FinchAdminConfig(admin.ModelAdmin):
	list_display = ('id', 'name', 'colors', 'diet')
	ordering = ('id',)


class FeedingAdminConfig(admin.ModelAdmin):
	list_display = ('date', 'meal', 'finch')
	ordering = ('finch',)
	
	
admin.site.register(Finch, FinchAdminConfig)
admin.site.register(Feeding, FeedingAdminConfig)
