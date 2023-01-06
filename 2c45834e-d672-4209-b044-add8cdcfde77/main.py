import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

restrictedWords = ["computer", "rat", "mouse"]

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("hello mr.garwick"):
    await message.channel.send("hello!")

  for word in restrictedWords:
    if word in message.content:
      await message.delete()
  

client.run("OTU4NDg3MjE2NzE4NDg3NjEy.YkOCyA.UowbqXEVD_GgCogNaBV-X2_Gq9Q"
)



