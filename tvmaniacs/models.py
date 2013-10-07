from mongoengine import *
from tvmaniacs_django.settings import DBNAME

connect(DBNAME)

class Actor(Document):
    firstname = StringField(max_length=255, required=True)
    lastname = StringField(max_length=255, required=True)