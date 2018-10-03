from django.urls import path
from django import views
from .views import index

urlpatterns = [
    path('', index, name='index'),    
]