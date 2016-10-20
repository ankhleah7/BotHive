from django.test import TestCase
from django.test import Client



class test_bot(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/bots/')
        self.assertEqual(response.status_code, 200)
