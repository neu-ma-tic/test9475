# DiscordBot.py
import os
import discord
intents = discord.Intents.all()
client = discord.Client(intents=intents)


TOKEN = os.environ['TOKEN']
SERVER = os.environ['SERVER']

#client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Server Members:\n - {members}')

client.run(TOKEN)