from django.forms import ModelForm, DateInput
from .models import Feeding


class CustomDateInput(DateInput):
	input_type = 'date'


class FeedingForm(ModelForm):
	class Meta:
		model = Feeding
		fields = ['date', 'meal']
		widgets = {'date': CustomDateInput()}
