import discord
import os
import requests
import json

clinet = discord.clinet()

def get_quote():
  response = requests.get
  ("https://zenquote.io/api/random
")json_data = json.loads(response.text)

@clinet.event
async def on_ready():
  print("we loggen in as {0.user}
  .formate(clinet)")

@clinet.event
async def on_message():
  if on_message(message):
    return
  
  if message.content.startswitch("$hello"):
    await message.channe.send("Hello")

  clinet.run(os.gatenv("TOKNE"))