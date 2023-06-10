from django.urls import path
from . import views

urlpatterns = [
    path('storehome', views.home)
    
]