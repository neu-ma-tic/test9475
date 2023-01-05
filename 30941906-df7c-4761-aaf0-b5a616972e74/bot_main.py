import asyncio
import os

import discord
from keep_alive import keep_alive
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")
ID_MARIUSZA = os.getenv("ID_MARIUSZA")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
channel_leszke = discord.utils.get(client.get_all_channels(), name="Leszke")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.invisible, activity=None)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to guild {guild.name}, {guild.id}')

    members = '\n - '.join([str(member.id) for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.content.startswith("!members"):
        for guild in client.guilds:
            if guild.name == GUILD:
                for member in guild.members:
                    print(member.name, member.id)


@client.event
async def on_voice_state_update(member, before, after):
    if member.id == id_mariusza:
        if after.channel:
            await member.move_to(channel_leszke)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Siema {member.name}, witaj na Analnym Kanale, gdzie czeka na Ciebie mnóstwo spierdolenia i analnej rozkoszy.'
            )

keep_alive()
client.run(TOKEN)
