from django.shortcuts import render
import requests
from .models import City
def index(request):
    appid = 'f0267f73b973e2f7cc32b86b7c1f58e6'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    # city = 'Cherepovets'
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities}

    return render(request, 'weather/index.html',context)
