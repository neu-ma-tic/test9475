import os
import json
import requests
base_url="https://api.openweathermap.org/data/2.5/weather?"
key=os.environ['weatherApi']
city="Kolkata"
url=base_url+"appid="+key+"&q="+city
response=requests.get(url).json()
temp=response['main']['temp']
humid=response['main']['humidity']
describe=response['weather'][0]['description']
netWeather=f'Temperature is :{temp}'
print(netWeather)