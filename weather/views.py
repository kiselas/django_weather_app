import requests
import json
from django.shortcuts import render
from decouple import config
from the_weather.settings import X_RAPIDAPI_KEY, X_RAPIDAPI_HOST
from .models import City
from .forms import CityForm


def index(request):

    cities = City.objects.all()
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:

        url = f"https://aerisweather1.p.rapidapi.com/forecasts/{city.code}"

        querystring = {"to": "2021-07-23"}

        headers = {
            'x-rapidapi-key': "c5c06c67cbmsh30ad3f4a6427604p18616djsn34847ba0019f",
            'x-rapidapi-host': "aerisweather1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        maxTemp = json.loads(response.text)['response'][0]['periods'][0]['maxTempC']
        minTemp = json.loads(response.text)['response'][0]['periods'][0]['minTempC']
        weather = json.loads(response.text)['response'][0]['periods'][0]['weather']
        icon = json.loads(response.text)['response'][0]['periods'][0]['icon']

        avgTemp = (maxTemp + minTemp)/2
        city_weather = {'city': city.name, 'avgTemp': avgTemp, 'weather_type': weather, 'icon': icon}

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    print(weather_data)
    return render(request, 'weather/weather.html', context)
