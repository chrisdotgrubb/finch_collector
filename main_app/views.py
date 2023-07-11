from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

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

class FinchCreate(generic.CreateView):
	model = Finch
	fields = '__all__'

class FinchUpdate(generic.UpdateView):
	model = Finch
	fields = '__all__'

class FinchDelete(generic.DeleteView):
	model = Finch
	success_url = reverse_lazy('finch:home')
