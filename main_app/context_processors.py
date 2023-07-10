from .views import finches

def nav_finches(request):
	return {'nav_finches': finches}