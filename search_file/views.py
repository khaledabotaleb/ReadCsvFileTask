from os import X_OK
from django.shortcuts import render
import pandas
import numpy as np
from rest_framework.response import Response
from rest_framework.views import APIView


class GetCitiesSuggestions(APIView):

    def get(self, request):
        country = request.query_params.get('q')
        latitude = request.query_params.get('lat')
        longitude = request.query_params.get('long')
        # names=['name', 'country', 'lat', 'long']
        data = pandas.read_csv('cities_canada-usa.csv', usecols=['name', 'country', 'lat', 'long'])
        # print(data)
        data = data[(data['country'] == country) | (data['lat']== latitude) | (data['long']== longitude)]
        # sorting dataframe
        # data.sort_values("name", inplace=True)
        
        # making boolean series for a team name
        # filter1 = data["name"] == "Airdrie"

        # making boolean series for age
        # filter2 = data["Age"] > 24

        # filtering data on basis of both filters
        # data.where(filter1, inplace=True)
        x = data.values.tolist()
        # print(typex)
        # display
        suggestions = []
        # print(x)
        for item in x:
            
            suggestions.append({
                "country": item[3],
                "latitude": item[1],
                "longitude": item[2]
            })
            
        return Response({'suggestions': suggestions}, 200)


