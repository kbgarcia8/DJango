from django.shortcuts import render
import json #when we request from api it is sent back in json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweather.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        #open a specific url; the appid is the API key
        json_data = json.loads(res) #will store the datas from the API
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' +  str(json_data['coord']['lat']),
            'temperature': str(json_data['main']['temp'])+'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
            #need info how the indexes are known
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})