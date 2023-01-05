import discord
import os
import random 
import requests
from keep_alive import keep_alive


query = "boobs"

r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 200,
        'q': query,
        't': 'images',
        'safesearch': 0,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
)

response = r.json().get('data').get('result').get('items')
urls = [r.get('media') for r in response]




h = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 200,
        'q': 'hentai picture',
        't': 'images',
        'safesearch': 0,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
)

hresponse = h.json().get('data').get('result').get('items')
hurls = [h.get('media') for h in hresponse]


# instantiate the discord client
client = discord.Client()

# start events

@client.event
async def on_ready():
    print("We have logged on as {0.user}".format(client))


#message events
@client.event
async def on_message(message):
    if message.author == client:
        return 

    msg = message.content

    #function to send string
    if msg == "--yahoo":
        test_message = 'This is a success'
        link = random.choice(urls)
        await message.channel.send(link)
    
    if msg == '--anime bitches':
        link = random.choice(hurls)
        await message.channel.send(link)


#keep the bot alive
keep_alive()

# run the bot
client.run(os.getenv("TOKEN"))