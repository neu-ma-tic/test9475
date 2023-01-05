import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('№СоздательБота'):
        await message.channel.send('Френда')

        @client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Привет всем'):
        await message.channel.send('Кар брат!')

client.run(os.getenv('854767575044063292'))