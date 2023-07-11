from django.urls import path

from . import views

app_name = 'finch'

urlpatterns = [
	path('', views.index, name='home'),
	path('about/', views.about, name='about'),
	path('finches/<int:pk>/', views.detail, name='detail'),
	path('finches/create/', views.FinchCreate.as_view(), name='create')
]
