import discord
import os
TOKEN='ODM4MzgzNTY4NjczMTc3NjEx.YI6Tiw.-owEF75bDPVYGVPxtOPPev43f4U'

client= discord.Client()

@client.event
async def on_ready():
    print('Logged in as',client.user.name)
    #print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("hello"):
    await message.channel.send("hello")
  if message.content.startswith("how are you"):
    await message.channel.send("Fine,and YOU?")
    if message.content.startswith("fine"):
      await message.channel.send("Ok")

      



client.run(TOKEN)


