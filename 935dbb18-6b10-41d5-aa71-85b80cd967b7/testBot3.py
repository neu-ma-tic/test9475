import discord
client = discord.Client()

@client.event
async def on_ready():
  print("We have loged in as {0.user}".format(client))

@client.event
async def on_message(message):
 if message.author == client.user:
   return

 if message.content.startswith('hello'):
   await message.channel.send('Hello!')

client.run('OTc4Nzk2MDE4MTIyNTE0NDQy.GkmSyq.dyF535yNOtZXGu4rLSYcWHG5jGM33z7gVfxsCc')