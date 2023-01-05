# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # colors = [
    #     'blue',
    #     'red',
    #     'yellow',
    #     'orange',
    #     'green'
    # ]

    # if message.content == "!pick-a-color":
    #     # pick a random color
    #     response = random.choice(colors)
    #     await message.channel.send(response)

    # memes = [
    #     ""
    # ]

    # user = message.guild.cache.get('bread');
    # print(dir(user))
    # print(user.id)
    print(message.guild.members)
    print(dir(message.guild.members))
    user = message.guild.fetch_member('bread')
    print(dir(user))

    # if message.content == "!spam":
    #     for i in range(10):
    #         response = "@Bread"
    #         await message.channel.send(response)

client.run(TOKEN)