from django.contrib import admin
from django.urls import path

from songs import views


urlpatterns = [
    path('', views.home, name='home')
]