
import os
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
from music import Player

client = discord.Client()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)




def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements 
    
sad_words = ["słabo","nie chce mi sie","zdenerwowany" ]

starter_encouragements = [
  "Jestem tu żeby poprawić Ci humor ;D",
  "Człowieki nie rozumieją :D",
  "Jesteś dobrym zawodnikiem, tylko zmień dyscyplinę, żeby nie ranić innych", "Czas na herbatkę :D"]

if "responding" not in db.keys():
  db['responding'] = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return

  msg = message.content
  

  if msg.startswith('?hej'):
    await message.channel.send('Witam wszystkich tu serdecznie wchodzę ja i robi się bezpiecznie :D')
  
  if db['responding']:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db['encouragements'])

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith('?nowa'):
    encouraging_message = msg.split("?nowa ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("Od teraz na zawsze w mojej głowie.")
  
  if msg.startswith("?usun"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("?usun",1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswitch("?lista"):
    encouragements = []
    if 'encouragements' in db.keys():
      encouragements = db['encouragements']
    await message.channel.send(encouragements)

  if msg.startswith("?responding"):
    value = msg.split("?responding",1)[1]

    if value.lower()== 'true':
      db['responding'] = True
      await message.channel.send("Odpowiedzi są aktywne")
    else:
      db['responding'] = False
      await message.channel.send("Odpowiedzi są nieaktywne")

async def setup():
  await bot.wait_until_ready()
  bot.add_cog(Player(bot))

keep_alive()
bot.loop.create_task(setup())
client.run(os.getenv('TOKEN'))

