"""
Notes on what to add to bot help pastebin
-!novowel

Things to add:
-Gif sender
-Conspiracy headline generator
"""

#### All imported libraries ###
import discord
import os
import requests
import json
import time
import random #for the random choice module
from replit import db
from keep_alive import keep_alive

###GIPHY TOKEN###
giphy_token = os.getenv('GIPHY_TOKEN')
#print(giphy_token) #to verify token has been grabbed.

### Target Client ###
client = discord.Client()

### Sad Words List ###
sad_words = ["sad", "depressed", "unhappy", "lame", "useless", "miserable", "depressing", "mad"] #list the bot checks for sad words

### Initial list of encouragements ###
starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You are a great person / bot!"
]


if "responding" not in db.keys():
  db["responding"] = True




def get_inspire(): #function to return quote from API
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  inspire = json_data[0]['q'] 
  return(inspire)

def get_roast(): #function to return roast from API
  response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
  print(response.json())
  json_data = json.loads(response.text)
  roast = json_data['insult']
  return(roast)

def get_advice():
  response = requests.get("https://api.adviceslip.com/advice")
  json_data = json.loads(response.text)
  advice = json_data['slip']['advice']
  return(advice)

''' def get_fortnite():
  response = requests.get(f'https://api.fortnitetracker.com/v1/profile/kbm/{epic_nickname}', auth=(gwolf204, '3a289324-074b-4922-a24e-a66b44c8887f'))
  json_data = json.loads(response.text)
  fort_stats = json_data
  return(fort_stats) '''

def get_price():
  response = requests.get('https://api.pancakeswap.info/api/v2/tokens/0xdfaabaa57dec10c049335bdaa2e949b4ce2ead30')
  data = json.loads(response.text)
  price = f"${data['data']['price']}"
  return(price)
  

def update_encouragements(encouraging_message): #function to update encouragements
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


@client.event   #waits for event of login, provides notice of login, sends a notice to channel
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

@client.event #triggers each time a message is received
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content.lower()

  if message.content.startswith('Harold'):
    harold_gifs = ["https://i.imgur.com/M8I1l3h.mp4", "https://i.imgur.com/PHhy8YO.gif", "https://i.imgur.com/Ktlbg51.mp4", "https://i.imgur.com/NTFoe0E.mp4", "https://media3.giphy.com/media/d5Fbhttps://i.giphy.com/media/d5Fbtoj47ROk0J9IgW/giphy.webp", "https://i.giphy.com/media/Ssm6ltHQ9gykRFAUXf/giphy.webp", "https://i.giphy.com/media/1Be3tj1xRclcFTBbZC/giphy.webp"]
    harold_greetings = ["Hello...", "Yes?", "WHAT!?", "I wasn't doing anything...", "Got good memes?", "I just made a Tinder", "I'm real if you're real", "MUGGLES?", "xxx360xxxNOSCOPExxx"]
    await message.channel.send(f"{random.choice(harold_greetings)} {random.choice(harold_gifs)}")

  if msg.startswith('!help'): #provides the user documentation about the bot from pastebin
    await message.channel.send("Want to read about what I can do?\n ☞ó ͜つò☞ https://pastebin.com/Q0BJmgAh")

  if msg.startswith('!inspire'):
    inspire = get_inspire()   #Checks for message !inspire
    await message.channel.send(inspire)   #replies with inspirational message

  if msg.startswith('!roastme'):
    roast = get_roast()   #Checks for message !roast
    await message.channel.send(roast)   #replies with the roast

  if msg.startswith('!advice'):
    advice = get_advice()   #Checks for message !advice
    await message.channel.send(advice)   #replies with the roast

  if msg.startswith('!price'):
    price = get_price()
    await message.channel.send(price)

  ''' if msg.startswith('!fort'):
    epic_nickname = str(msg.split("!fort ", 1)[1])
    response = requests.get(f'https://api.fortnitetracker.com/v1/profile/kbm/{epic_nickname}', auth=('3a289324-074b-4922-a24e-a66b44c8887f'))
    json_data = json.loads(response.text)
    fort_stats = json_data
    return(fort_stats)
    await message.channel.send(fort_stats)   '''  #Fortnite stat tracker, not working

  ###Encouraging messages functionality section###
  
  if db["responding"]:
    options = starter_encouragements #initializes options as the starter_encouragements json_data
    if "encouragements" in db.keys(): 
      options = options + db["encouragements"]


    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith('!newencouragement'): #grabs new encouraging message submitted by users and adds to database.
    encouraging_message = msg.split("!newencouragement ", 1)[1] 
    update_encouragements(encouraging_message)
    await message.channel.send("Your encouragement has been added to the database!")

  if msg.startswith('!delencouragement'): #deletes an encouragement from the database using the integer for the space in the DB.
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("!delencouragement",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)  

  if msg.startswith("!encouragedlist"): #looks for message and returns the list of encouragements 
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
  
  if msg.startswith("!encouraging"): #when it sees !encouraging this turns on or off sending encouraging messages, use true to turn on, any message to turn off
    value = msg.split("!encouraging ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("I am ready to encourage you!")
    else:
      db["responding"] = False
      await message.channel.send("I am taking a break from encouraging you.")
  

  if msg.startswith("fuck you"): #looks for message and returns the list of encouragements 
    await message.channel.send("凸( •̀_•́ )凸")

  if msg.startswith("!novowels"):  #looks for message and returns the list of encouragements 
    start_message = message.content
    #start_message = msg.startswith("!novowel")
    new_message = start_message[6::]
    print(new_message[6:])
    new_message = ''.join(char for char in start_message if char not in "aeiou")
    updated_message = new_message[6:]
    await message.channel.send(updated_message)

  
    



keep_alive() #calls the keep alive function to keep the webserver running
client.run(os.getenv('TOKEN')) #Super hidden token.


