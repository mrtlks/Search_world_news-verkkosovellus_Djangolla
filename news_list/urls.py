#from django.contrib import admin --> ei tarvita sovellustasolla
from django.urls import path
from .import views

urlpatterns = [
    path('', views.frontpage, name ='frontpage'),
    path('newspage', views.newspage, name ='newspage'),
]
