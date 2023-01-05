import discord
import os
import requests

import random
import json
import time





client = discord.Client()


@client.event
async def on_ready():
    print("We have logging in as {0.user}".format(client))


def rollDice(guess):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    newdie = die1 + die2
    if newdie == guess:
        return ("You guessed correctly!")
    else:
        newdie = str(newdie)
        return ("You didn't guess it :( The number was " + newdie)


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith("!erin"):
        await msg.channel.send("What's up!")

    if msg.content.startswith("!EErollDice"):
        length = len("!EErollDice")
        guess = msg.content[length:]
        guess = int(guess)
        roll = rollDice(guess)
        await msg.channel.send(roll)

    

    if msg.content.startswith("!EEMadLibs"):
  
      await msg.channel.send("Let's start the Madlib!")
      await msg.channel.send("Type in an adjective following adj:  'adj:blue'")
    if msg.content.startswith("adj:"):
      length = len("adj:")
      global adj
      adj = msg.content[length:]
      await msg.channel.send("Type in a noun following noun:  'noun:dog'")
    elif msg.content.startswith("noun:"):
      length=len("noun:")
      global noun
      noun= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj2:  'adj2:blue'")
    elif msg.content.startswith("adj2:"):
      length=len("adj2:")
      global adj2
      adj2= msg.content[length:]
      await msg.channel.send("Type in a place following place:  'place:Europe'")
    elif msg.content.startswith("place:"):
      length=len("place:")
      global place
      place= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj3:  'adj3:blue'")
    elif msg.content.startswith("adj3:"):
      length=len("adj3:")
      global adj3
      adj3= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj4:  'adj4:blue'")
    elif msg.content.startswith("adj4:"):
      length=len("adj4:")
      global adj4
      adj4= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj5:  'adj5:blue'")
    elif msg.content.startswith("adj5:"):
      length=len("adj5:")
      global adj5
      adj5= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj6:  'adj6:blue'")
    elif msg.content.startswith("adj6:"):
      length=len("adj6:")
      global adj6
      adj6= msg.content[length:]
      await msg.channel.send("Type in a plural nound following plunoun:  'plunoun:bees'")
    elif msg.content.startswith("plunoun:"):
      length=len("plunoun:")
      global plunoun
      plunoun= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj7:  'adj7:blue'")
    elif msg.content.startswith("adj7:"):
      length=len("adj7:")
      global adj7
      adj7= msg.content[length:]
      await msg.channel.send("Type in a plural noun following plunoun2:  'plunoun2:bees'")
    elif msg.content.startswith("plunoun2:"):
      length=len("plunoun2:")
      global plunoun2
      plunoun2= msg.content[length:]
      await msg.channel.send("Type in a plural noun following plunoun3:  'plunoun3:bees'")
    elif msg.content.startswith("plunoun3:"):
      length=len("plunoun3:")
      global plunoun3
      plunoun3= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj8:  'adj8:blue'")
    elif msg.content.startswith("adj8:"):
      length=len("adj8:")
      global adj8
      adj8= msg.content[length:]
      await msg.channel.send("Type in a noun following noun2:  'noun2:dog'")
    elif msg.content.startswith("noun2:"):
      length=len("noun2:")
      global noun2
      noun2= msg.content[length:]
      await msg.channel.send("Type in a verb following verb:  'verb:sing'")
    elif msg.content.startswith("verb:"):
      length=len("verb:")
      global verb
      verb= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj9:  'adj9:blue'")
    elif msg.content.startswith("adj9:"):
      length=len("adj9:")
      global adj9
      adj9= msg.content[length:]
      await msg.channel.send("Type in a verb following verb2:  'verb2:sing'")
    elif msg.content.startswith("verb2:"):
      length=len("verb2:")
      global verb2
      verb2= msg.content[length:]
      await msg.channel.send("Type in a plural noun following plunoun4:  'plunoun4:bees'")
    elif msg.content.startswith("plunoun4:"):
      length=len("plunoun4:")
      global plunoun4
      plunoun4= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj10:  'adj10:blue'")
    elif msg.content.startswith("adj10:"):
      length=len("adj10:")
      global adj10
      adj10= msg.content[length:]
      await msg.channel.send("Type in a verb following verb3:  'verb3:sing'")
    elif msg.content.startswith("verb3:"):
      length=len("verb3:")
      global verb3
      verb3= msg.content[length:]
      await msg.channel.send("Type in an adjective following adj11:  'adj11:blue'")
    elif msg.content.startswith("adj11:"):
      length=len("adj11:")
      global adj11
      adj11= msg.content[length:]
      await msg.channel.send("Calculating madlib...")
    else:
      return


    await msg.channel.send("Star Wars is a " + adj +  "," + noun + " of " + adj2 + " versus evil in a "+ place +" far far away. There are " + adj3 + " battles between " + adj4 + " ships in " + adj5 + " space and " + adj6 +  " duels with " + plunoun + " called "  + adj7 + " sabers. " + plunoun2 +  " called 'droids' are helpers and " +  plunoun3 +  " to the heroes. A "  + adj8 + " power called The "+ noun2 +  " " + verb + "s people to do " + adj9 +  " things, like " + verb2 +  " "+ plunoun4 +  " use The Force for the " + adj10 +  " side and the Sith " + verb3 +  " it for the "+ adj11 +  " side.")



client.run(os.getenv('TOKEN'))
