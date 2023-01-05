#import requests
#req = requests.get("https://discord.com/api/path/to/the/endpoint")
#print(req.headers)
#for k,v in req.headers.items():
  #print(k, v)
#print(req.headers) # How many more requests you can make before `X-RateLimitReset`

import requests

r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")


from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
    return "Your Bot Is Ready"


def run():
    app.run(host="0.0.0.0", port=8000)


def keep_alive():
    server = Thread(target=run)
    server.start()


import json

import os
import discord
import asyncio
import re
import html

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

data = {}

with open('trivia2.txt') as json_file:
    data = json.load(json_file)

f = open('pokemon_list.txt', 'r')
pokes = []
for line in f:
    pokes += line.strip().split(',')

ping_msg = '<@599506091058921493> <@554379252728856626>'

legends = []
with open('legendaries.txt') as infile:
    legends = json.load(infile)

def get_matches(string):
    string = string[15:-1].replace('\\_', '.')
    pattern = re.compile(string)
    matches = []
    for poke in pokes:
        if pattern.fullmatch(poke):
            matches.append(poke)
    if len(matches) > 0:
        return matches
    else:
        return ['Nidoran']


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(guild.name, ' id:', guild.id)  #test


@client.event
async def on_message(message):
    if message.author == client.user:
        #await message.delete(delay=2)
        if message.channel.name == 'bot-spam':
            await message.delete(delay=2)
        return
    global spawned
    global matches
    global index
    global skip
    global ping_msg

    if str(message.author) == 'Pokétwo#8236':
        if message.content.startswith('The pokémon is '):
            matches = get_matches(message.content)

            await message.channel.send(', '.join(matches))
            possible = False
            for name in matches:
              for legend in legends:
                if legend in name:
                  possible = True
                  break
            if possible:
              await message.channel.send(ping_msg)
            
    elif str(message.author) == 'Dank Memer#5192':
        for embed in message.embeds:
            dic = embed.to_dict()
            if 'footer' in dic and dic['footer']['text'].startswith(
                    'Use the letter'):
                print('trivia')
                q = dic['description']
                #print(q)
                question = q[2:q[2:].find('**') + 2]
                #print(question)
                if question in data:
                    #print(True)
                    await message.channel.send(data[question])
                    await asyncio.sleep(15)
                    await message.channel.send('15')

            #print(dic)
        #await message.channel.send('testing')
        pass
    elif str(message.author) == 'spider#1556':
      if message.content == 'ping test':
        await message.channel.send(ping_msg)
      if message.content.startswith('The pokémon is '):
            matches = get_matches(message.content)

            await message.channel.send(', '.join(matches))
            possible = False
            for name in matches:
              for legend in legends:
                if legend in name:
                  possible = True
                  break
            if possible:
              await message.channel.send(ping_msg)
            

keep_alive()

try:
  client.run(TOKEN)
except Exception as e:
  print(e)