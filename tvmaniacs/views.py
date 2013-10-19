from django.shortcuts import render_to_response
from models import Actor
from models import Series


def home(request):
    return render_to_response("tvmaniacs/home.html", {'welcome_msg': "Welcome to TvManiacs!"})


def actors(request):
    actors_all = Actor.objects
    return render_to_response("tvmaniacs/actors.html", {'Actors': actors_all})


def series(request):
    series_all = Series.objects
    return render_to_response("tvmaniacs/series.html", {'Series': series_all})


def actor_details(request, imdb_id):
    actor = Actor.objects.get(imdb_id=imdb_id)
    return render_to_response("tvmaniacs/actor_details.html", {'Actor': actor})


def series_details(request, imdb_id):
    series = Series.objects.get(imdb_id=imdb_id)
    return render_to_response("tvmaniacs/series_details.html", {'Series': series})


def episodes(request, imdb_id, season):
    series = Series.objects.get(imdb_id=imdb_id)
    return render_to_response("tvmaniacs/episodes.html", {'Series': series, 'Num': season})