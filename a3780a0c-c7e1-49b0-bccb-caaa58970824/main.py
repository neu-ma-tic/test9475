import discord
import random
import os
import keep_alive

from random import choice

client = discord.Client()

response_list = ["No shut up", "Shut", "Stop just stop", "Why ?", "Get some braincells", "No more bot", "Dumbass", "Idiot", "STUPID CUNT", "FUCK OFF", "LOSER", "SHUT THE FUCK UP", "Fool", "Moron", "Imbecile", "Stupid"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        

@client.event
async def on_message(message):
    if message.content.startswith("/random"):
        user = choice(message.channel.guild.members)
        await message.channel.send(user.mention)

keep_alive.keep_alive()

client.run('OTUxMTM1NDczOTMyMzE2NzQy.YijD8A.CAQBUzwV-7RgxLuCB4FDSp2uPX8')