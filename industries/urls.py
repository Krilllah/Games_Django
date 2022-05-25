from django.urls import include, path, re_path
from django.http import HttpRequest
from . import views
from .views import *

urlpatterns = [
    path('add_industry/', views.add_industry, name='add_industry'),
    path('add_franchise/', views.add_franchise, name='add_franchise'),
    path('add_game/', views.add_game, name='add_game'),
]
