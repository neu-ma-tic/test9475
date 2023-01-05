import discord 

client = discord.Client()

@client.event 
async def on_ready():
  print('We have logged in as{0.user}'.format (client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('ping'):
    await message.channel.send('pong!')


@client.event
async def on_

client.run("ODg2ODQ5Mjc2MDQ5NzY4NDQ4.YT7kwA.HsFQgx0LsRwrnq2savEXLhpzuhc")


