from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="index"),
	path('index',views.index,name="index"),
	path('input',views.input,name="input"),
]