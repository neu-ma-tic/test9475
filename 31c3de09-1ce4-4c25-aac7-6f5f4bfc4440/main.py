import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in ")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!Hello"):
    member_list = ''
    for member in ctx.message.server.members:
      member_list += member.name
    
    print(member_list)
		    
client.run(os.getenv("Token"))