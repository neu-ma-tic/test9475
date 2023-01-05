import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands

db["roasts"] = ["you are trash at every game you play", "you smell", "You must of been born on a highway’ cause that’s where most accidents happen.", "Don’t be ashamed of who you are. That’s your parents’ job.", 'I thought of you today. It reminded me to take out the trash.', 'Is your ass jealous of the amount of shit that comes out of your mouth?', 'When you look in the mirror, say hi to the clown you see in there for me, would ya?', "You’re kinda like Rapunzel except of letting your hair down you let everyone down in your life.", 'You look like a gta civilian', 'You look like a sentient STD', 'You look like you got rejected from a pride parade.', 'We, the LGBTQ community, welcome everybody to join us.... Except you, Nooooo thanks', 'You look like someone hit random on the character generator.', 'You look like watery ketchup if it was a person', 'Take my lowest priority and put yourself beneath it.', 'Hell we just roasted your sister yesterday, tell your parents to knock it off!', 'Light travels faster than sound, which is why you seemed bright until you spoke', 'You have so many gaps in your teeth it looks like your tongue is in jail', "If you're going to be a smart ass, first you have to be smart, otherwise you're just an ass", "I’ll never forget the first time we met. But I’ll keep trying", "You should put a condom on your head, because if you're going to act like a dick you better dress like one too", "Carlos' teeth are so bad he could eat an apple through a fence", "There are two ugly people in this chat, and you're both of them", "You are the human version of period cramps", "The last time I saw something like you… I flushed", "I was going to make a joke about your life, but I see life beat me to the punch", "I treasure the time I don’t spend with you","Life is full of disappointments, ig life added you to the list", "Your birth certificate is an apology letter from the condom factory", "You’re the reason this country has to put directions on shampoo", "You're like a slinkie — not really good for much, but they bring a smile to your face when pushed down the stairs"]
value = db["roasts"]

db["commands"] = ['$hello', '$roast me', '$commands']
coms = db["commands"]

my_secret = os.environ['bottoken']

client = discord.Client()

def jokes(f):
    
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt

f = r"https://official-joke-api.appspot.com/random_joke"
a = f

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("$commands"))
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):

  msg = message.content
  

  if message.author == client.user:
    return
  
  if message.content.startswith("$hello"):
    await message.channel.send("Hello Cutie!")
  
  if message.content.startswith("$joke"):
    await message.channel.send(a)
  
  if message.content.startswith("kys"):
    await message.channel.send("No u pussy")
  if message.content.startswith("Kys"):
    await message.channel.send("No u pussy")
  if msg.startswith("KYS"):
    await message.channel.send("No u pussy")

  if message.content.startswith("is carlos fat?"):
    await message.channel.send("Yes Very fat indeed!")

  if message.content.startswith("$roast me"):
    await message.channel.send(random.choice(value))

  if message.content.startswith("$commands"):
    await message.channel.send(coms)

  if message.author.id == 311649605655724033:
    await message.channel.send("Shut up Izzy and Bre don't like you!")


keep_alive()
client.run(os.getenv('bottoken'))
