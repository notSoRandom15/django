from django.shortcuts import make_toasts
from django.test import SimpleTestCase

class MakeToastsTests(SimpleTestCase):
    def test_make_toasts(self):
        self.assertEqual(make_toasts(), 'toast')