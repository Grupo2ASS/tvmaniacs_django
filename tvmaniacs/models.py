from mongoengine import *
from django.db import models
from tvmaniacs_django.settings import DBNAME


connect(DBNAME)


class Series(Document):
    imdb_id = StringField(max_length=15, required=True)
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

    @staticmethod
    def get_actors_objects(series_id):
        actors = Actor.objects.filter(imdb_id__in=Series.objects.get(imdb_id=series_id).cast)
        return actors

    def __unicode__(self):
        return self.name


class Actor(Document):
    imdb_id = StringField(max_length=15, required=True)
    first_name = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    pic = URLField()
    bio = StringField()
    birth_date = DateTimeField()
    birth_place = StringField(max_length=255)
    series = ListField()

    @staticmethod
    def get_series_objects(actor_id):
        series = Series.objects.filter(imdb_id__in=Actor.objects.get(imdb_id=actor_id).series)
        return series

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Season(models.Model):
    number = IntField()
    year = DateTimeField()
    #series = models.ForeignKey(Series)


