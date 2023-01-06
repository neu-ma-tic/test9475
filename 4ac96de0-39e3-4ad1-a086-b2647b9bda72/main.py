import discord
import random
import regex

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(discord.__version__)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('$hello'):
        await message.channel.send('Hello!')
        guild = message.guild
    elif message.content.lower().startswith('pizza'):
        await message.channel.send("🍕 My favourite thing with pizza is CHIPS.")
    elif message.content.lower().startswith('give me role'):
        role = discord.utils.get(message.guild.roles, name="Testing role")
        user = message.author
        await user.add_roles(role)

client.run('NjUyMTM2NTI3OTc1MDIyNjEy.XekEJw.O08s5BVFGPEiw9V-3qipnvA7LY0')