from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Warcraft/', include('A_Blizzard_Warcraft.urls')),
]