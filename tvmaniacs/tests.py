from django.test import TestCase
from django.test.client import Client
from models import Actors
from models import Series


class SeriesTestMethods(TestCase):
    def setUp(self):
        self.client = Client()

    def test_series_list_exist(self):
        response = self.client.get('/series/')
        self.assertEqual(response.status_code, 200)

    def test_series_list_limit(self):
        response = self.client.get('/series/')
        # Check that the rendered context contains a limited amount of series.
        self.assertLessEqual(len(response.context['Series']), Series.page_limit())

    def test_series_uniqueness(self):
        series_freq = Series.objects.item_frequencies('imdb_id')
        max_freq = 0
        for key, value in series_freq.iteritems():
            if max_freq < value:
                max_freq = value
        self.assertLessEqual(max_freq, 1)


class ActorTestMethods(TestCase):
    def setUp(self):
        self.client = Client()

    def test_actor_list_exist(self):
        response = self.client.get('/actors/')
        self.assertEqual(response.status_code, 200)

    def test_actor_list_limit(self):
        response = self.client.get('/actors/')
        # Check that the rendered context contains a limited amount of actors.
        self.assertLessEqual(len(response.context['Actors']), Actors.page_limit())

    def test_actor_uniqueness(self):
        actors_freq = Series.objects.item_frequencies('imdb_id')
        max_freq = 0
        for key, value in actors_freq.iteritems():
            if max_freq < value:
                max_freq = value
        self.assertLessEqual(max_freq, 1)
