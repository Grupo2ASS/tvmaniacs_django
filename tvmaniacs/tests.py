from django.test import TestCase
from django.test.client import Client
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from models import Actors
from models import Series


class SeriesTestMethods(TestCase):

    def test_series_to_string(self):
        series_list = Series.objects
        for series in series_list:
            series_str = series.__unicode__()
            self.assertEqual(series_str, series.name)

    def test_series_uniqueness(self):
        series_freq = Series.objects.item_frequencies('imdb_id')
        max_freq = 0
        for key, value in series_freq.iteritems():
            if max_freq < value:
                max_freq = value
        self.assertLessEqual(max_freq, 1)


class ActorsTestMethods(TestCase):
    def test_actors_to_string(self):
        actors = Actors.objects
        for actor in actors:
            actor_str = actor.__unicode__()
            self.assertEqual(actor_str, actor.first_name+' '+actor.last_name)

    def test_actors_uniqueness(self):
        actors_freq = Series.objects.item_frequencies('imdb_id')
        max_freq = 0
        for key, value in actors_freq.iteritems():
            if max_freq < value:
                max_freq = value
        self.assertLessEqual(max_freq, 1)


class PageExistTestMethods(TestCase):
    def setUp(self):
        self.client = Client()

    def test_series_list_exist(self):
        response = self.client.get('/series/')
        self.assertEqual(response.status_code, 200)

    def test_series_details_exist(self):
        first_series = Series.objects[0]
        response = self.client.get('/series/'+first_series.imdb_id+'/')
        self.assertEqual(response.status_code, 200)

    def test_season_exist(self):
        series_list = Series.objects
        url_season = ''
        for series in series_list:
            if len(series.seasons) > 0:
                url_season = '/series/'+series.imdb_id+'/'+str(series.seasons[0].number)+'/'
                print(url_season)
                break
        response = self.client.get(url_season)
        self.assertEqual(response.status_code, 200)

    def test_actor_list_exist(self):
        response = self.client.get('/actors/')
        self.assertEqual(response.status_code, 200)

    def test_actor_details_exist(self):
        first_actor = Actors.objects[0]
        response = self.client.get('/actor/'+first_actor.imdb_id+'/')
        self.assertEqual(response.status_code, 200)


class SeleniumTestMethods(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTestMethods, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SeleniumTestMethods, cls).tearDownClass()
        cls.selenium.quit()

    def test_nav_bar(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))

        self.selenium.find_element_by_id("nav_actors").click()
        title_str = self.selenium.find_element_by_id("content_title").text
        self.assertEqual(title_str, "Actors")

        self.selenium.find_element_by_id("nav_series").click()
        title_str = self.selenium.find_element_by_id("content_title").text
        self.assertEqual(title_str, "Series")

    def test_actors_search(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        self.selenium.find_element_by_id("nav_actors").click()
        search_input = self.selenium.find_element_by_id("actor_search_input")
        search_input.send_keys("Kevin Bacon")
        self.selenium.find_element_by_id("actor_search_button").click()
        self.assertTrue(self.selenium.find_element_by_class_name("search_message"))

    def test_series_search(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        self.selenium.find_element_by_id("nav_series").click()
        search_input = self.selenium.find_element_by_id("series_search_input")
        search_input.send_keys("Game of Thrones")
        self.selenium.find_element_by_id("series_search_button").click()
        self.assertTrue(self.selenium.find_element_by_class_name("search_message"))