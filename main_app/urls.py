from django.urls import path

from . import views

app_name = 'finch'

urlpatterns = [
	path('', views.index, name='home'),
	path('about/', views.about, name='about'),
	path('finches/<int:pk>/', views.detail, name='detail'),
	path('finches/create/', views.FinchCreate.as_view(), name='create'),
	path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='update'),
	path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='delete'),
]
