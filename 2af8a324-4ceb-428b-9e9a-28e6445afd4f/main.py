import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

rahul_words = ["Rahul", "rahul"]
felix_words = ["Felix", "felix"]
linus_words = ["Linus", "linus"]
finley_words = ["Finley", "finley"]
alex_words = ["Alex", "alex", "Alexander", "alexander"]
josef_words = ["Josef", "josef"]
simon_words = ["Simon", "simon"]
switch_words = ["Switch", "switch"]
latin_words = ["Latein", "latein"]
school_words = ["Schule", "schule"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]


game_word = "error g_w"
game_response_start = "error g_r_s"
game_response_end = "error g_r_e"
game_status = False
game_status_overall = False

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)



@client.event
async def on_ready():
  print("We have logged in as {0.user} ".format(client))

@client.event
async def on_message(message, game_status, game_status_overall):
  if message.author == client.user:
    return
    
  msg = message.content

  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if any(word in msg for word in rahul_words):
    await message.channel.send("Lalul stinkt!")

  if any(word in msg for word in felix_words):
    await message.channel.send("Feflix")
    
  if any(word in msg for word in linus_words):
    await message.channel.send("Sinus")

  if any(word in msg for word in finley_words):
    await message.channel.send("Schminley")

  if any(word in msg for word in alex_words):
    await message.channel.send("Alex ist mächtig!")

  if any(word in msg for word in josef_words):
    await message.channel.send("Sosef")

  if any(word in msg for word in simon_words):
    await message.channel.send("Sismon")

  if any(word in msg for word in switch_words):
    await message.channel.send("Du Snitch hast ne Switch.")

  if any(word in msg for word in latin_words):
    await message.channel.send("Latein sucks!")
  
  if any(word in msg for word in school_words):
    await message.channel.send("Schule sucks!")
  
  if msg.startswith("$help"):
    await message.channel.send("$inspire\nsad words\nnames\nlatein\nschule\nswitch\n$help\n$repeat\n$gameinfo")

  if msg.startswith("$repeat "):
    await message.channel.send(msg[7 : ])

  if msg.startswith("$rules"):
    await message.channel.send("SOON(ABER NICHT SO WIE BEI SPOMB)")

  if msg == "$gameinfo":
    await message.channel.send("Start Minigame---\nMinigame succesfully started\n$rules um die Regeln zu sehen\n$start um zu starten")
  
  if msg == "$start game":
    game_status_overall = True
    game_status = False
    await message.channel.send("Du hast einen Flugzeuhabsturz überlebt und bist auf einer einsamen Insel gestrandet.\nWas tust du zuerst?\n'essen' um essen zu suchen\n'schlafen' um nach einem Unterschlupf zu suchen\n'feuer' um Feuer zu machen")

  if msg == "essen":
    game("essen", "Glückwunsch, du hast einen Koffer voller Nahrung gefunden!", "Du hast deine letzten Energiereserven bei der vergeblichen Suche nach Nahrung aufgebraucht und schläfst am Strand für immer ein.", message, game_status, game_status_overall)
  elif msg == "schlafen":
    game("schlafen", "Glückwunsch, du hast dich ausgeschlagen, solltest aber bald mal etwas tun, du fauler Sack!", "Du schläfst so fest das du nicht merkst, wie ein Stratovulkan auf der Insel ausbricht und stirbst.", message, game_status, game_status_overall)
  elif msg == "feuer":
      game("feuer", "Glückwunsch, du hast Feuerholz gefunden und hast damit ein Feuer entfacht. Das hält dich warm und vertreibt etwaige Raubtiere.", "Glückwunsch, du hast Feuerholz gefunden und hast damit ein Feuer entfacht, allerdings verlierst du die Kontrolle darüber und es verbrennt dich bei lebendigen Leibe.", message, game_status, game_status_overall)
 


@client.event
async def game(game_word, game_response_start, game_response_end, message, game_status, game_status_overall):
  msg = message.content
  channel = message.channel.send
  if message.author == client.user:
    return
  if game_status_overall:
    if msg == game_word and random.choice([True, False]):
      await channel(game_response_start)
      game_status = True
    else:
      await channel(game_response_end)
      game_status = False
      game_status_overall = False



keep_alive()
client.run(os.getenv("TOKEN"))