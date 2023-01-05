import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Credo che {0.user} sia fatto'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Cazzo'):
        await message.channel.send('Piselo')

#@client.event
#async def on_channel(channel):

client.run(os.getenv('TOKEN'))