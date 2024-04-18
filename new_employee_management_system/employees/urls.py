from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('employees/', views.employees, name='employees'),
    path('employees/details/<slug:slug>', views.details, name='details'),
]
