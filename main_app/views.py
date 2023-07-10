from django.shortcuts import render

# Create your views here.
finches = [
	{
		'name': 'American Goldfinch',
		'color': 'black and yellow',
		'diet': 'vegetarian',
	},
	{
		'name': 'House Finch',
		'color': 'red and brown',
		'diet': 'seeds',
	},
	{
		'name': 'Red Crossbill',
		'color': 'red and black',
		'diet': 'pinecones',
	},
	{
		'name': 'Purple Finch',
		'color': 'purple and red',
		'diet': 'sunflower seeds',
	},
	{
		'name': 'Blue Grosbeak',
		'color': 'blue and silver',
		'diet': 'seeds',
	},
]


def index(request):
	context = {
		'finches': finches,
	}
	return render(request, 'index.html', context)


def about(request):
	return render(request, 'about.html', context={})
