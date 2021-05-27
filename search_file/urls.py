from django.urls import path
from .views import *

urlpatterns=[
    path('suggestions/', GetCitiesSuggestions.as_view(), name='get-cities')
]