from django.test import TestCase
from django.test.client import Client
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
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

    def test_actors_to_string(self):
        actors = Actors.objects
        for actor in actors:
            actor_str = actor.__unicode__()
            self.assertEqual(actor_str, actor.first_name+' '+actor.last_name)

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


class SeleniumTestMethods(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTestMethods, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SeleniumTestMethods, cls).tearDownClass()
        cls.selenium.quit()

    def test_navegation_bar(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))

        self.selenium.find_element_by_id("nav_actors").click()
        title_str = self.selenium.find_element_by_id("content_title").text
        self.assertEqual(title_str, "Actors")

        self.selenium.find_element_by_id("nav_series").click()
        title_str = self.selenium.find_element_by_id("content_title").text
        self.assertEqual(title_str, "Series")

    """
    def test_search(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        search_input = self.selenium.find_element_by_name("search")
        search_input.send_keys("Kevin Bacon")
        self.selenium.find_element_by_xpath('//input[@value="Search"]').click()
    """