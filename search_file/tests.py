from django.http import response
from django.test import TestCase
import os
import pandas as pd
import requests

# Create your tests here.
# def test_csv(TestCase):
#     fname = os.path.join(os.path.dirname(__file__), 'cities_canada-usa.csv')
#     pd.read_csv(fname)
    #self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
class Test(TestCase):
    def test_read_csv(self):
        response = requests.get("http://127.0.0.1:8000/suggestions/")
        response_body = response.json()
        assert response_body["name"] == "CA"