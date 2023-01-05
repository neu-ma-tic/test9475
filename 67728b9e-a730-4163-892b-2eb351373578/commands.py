import discord
import requests
import random
import json

ballingURLs = [
  "https://media1.tenor.com/images/50f9a6b893f03a2a2bfd3a0c5608c9ef/tenor.gif",
  "https://c.tenor.com/i87v9qZXMm8AAAAd/squid-game-balling.gif",
  "https://c.tenor.com/M7GcRI9jgG8AAAAC/stupid-dog-im-ballin.gif"
]

async def giveHelp(message):
  s = "List of commands: \n \n"
  for command, info in commandList.items():
    s += command + " : " + info["Description"] + "\n"

  await message.channel.send(s)

async def inspire(message):
  response = requests.get("https://inspirobot.me//api?generate=true")

  if response.status_code == 200 and response.text != "":
    embed = discord.Embed()
    embed.set_image(url=response.text)

    await message.channel.send("I got u fam")
    await message.channel.send(embed=embed)
  else:
    await message.channel.send(f"Could not recieve a response, status code: {response.status_code}")
  
async def ballin(message):
    embed = discord.Embed()

    randURL = random.choice(ballingURLs)
    embed.set_image(url=randURL)

    await message.channel.send("Did someone say ballin!?")
    await message.channel.send(embed=embed)

async def meme(message):
  response = requests.get("https://api.imgflip.com/get_memes")

  if response.status_code == 200:
    memeList = json.loads(response.text)
    if memeList["success"]:
      meme = random.choice(memeList["data"]["memes"])
      embed = discord.Embed()
      embed.set_image(url=meme["url"])
      await message.channel.send(embed=embed)
      return
  
  await message.channel.send("The server was stoopid and did not manage to send a meme.")

commandList = {
  "!help" : {
    "Func" : giveHelp,
    "Description" : "Returns a list of all possible commands along with a description."
  },
  "!inspire" : {
    "Func" : inspire,
    "Description" : "Returns an image of a inspirational quote from 'inspirobot.me'."
  },
  "!ballin" : {
    "Func" : ballin,
    "Description" : "Makes you a baller."
  },
  "!meme" : {
    "Func" : meme,
    "Description" : "Sends a random meme template (will get updated to send actual meme)."
  }
}