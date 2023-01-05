import os
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'miserable', 'despressing']

starter_encouragements = [
    'Cheer Up',
    'Hand in there.', 
    'You are amazing!'
    ]

if 'responding' not in db.keys():
    db['responding'] = True


def get_quote() -> str:
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote =  f"{json_data[0]['q']} - {json_data[0]['a']}"
    return quote


def update_encouragements(message: str):
    if 'encouragements' in db.keys():
        encouragements = db['encouragements']
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [message]


def delete_encouragements(index: int):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
        db['encouragements'] = encouragements
    

@client.event
async def on_ready():
    print(f'We have logged in as - {client.user}')


@client.event
async def on_message(message: str):
    msg = message.content

    if db['responding']:
        options = starter_encouragements

        if 'encouragements' in db.keys():
            options.extend(db["encouragements"])
        
        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if message.author == client.user:
        return

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('$status'):
        await message.channel.send('Active!')

    if msg.startswith('$new'):
        encouraging_message = msg.split('$new ', 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send('New Encouraging message added !')

    if msg.startswith('$del'):
        encouragements = []
        if 'encouragements' in db.keys():
            index = int(msg.split('$del', 1)[1])
            delete_encouragements(index)
            encouragements = db['encouragements']
        
        await message.channel.send(encouragements)

    if msg.startswith('$list'):
        encouragements = []
        if 'encouragements' in db.keys():
            encouragements = db['encouragements']
        await message.channel.send(encouragements)

    if msg.startswith('$responding'):
        value = msg.split('$responding ', 1)[1]

        if value.lower() == 'true':
            db['responding'] = True
            await message.channel.send('Responding is ON.')
        else:
            db['responding'] = False
            await message.channel.send('Responding is OFF.')

keep_alive()
client.run(my_secret)
