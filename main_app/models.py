from datetime import date

from django.db import models
from django.db.models import UniqueConstraint, Case, When, Value
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
	
	# check if finch was fed 3 times today
	def fed_today(self):
		return self.feedings.filter(date=date.today()).count() > 2

class FeedingManager(models.Manager):
	def get_queryset(self):
		p = Case(
			When(meal='B', then=Value(1)),
			When(meal='L', then=Value(2)),
			When(meal='D', then=Value(3)),
		)
		return super().get_queryset().alias(priority_order=p).order_by('-date', '-priority_order')
	
class Feeding(models.Model):
	MEAL_CHOICES = (
		('B', 'Breakfast'),
		('L', 'Lunch'),
		('D', 'Dinner'),
	)
	
	date = models.DateField(verbose_name='Feeding Date')
	meal = models.CharField(max_length=1, choices=MEAL_CHOICES, default='B')
	finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name='feedings')
	
	objects = FeedingManager()
	
	def __str__(self):
		return f'{self.get_meal_display()} on {self.date}'
	
	class Meta:
		ordering = ('finch', '-date')
		constraints = [UniqueConstraint('date', 'meal', 'finch', name='finch_feeding_daily_meal_unique', violation_error_message='This Finch was already fed this meal for this day.')]
	
