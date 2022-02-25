from django.http import HttpResponse


def index(request):
    return HttpResponse('Here are our franchises: Battlefield/ Plants_vs_Zombies/ ')