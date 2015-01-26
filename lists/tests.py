from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_URLresolve(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
# Create your tests here.
