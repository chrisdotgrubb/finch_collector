from django.db import models
from django.urls import reverse


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
	
	def get_absolute_url(self):
		return reverse('finch:detail', kwargs={'pk': self.pk})


class Feeding(models.Model):
	MEAL_CHOICES = (
		('B', 'Breakfast'),
		('L', 'Lunch'),
		('D', 'Dinner'),
	)
	
	date = models.DateField(verbose_name='Feeding Date')
	meal = models.CharField(max_length=1, choices=MEAL_CHOICES, default='B')
	finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name='feedings')
	
	def __str__(self):
		return f'{self.get_meal_display()} on {self.date}'
	