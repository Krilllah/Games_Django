from django.http import HttpResponse


def index(request):
    return HttpResponse('Here are our franchises: Call_of_Duty/ Warcraft/')