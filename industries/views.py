from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from industries.forms import AddIndustry, AddFranchise, AddGame
from industries.models import Industry, Franchise, Game


def home(request):
    return HttpResponse(render_to_string('industry_names/home.html'))


def get_industries(request):
    industries = Industry.objects.all()
    return render(request, 'industry_names/my_industries.html', {"industries": industries})


def get_franchises(request):
    franchises = Franchise.objects.all()
    return render(request, 'industry_names/my_franchises.html', {"franchises": franchises})


def get_games(request):
    games = Game.objects.all()
    return render(request, 'industry_names/my_games.html', {"games": games})


def add_industry(request):
    if request.method == 'POST':
        form = AddIndustry(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddIndustry()
    return render(request, 'industry_names/industry.html', {'form': form})


def add_franchise(request):
    if request.method == 'POST':
        form = AddFranchise(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddFranchise()
    return render(request, 'industry_names/franchise.html', {'form': form})


def add_game(request):
    if request.method == 'POST':
        form = AddGame(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddGame()
    return render(request, 'industry_names/game.html', {'form': form})


def getNotFound(request):
    return HttpResponse(render_to_string('industry_names/404.html'))
