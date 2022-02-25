from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, there are list of game industries:  Electronic_Arts/ - Nintendo/ - Activision_Blizzard/')