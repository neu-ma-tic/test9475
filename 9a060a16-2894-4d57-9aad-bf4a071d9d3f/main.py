import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Bot Online {0.user}')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('!Enlightenment'):
        await message.channel.send('https://tenor.com/view/winning-smile-gif-21571455')

    if message.author == client.user:
      return

    if message.content.startswith('!Video'):
        await message.channel.send('https://www.youtube.com/watch?v=Qe2squBfa80')

Token = os.environ['Token']
keep_alive()
client.run(Token)