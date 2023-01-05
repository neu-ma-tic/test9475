import discord
import json

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

@client.event
async def on_raw_reaction_add(message, payload):\
  if message.id == payload.message_id:
    guild_id= payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

    
    role = discord.utils.get(guild.role, name="Blue Team")


client.run('NTc0NjkyODg2MzM2MTEwNjgw.XM9GdQ.JJti54-3rMV0MKaOMWsM0dBrqb8')

