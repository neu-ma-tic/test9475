import discord
from keep_alive import keep_alive
from diceCalculator import gibErfolge
from diceCalculator import machLustigeNachricht

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
      
    if message.content.startswith('!'):
        input = message.content[1:]
        erfolge = gibErfolge(input)
        nachricht = machLustigeNachricht(erfolge)
        await message.channel.send(nachricht)
  
keep_alive()

client.run('')