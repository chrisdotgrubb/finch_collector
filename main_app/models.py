from django.db import models


# Create your models here.

class Finch(models.Model):
	name = models.CharField(max_length=255)
	colors = models.CharField(max_length=255)
	diet = models.CharField(max_length=255)
	
	class Meta:
		verbose_name = 'Finch'
		verbose_name_plural = 'Finches'
	
	def __str__(self):
		return f'{self.name} ({self.id})'
