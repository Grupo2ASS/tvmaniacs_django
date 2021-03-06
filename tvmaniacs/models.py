from mongoengine import *


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
    user_rating = FloatField(min_value=0, max_value=10)
    description = StringField()

    def get_s_name(self):
        s_name = self.name
        s_name = s_name.replace(" ", "")
        s_name = s_name.lower()
        return s_name


class Season(EmbeddedDocument):
    number = IntField(required=True)
    date = DateTimeField()
    chapters = ListField(EmbeddedDocumentField(Episode))
    reviews = ListField(EmbeddedDocumentField(Review))

    def get_chapter(self, chapter_name):
        for c in self.chapters:
            s_name = c.name
            s_name = s_name.replace(" ", "")
            s_name = s_name.lower()
            if s_name == chapter_name:
                return c
        return {}


class Series(Document):
    imdb_id = StringField(max_length=15, required=True)
    name = StringField(max_length=255, required=True)
    year_start = DateTimeField()
    year_end = DateTimeField()
    user_rating = FloatField(min_value=0, max_value=10)
    metascore = IntField(min_value=0, max_value=100)
    length = IntField()
    description = StringField()
    genres = ListField(StringField())
    pic = URLField()
    seasons = ListField(EmbeddedDocumentField(Season))
    cast = ListField()

    @staticmethod
    def page_limit():
        return 20

    @staticmethod
    def all_ordered_alphabetically():
        return Series.objects.only('imdb_id', 'name', 'user_rating', 'year_start', 'year_end', 'description')\
            .order_by('name')

    @staticmethod
    def all_order_by_rating():
        return Series.objects.only('imdb_id', 'name', 'user_rating', 'year_start', 'year_end', 'description')\
            .order_by('-user_rating')

    def timespan(self):
        if self.year_start:
            start = self.year_start
        else:
            start = ''
        if self.year_end:
            end = self.year_end
        else:
            end = ''
        return '(' + str(start) + ' - ' + str(end) + ')'

    def get_cast(self):
        return Actors.objects.filter(imdb_id__in=self.cast)

    def get_season(self, season_number):
        for s in self.seasons:
            if s.number == int(season_number):
                return s
        return {}

    def get_length(self):
        return str(self.length) + ' min'


    def __unicode__(self):
        return self.name


class Actors(Document):
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
    bacon_number = IntField(min_value=0) 

    @staticmethod
    def page_limit():
        return 20

    @staticmethod
    def all_ordered_alphabetically():
        return Actors.objects.only('imdb_id', 'first_name', 'last_name').order_by('first_name', 'last_name')

    def get_series(self):
        return Series.objects.filter(imdb_id__in=self.series)


    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
