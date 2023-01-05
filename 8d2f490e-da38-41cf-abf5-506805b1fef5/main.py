import os
import discord

client = discord.Client() 

@client.event
async def on_ready():
  print(f"{client.user} logged in now!")
  
@client.event
async def on_message(message):
 if message.content.startswith("Oliver"):
   await message.channel.send(f"Fatti un abbonamento {message.author}")
  
  

my_secret = os.environ['Token']
client.run(my_secret)