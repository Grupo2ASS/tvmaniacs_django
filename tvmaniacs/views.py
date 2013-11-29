from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Actors
from models import Series
from models import Episode

VALID_SERIES_SORTS = {
    "name": "name",
    "rating": "rating"
}
VALID_ACTORS_SORT = {
    "name": "name",
    "bacon": "bacon"
}
DEFAULT_SORT = 'name'


def home(request):
    return render_to_response('tvmaniacs/home.html', {'welcome_msg': 'Welcome to TvManiacs!'})


def actors(request):
    sort_key = request.GET.get('sort', DEFAULT_SORT)
    sort = VALID_ACTORS_SORT.get(sort_key, DEFAULT_SORT)

    #TODO: Ordered by Bacon number instead of alphabetically.
    if sort == 'bacon':
        actors_all = Actors.all_ordered_alphabetically()
    else:
        actors_all = Actors.all_ordered_alphabetically()

    if 'search_query' in request.GET:
        return search_actors(request, actors_all)
    else:
        return render_to_response('tvmaniacs/actors.html',
                                  {'Actors': actors_all, 'page_limit': Actors.page_limit()},
                                  context_instance=RequestContext(request))


def series(request):
    sort_key = request.GET.get('sort', DEFAULT_SORT)
    sort = VALID_SERIES_SORTS.get(sort_key, DEFAULT_SORT)

    if sort == 'rating':
        series_all = Series.all_order_by_rating()
    else:
        series_all = Series.all_ordered_alphabetically()

    if 'search_query' in request.GET:
        return search_series(request, series_all)
    else:
        return render_to_response('tvmaniacs/series.html',
                                  {'Series': series_all, 'page_limit': Series.page_limit()},
                                  context_instance=RequestContext(request))


def actor_details(request, imdb_id):
    actor = Actors.objects.get(imdb_id=imdb_id)
    return render_to_response('tvmaniacs/actor_details.html', {'Actor': actor})


def series_details(request, imdb_id):
    series = Series.objects.get(imdb_id=imdb_id)
    return render_to_response('tvmaniacs/series_details.html', {'Series': series})


def episodes(request, imdb_id, season_number):
    series = Series.objects.get(imdb_id=imdb_id)
    season = series.get_season(season_number)
    return render_to_response('tvmaniacs/episodes.html', {'Series': series, 'Season': season})


def episode_details(request, imdb_id, season_number, name):
    series = Series.objects.get(imdb_id=imdb_id)
    season = series.get_season(season_number)
    episode = season.get_chapter(name)
    return render_to_response('tvmaniacs/episode_details.html', {'Series': series, 'Season': season, 'Episode': episode})


##---------------------------------- INTERNAL METHODS---------------------------------------------------
def search_series(request, series_list):
    text = request.GET["search_query"]
    found_series = series_list.filter(name__icontains=text)
    message = 'Results: ' + str(len(found_series))
    return render_to_response('tvmaniacs/series.html',
                              {'Series': found_series, 'page_limit': Series.page_limit(),
                               'search_message': message}, context_instance=RequestContext(request))


def search_actors(request, actors_list):
    text = request.GET["search_query"]
    found_actors = actors_list.filter(first_name__icontains=text)
    message = "Results: " + str(len(found_actors))
    return render_to_response('tvmaniacs/actors.html',
                              {'Actors': found_actors, 'page_limit': Actors.page_limit(),
                               'search_message': message }, context_instance=RequestContext(request))