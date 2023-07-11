from .models import Finch

def nav_finches(request):
	return {'nav_finches': Finch.objects.all()}