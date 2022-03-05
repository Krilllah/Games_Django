from django.urls import include, path
from django.http import HttpRequest

from . import views

urlpatterns = [
    path('404', views.getNotFound),
    path('<name>', views.getinfo)
]