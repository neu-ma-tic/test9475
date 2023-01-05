
import discord 

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author ==  client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello')

TOKEN= "MTAwNjQ5NDQ0MzUyNTg5ODM1MA.G1OD5c.icqk4yHcIoWKJXfCpH8L0sPTHKdrPwogYVXb9w"

client.run(TOKEN) 