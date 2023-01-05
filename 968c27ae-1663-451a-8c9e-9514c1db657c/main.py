import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from discord.ext import commands
import music 

cogs = [music]

clients = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(clients)

client = discord.Client()


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
rude_words = ["fuck", "bitch", "stupid", "fucking", "damn"]
_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]


@client.command(aliases=['sup', 's'])
async def support(ctx):
    log = client.get_channel(id=701765882417774663)
    channels = ['bot-befehle']
    vc = client.get_channel(id=702412635127152686)

    if not vc.members:
        return

      player.play(discord.FFmpegPCMAudio('welcome.mp3'))
      player.source = discord.PCMVolumeTransformer(player.source)
      player.source.volume = 1.00
      await asyncio.sleep(30)
      player.stop()
      await player.disconnect()
      await log.send('Habe den Befehl "!support" erfolgreich ausgeführt.')
      print('Habe den Befehl "Support" erfolgreich ausgeführt.')

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()

  if msg.startswith('$hello'):
    await message.channel.send('Hello! :)')

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
     await message.channel.send(random.choice(_encouragements))

  if any(word in msg for word in rude_words):
    await message.delete()
    await message.channel.send("Be carefull about your language!")

keep_alive()
client.run(os.environ['password'])

