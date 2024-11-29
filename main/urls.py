from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_route, name='calculate_route'),
    path('calculate_route/', views.calculate_route, name='calculate_route'),
]
