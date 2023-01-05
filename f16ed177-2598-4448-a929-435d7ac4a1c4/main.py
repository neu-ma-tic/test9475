import discord

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("chat with me?"):
    await message.channel.send("Sure!")

client.run('ODY4MTM5NTQwMDQzNDExNTA3.YPrT8w.hwVjslMAHJ2gZOGzdFB6ym4o-Y8')