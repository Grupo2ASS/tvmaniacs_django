from mongoengine import *
from django.db import models
from tvmaniacs_django.settings import DBNAME


connect(DBNAME)


class Series(Document):
    name = StringField(max_length=255, required=True)
    year = DateTimeField()
    year_start = DateTimeField()
    year_end = DateTimeField()
    user_rating = StringField()
    description = StringField()
    seasons = ListField()
    genres = ListField()
    pic = URLField()
    cast = ListField()


class Actor(Document):
    first_name = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    id = IntField()
    pic = URLField()
    bio = StringField()
    birth_date = DateTimeField()
    birth_place = StringField(max_length=255)
    series = ListField()
  #  series = ReferenceField(Series, reverse_delete_rule=DO_NOTHING)


class Season(models.Model):
    number = IntField()
    year = DateTimeField()


