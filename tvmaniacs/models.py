from mongoengine import *
from tvmaniacs_django.settings import DBNAME

connect(DBNAME)

class Actor(Document):
    first_name = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    id = IntField()
    bio = StringField()
    birthdate = DateTimeField()
    birth_place = StringField(max_length=255)


class Series(Document):
    name = StringField(max_length=255, required=True)
    year_start = DateTimeField()
    user_rating = StringField()
    description = StringField()

