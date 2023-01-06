import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

sad_words = ["achjo", "bože", "kurva", "doprdele", "do prdele", "do háje", "fuj", "neee"]

starter_encouragements = ["To bude zase dobrý!", "To chce klid a nohy v teple!", "To zvládneš!", "Usměj se!", "Hlavu vzhůru!"]

nesnasim = ["nesnáším", "Nesnáším"]
nesnasim_odpoved = ["Taky to nesnáším, ale nedá se nic dělat.", "Fuj, tak to já taky ne."]

smrdim = ["smrdím", "Smrdím", "smrdim", "Smrdim", "smrdíš", "Smrdíš", "smrdí", "Smrdí", "smrdi", "Smrdi","smrdíme", "Smrdíme", "smrdíte", "Smrdíte"]

odpoved_na_smrdim = ["Já vím.", "No a co?", "Tak to není nic nového, ne?", "Však ty taky.", "Zato ty voníš jak květinka."]

introduction = "Ahoj, jmenuji se Bořek a jsem váš bot. Co umím: pokud zadáte: $inspire, zobrazím vám náhodný citát. Když budete smutní, povzbudím vás. Někdy ale dokážu být pěkná svině :* ."

pozdravy = ["ahoj", "Ahoj", "ahojky", "Ahojky", "Čau", "Čauky", "čau", "čauky", "Nazdar", "nazdar", "Nazdárek", "nazdárek", "Čus", "čus", "Čusík", "čusík", "čauvec", "Čauvec", "čauves", "Čauves", "Dobrý den", "dobrý den", "Zadravím", "zdravím", "Zdravíčko", "zdravíčko", "ahojdá", "Ahojdá", "ahojda", "Ahojda"]

odpoved_na_pozdrav = ["Zdravím tě!", "Čau kotě!", "Nazdar brouku!", "Ahoj puso!", "Čus puso!", "Nádarek"]

jak_se_mas = ["Jak se máš", "jak se máš", "Jak se mas", "jak se mas", "Jak je", "jak je", "Jak to jde", "jak to jde", "Jak se daří", "jak se daří", "jak se dari", "Jak se dari", "Jak to jde", "jak to jde"]

jak_se_mas_odpovedi = ["Ani se neptej...", "Stojí to za hovno, co ty?", "Peckově!", "No úžasně.."]

if "responding" not in db.keys():
  db["responding"] = True


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
   encouragements = db["encouragements"]
   if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))

    if any(word in msg for word in nesnasim):
      await message.channel.send(random.choice(nesnasim_odpoved))
  
    if any(word in msg for word in smrdim):
      await message.channel.send(random.choice(odpoved_na_smrdim))

    if any(word in msg for word in pozdravy):
      await message.channel.send(random.choice(odpoved_na_pozdrav))

    if any(word in msg for word in jak_se_mas):
      await message.channel.send(random.choice(jak_se_mas_odpovedi))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")
  
  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

  if msg.startswith("$intro"):
    await message.channel.send(introduction)

keep_alive()
client.run(os.getenv('TOKEN'))