import os

TOKEN = os.getenv('TOKEN')

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
GUILD = os.getenv('DISCORD-GUILD-NAME')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
'''
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hallo {member.name}, Willkommen es wer Discord-server, Plebejer!'
    )
'''
client.run(TOKEN)