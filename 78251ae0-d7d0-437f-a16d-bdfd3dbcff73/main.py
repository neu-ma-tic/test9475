import discord
import os
import requests
import json
import random
from replit import db
from KeepAlive import keepAlive
import urllib.request

client = discord.Client()
sadWords = ["Sad","Unhappy","Depressed","sad","unhappy","depressed","feeling down","feel down","feel horrible","feeling horrible","feel awful","feeling awful"]

morningGreeting = ["Morning","Good morning","gmorning","good morning"]
toU2 = "to you too!"

morninggreetingResponse = ["Morning "+toU2,"Good morning "+toU2,"gmorning "+toU2,"good morning "+toU2]

starterEncouragements = [
  "Hang in there!",
  "Cheer up!",
  "You are a great person!",
  "You are so talented!",
  "You deserve to be happy!",
  "You can take on any challenge!",
  "You are stronger than you think!",
  "Nothing can bring you down!"
]

auth = "\n - Mr. Inspire"
myQuotes = [
  "Death is inevitable"+auth,
  "There is no such thing as bad experience"+auth,
  "Learn from your experience, instead of regretting it"+auth,
  "Strive for more, but don't forget to be grateful for what you have"+auth
]

### Random quote generator ###

#def getQuote():
 # response = requests.get("https://zenquotes.io/api/random")
  #jsonData = json.loads(response.text)
  #quote = jsonData[0]["q"] + " -" +jsonData[0]["a"]
  #return(quote)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if (msg == "$inspire"):
    await message.channel.send(random.choice(myQuotes))

### Work in progress --- Earthquake generator ###
  if msg == '$quakes.today':
    dataURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

    webURL = urllib.request.urlopen(dataURL)
    print("Result code: "+ str(webURL.getcode()))

    
    data = webURL.read()
    jsonData = json.loads(data)
      
    

    if "title" in jsonData["metadata"]:
      count = jsonData["metadata"]["count"]
      await message.channel.send(jsonData["metadata"]["title"]+"\n"+str(count)+" events recorded")

  
  if msg == '$quakes.today.place':
    dataURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

    webURL = urllib.request.urlopen(dataURL)
    print("Result code: "+ str(webURL.getcode()))

    
    data = webURL.read()
    jsonData = json.loads(data)

    if "title" in jsonData["metadata"]:
      count = jsonData["metadata"]["count"]
      for i in jsonData["features"]: 
        result = i["properties"]["place"]   
        await message.channel.send(str(result))
        
        




## Dog generator ##
  if (msg == "$dog"): 
    dataURL = "https://dog.ceo/api/breeds/image/random"

    webURL = urllib.request.urlopen(dataURL)
    print("Result code: "+ str(webURL.getcode()))

    if webURL.getcode() == 200:

      data = webURL.read()
      jsonData = json.loads(data)
      dog = jsonData["message"]
      await message.channel.send(dog)
    
    else:
        print("Unexpected error")  
    

  if any(word in msg for word in sadWords):
    await message.channel.send(random.choice(starterEncouragements))

  if any(word in msg for word in morningGreeting):
    await message.channel.send(random.choice(morninggreetingResponse))

keepAlive()
client.run(os.getenv("TOKEN"))

