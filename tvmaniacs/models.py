from mongoengine import *
from django.db import models
from tvmaniacs_django.settings import DBNAME


connect(DBNAME)


class Review(EmbeddedDocument):
    score = IntField()
    name = StringField()
    institution = StringField()
    comment = StringField()
    date = DateTimeField()
    critic = BooleanField()
    link = URLField()


class Episode(EmbeddedDocument):
    name = StringField()
    user_rating = IntField(min_value=0, max_value=10)
    description = StringField()


class Season(EmbeddedDocument):
    number = StringField(required=True)
    date = DateTimeField()
    chapters = ListField(EmbeddedDocumentField(Episode))
    reviews = ListField(EmbeddedDocumentField(Review))


class Series(Document):
    imdb_id = StringField(max_length=15, required=True)
    name = StringField(max_length=255, required=True)
    year = DateTimeField()
    year_start = DateTimeField()
    year_end = DateTimeField()
    user_rating = IntField(min_value=0, max_value=10)
    metascore = IntField(min_value=0, max_value=100)
    length = IntField()
    description = StringField()
    genres = ListField(StringField())
    pic = URLField()
    seasons = ListField(EmbeddedDocumentField(Season))
    cast = ListField()

    def timespan(self):
        return '(' + self.year_start + ' - ' + self.year_end + ')'

    def get_cast(self):
        return Actor.objects.filter(imdb_id__in=self.cast)

    def get_season(self, season_number):
        for s in self.seasons:
            if s.number == season_number:
                return s
        return {}

    def get_length(self):
        return str(self.length) + ' min'

    def __unicode__(self):
        return self.name


class Actor(Document):
    imdb_id = StringField(max_length=15, required=True)
    first_name = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    score = IntField(min_value=0, max_value=100)
    high_score = IntField(min_value=0, max_value=100)
    low_score = IntField(min_value=0, max_value=100)
    pic = URLField()
    bio = StringField()
    birth_date = DateTimeField()
    birth_place = StringField(max_length=255)
    series = ListField()

    def get_series(self):
        return Series.objects.filter(imdb_id__in=self.series)

    def has_scores(self):
        if self.score and self.high_score and self.low_score:
            return True

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
