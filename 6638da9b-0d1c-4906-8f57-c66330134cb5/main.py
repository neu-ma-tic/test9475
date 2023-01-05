import discord
import os
from dotenv import load_dotenv
from random import randint

#https://discordpy.readthedocs.io/en/latest/index.html
#https://cog-creators.github.io/discord-embed-sandbox/
#https://realpython.com/how-to-make-a-discord-bot-python/

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

client = discord.Client()

commandSymbol = "!"

emojis = ["😋", "💁", "👌" , "🎍" , "😍"]

#embed stuff here

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith(f"{commandSymbol}hello"):
    await message.channel.send("Hello!")
  elif message.content.startswith(f"{commandSymbol}image"):
    await message.channel.send(file = discord.File("font.png"))
  elif message.content.startswith(f"{commandSymbol}react"):
    #emoji = "😋"
    emoji = emojis[randint(0, len(emojis)-1)]
    await message.add_reaction(emoji)

client.run(TOKEN)


"""  elif message.content.startswith(f"{commandSymbol}help"):
    await message.channel.send(embed = embed)  """