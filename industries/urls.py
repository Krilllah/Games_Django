from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Electronic_Arts/', include('Electronic_Arts_franchises.urls')),
    path('Nintendo/', include('Nintendo_franchises.urls')),
    path('Activision_Blizzard/', include('Activision_Blizzard_franchises.urls'))

]