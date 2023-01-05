import discord
client = discord.Client

@client.event
async def on_ready():
  print(f"I'm ready, I've logged as {0.user}".format(user))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("\\Hello"):
      await message.channel.send("Hello")