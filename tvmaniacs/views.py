from django.shortcuts import render_to_response
from models import Actor
from models import Series


def home(request):
    return render_to_response("tvmaniacs/home.html", {'welcome_msg': "Hello TvManiacs World!"})


def actors(request):
    actors = Actor.objects
    return render_to_response("tvmaniacs/actors.html", {'Actors': actors})


def series(request):
    series = Series.objects
    return render_to_response("tvmaniacs/series.html", {'Series': series})


def actor_details(request, id):
    actor = Actor.objects.get(id=id)
    return render_to_response("tvmaniacs/actor_details.html", {'Actor': actor})

def series_details(request, id):
    series = Series.objects.get(id=id)
    return render_to_response("tvmaniacs/series_details.html", {'Series': series})