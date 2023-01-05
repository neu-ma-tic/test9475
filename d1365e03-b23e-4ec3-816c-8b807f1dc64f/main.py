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

    if message.content.startswith('$letsplay'):
        await message.channel.send('Player 1, choose your fighter: ')
    if message.content.startswith('$lamp'):
        await message.channel.send('Player 2, choose your fighter: ')
    if message.content.startswith ('$fanfic'):
        await message.channel.send ('Player 2 wins')


client.run(os.getenv('TOKEN'))

