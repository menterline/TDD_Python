from django.test import TestCase

class SmokeTest(TestCase):

    def test_badMath(self):
        self.assertEqual(1+1, 3)
# Create your tests here.
