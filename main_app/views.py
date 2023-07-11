from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from .models import Finch

# Create your views here.


def index(request):
	context = {
		'finches': Finch.objects.all(),
	}
	return render(request, 'index.html', context)


def about(request):
	return render(request, 'about.html', context={})

def detail(request, pk):
	context = {
		'finch': get_object_or_404(Finch, pk=pk),
	}
	return render(request, 'detail.html', context)

class FinchCreate(CreateView):
	model = Finch
	fields = '__all__'
