import discord
import os
from replit import db
matches = db.prefix("prefix")
keys = db.keys()
del db["key"]
value = db["key"]
db["key"] = "value"
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))