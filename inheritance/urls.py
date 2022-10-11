from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
]

