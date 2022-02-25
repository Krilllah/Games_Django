from django.http import HttpResponse


def index(request):
    return HttpResponse('Here are our franchises: The_Legend_of_Zelda/ Donkey_Kong/')
