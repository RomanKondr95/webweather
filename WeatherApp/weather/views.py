from django.shortcuts import render
import requests
def index(request):
    appid = 'f0267f73b973e2f7cc32b86b7c1f58e6'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Cherepovets'
    response = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': response["main"]["temp"],
        'icon': response["weather"][0]["icon"]
    }
    context = {'info': city_info}

    return render(request, 'weather/index.html',context)
