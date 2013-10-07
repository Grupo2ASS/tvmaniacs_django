from django.shortcuts import render_to_response
from models import Actor

def home(request):
    actors = Actor.objects
    return render_to_response("tvmaniacs/home.html", {'welcome_msg': "Hello TvManiacs World!", 'Actors': actors})