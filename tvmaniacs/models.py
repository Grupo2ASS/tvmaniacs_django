from mongoengine import *
from django.db import models
from tvmaniacs_django.settings import DBNAME

connect(DBNAME)


class Actor(Document):
    first_name = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    id = IntField()
    pic = URLField()
    bio = StringField()
    birth_date = DateTimeField()
    birth_place = StringField(max_length=255)


class Series(Document):
    name = StringField(max_length=255, required=True)
    year_start = DateTimeField()
    user_rating = StringField()
    description = StringField()
    seasons = ListField()
    pic = URLField()

class Season(models.Model):
    number = IntField()
   # series = models.ForeignKey(Series)

