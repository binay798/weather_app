from django.shortcuts import render
import requests
from .forms import NameForm

# Create your views here.
def index(request):
    api_key = '603b358dc9494673e4441df6be18f137'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    
    if request.method == 'POST':
        name = request.POST["name"]
        r = requests.get(url.format(name,api_key)).json()
        return render(request,'weather/index.html',{
            'name':name,
            'desc':r['weather'][0]['description'],
            'temp':r['main']['temp'],
            'icon':r['weather'][0]['icon'],
            'r':r,
            'desc':r['weather'][0]['description']
        })

    
    else:
        
        return render(request,'weather/index.html')


    
    


    