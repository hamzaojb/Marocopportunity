# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_publications, name='publications'),
]
