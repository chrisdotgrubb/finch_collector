from django.shortcuts import render

from .models import Finch

# Create your views here.


def index(request):
	context = {
		'finches': Finch.objects.all(),
	}
	return render(request, 'index.html', context)


def about(request):
	return render(request, 'about.html', context={})
