from mongoengine import *
from django.db import models
from tvmaniacs_django.settings import DBNAME


connect(DBNAME)


class Season(EmbeddedDocument):
    number = StringField()
    date = DateTimeField()
    episodes = ListField()
    chapters = ListField()
    #reviews


class Series(Document):
    imdb_id = StringField(max_length=15, required=True)
    name = StringField(max_length=255, required=True)
    year = DateTimeField()
    year_start = DateTimeField()
    year_end = DateTimeField()
    user_rating = StringField()
    description = StringField()
    genres = ListField()
    pic = URLField()
    seasons = ListField(EmbeddedDocumentField(Season))
    cast = ListField()

    def timespan(self):
        return '(' + self.year_start + ' - ' + self.year_end + ')'

    def get_cast(self):
        return Actor.objects.filter(imdb_id__in=self.cast)

    def get_season(self, season_number):
        print self.seasons
        for s in self.seasons:
            if s.number == season_number:
                return s
        return {}

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

    def get_series(self):
        return Series.objects.filter(imdb_id__in=self.series)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)



