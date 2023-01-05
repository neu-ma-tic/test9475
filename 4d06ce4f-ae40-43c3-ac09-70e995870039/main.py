import os
import discord
import requests
import json
import random
from keep_alive import keep_alive
my_secret = os.environ['TOKEN']

TOKEN='ODY5MjE1MzMzOTM0ODQ1OTcy.YP693A.wvFF6OrJNnurPNwmKBFVKvyC0aI'

client = discord.Client()

sad_word = ["buồn", "bùn", "pùn", "sad", "sạd"]

starter_encouragements = [
  "vui lên cho DIO vui với",
  "vui lên lào",
  "kìa sao pùn :<, vui lên :)"
]
bad_word = ["bot cút đi", "bot đi đi", "f*ck bot", "fuck bot", "bot cút", "bot đi"]
say_back = [
  "Ơ kìa sao nói em như vậy ;-;",
  "hic hic tại sao :(",
  "bủh bủh dảk dảk"
]

def get_quote():
  respone = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(respone.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Kono {0.user} da'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$hello'):
    await message.channel.send('Hô ngươi gọi tên ta ư')
  if message.content.startswith('$amogus'):
    await message.channel.send('that kinda sus tho')
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote + ' P/s: chỉ cho người hiểu TA')
  if any(word in msg for word in sad_word):
    await message.channel.send(random.choice(starter_encouragements))
  if any(word in msg for word in bad_word):
    await message.channel.send(random.choice(say_back))

  await bot.process_command(message)
  keep_alive()

client.run(TOKEN)
