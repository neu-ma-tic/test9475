import os
import requests
import json
import discord as ds

user= ds.Client()
botToken= os.environ['Token']
key=os.environ['weatherApi']
base_url="https://api.openweathermap.org/data/2.5/weather?"

def locationWeather(location):
  city="Kolkata"
  url=base_url+"appid="+key+"&q="+city
  response=requests.get(url).json()
  temp=response['main']['temp']
  humid=response['main']['humidity']
  describe=response['weather'][0]['description']
  netWeather=f'Temperature is :{temp} \nHumidity : {humid} \nDesciption: {describe}'
  return netWeather

async def on_ready():
  print('Logged in as {0.user}'.format(user))

@user.event
async def on_message(message):
  if message.author==user.user:
    return

  if message.content.startswith("$weather"):
    response=locationWeather('kolkata')
    await message.channel.send(response)

user.run(botToken)