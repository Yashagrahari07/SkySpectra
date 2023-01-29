from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=ecd55b265bce9fa821b3000b08b88256').read()
        api_dict = json.loads(api_url)
        weather_data = {
            "country": city,
            "weather_description": api_dict['weather'][0]['description'],
            "weather_temperature": api_dict['main']['temp'],
            "weather_pressure": api_dict['main']['pressure'],
            "weather_humidity": api_dict['main']['humidity'],
            "weather_icon": api_dict['weather'][0]['icon'],
        }
        print(weather_data)
    else:
        city = None
        weather_data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity":None,
            "weather_icon": None,
        }
    return render(request,'index.html',{"city": city, "data" :weather_data})
