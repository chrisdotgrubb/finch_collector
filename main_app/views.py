from django.shortcuts import render, get_object_or_404

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
	print(context, pk)
	return render(request, 'detail.html', context)
