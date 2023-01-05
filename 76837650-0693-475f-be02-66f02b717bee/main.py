import discord
import os
import requests
import json
import random
from replit import db
from bs4 import BeautifulSoup
from keep_alive import keep_alive

agent_list = ["Brimstone","Viper","Astra","Omen","Raze","Killjoy","Cypher","Sova","Sage","Jett","Pheonix","Reyna","Breach","Brimstone","Skye","Yoru","KAY/O"]


client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

URL = "https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

name_categories = soup.select("span .trn-ign__username")

top_5 = []

for index, name in enumerate (name_categories):
  top_5.append({
  "rank": index + 1,
  "name": name.getText()
})
N = 5
new_top_5 = top_5[:N]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def roll_random(roll):
  num_list = random.sample(range(17), roll)
  return num_list

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

def delete_encouragment(index):
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
       options += db["encouragements"]

    if any(word in msg.lower() for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
  
  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$top5"):
    for user_info in new_top_5:
      await message.channel.send("Rank: " + str(user_info["rank"]))
      await message.channel.send(str(user_info["name"]))
      await message.channel.send("-------------------------------")

  if msg.startswith("$roll"):
    value = int(msg.split("$roll",1)[1])
    num_list = roll_random(value)
    for index in num_list:
      await message.channel.send(agent_list[index])

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()
client.run(os.getenv('TOKEN'))