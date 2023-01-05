import discord
import os
import requests
import json
import random
import time
from replit import db


client = discord.Client()

db = {
  "guessingnumber":{
    "guessing":False, 
    "tries":0, 
    "start":0, 
    "end":100, 
    "target":85
  }, 
  "wished":False
}

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

# Returns (Valid parameters, Correct number) 
def check_guessingnumber(num, target_num, start = 0, end = 100):
    try:
        num = int(num)
        if num < start or num > end or end <= start:
            raise ValueError
    except ValueError:
        return False, "="

    if target_num == num:
        return True, "="
    else:
        if target_num > num:
            return True, ">"
        else:
            return True, "<"

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  msg = message.content
  db_guess = db["guessingnumber"]

  # Random inspiring quote
  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  # Number guessing game
  if msg.startswith("%guess"):
    # Initialise
    if not db_guess["guessing"]:
      db_guess["guessing"] = True
      db_guess["tries"] = 0
      db_guess["start"] = 0
      db_guess["end"] = 100
      start = db_guess["start"]
      end = db_guess["end"]
      db_guess["target"] = random.randint(start, end)
      await message.channel.send("Guess a number from {} to {}!".format(start, end))
  # Check if guess is right
  if db_guess["guessing"]:
    target = db_guess["target"]
    tries = db_guess["tries"]
    checked_num = check_guessingnumber(msg, target, db_guess["start"], db_guess["end"])
    valid = checked_num[0]
    compare = checked_num[1]

    if valid:
      tries += 1
      if compare == "=":
        if tries <= 10:
          await message.channel.send("You are correct! You took {} tries.".format(tries))
        if tries > 10:
          await message.channel.send("You are correct.. but you took even {} tries.".format(tries))
        tries = 0
        db_guess["guessing"] = False
      elif compare == ">":
        await message.channel.send("Try {}. The number is greater than {}".format(tries, msg))
      elif compare == "<":
        await message.channel.send("Try {}. The number is less than {}".format(tries, msg))
    
    db_guess["tries"] = tries

  # Wish SH a happy birthday
  if message.author.id == 621713332675543052 or msg.startswith("hokey"):
    if db["wished"] == False:
      db["wished"] = True
      wait = 3
      await message.channel.send("Happy birthday to you...")
      time.sleep(wait)
      await message.channel.send("Happy birthday to you.......")
      time.sleep(wait)
      await message.channel.send("Happy birthday Swan Htet....")
      time.sleep(wait)
      await message.channel.send("Happy birthdayyy........")
      time.sleep(wait - 1)
      await message.channel.send("TO YOUUU")
      time.sleep(wait)
      await message.channel.send("Thanks for being my friend :)")
      time.sleep(wait)
      deleted = await message.channel.send("Sorry for being cheesy xd")
      time.sleep(2)
      await deleted.delete()
  
  
  if msg.startswith("$sfgfsg"):
    await message.channel.send("You have exchanged 10 eggs for 1 golden egg. You now have 5 normal eggs remaining")


    


  
    


client.run(os.getenv("TOKEN"))