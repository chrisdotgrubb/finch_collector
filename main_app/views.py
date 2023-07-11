from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Finch
from .forms import FeedingForm


def index(request):
	context = {
		'finches': Finch.objects.all(),
	}
	return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html', context={})

def detail(request, pk):
	finch = get_object_or_404(Finch, pk=pk)
	feeding_form = FeedingForm()
	context = {
		'finch': finch,
		'feeding_form': feeding_form,
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

def add_feeding(request, pk):
	feeding_form = FeedingForm(request.POST)
	if feeding_form.is_valid():
		new_feeding = feeding_form.save(commit=False)
		new_feeding.finch_id = pk
		new_feeding.save()
	return redirect('finch:detail', pk=pk)
