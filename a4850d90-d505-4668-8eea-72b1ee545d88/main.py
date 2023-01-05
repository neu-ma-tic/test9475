import discord
import os
from dotenv import load_dotenv

load_dotenv("./token.env")
TOKEN = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: #if the person who sent the message is this bot do nothing
        return

    if message.content.startswith('$test'):
        await message.channel.send('Hello World!')

client.run(TOKEN)
