from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Actors
from models import Series


def home(request):
    return render_to_response("tvmaniacs/home.html", {'welcome_msg': "Welcome to TvManiacs!"})


def actors(request):
    actors_all = Actors.objects
    return render_to_response("tvmaniacs/actors.html",
                              {'Actors': actors_all, "page_limit": Actors.page_limit()},
                              context_instance=RequestContext(request))


def series(request):
    series_all = Series.objects
    return render_to_response("tvmaniacs/series.html",
                              {'Series': series_all, "page_limit": Series.page_limit()},
                              context_instance=RequestContext(request))


def actor_details(request, imdb_id):
    actor = Actors.objects.get(imdb_id=imdb_id)
    return render_to_response("tvmaniacs/actor_details.html", {'Actor': actor})


def series_details(request, imdb_id):
    series = Series.objects.get(imdb_id=imdb_id)
    return render_to_response("tvmaniacs/series_details.html", {'Series': series})


def episodes(request, imdb_id, season_number):
    series = Series.objects.get(imdb_id=imdb_id)
    season = series.get_season(season_number)
    return render_to_response("tvmaniacs/episodes.html", {'Series': series, 'Season': season})