import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://v2.jokeapi.dev/joke/Any")
  json_data = json.loads(response.text)
  quote = json_data[0, 1] ['joke']
  return(quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('sup nigga')

    if message.content.startswith('$monkey'):
      await message.channel.send('David is a stupid nigger monkey')

    if message.content.startswith('$jew'):
      await message.channel.send('GASSSSSS')

    if message.content.startswith('$42'):
      await message.channel.send('42 nigger jackie robinson')

    if message.content.startswith('$woman'):
      await message.channel.send('Nice tits Frank')

    if message.content.startswith('$quote'):
      quote = get_quote()
      await message.channel.send(quote)


client.run(os.getenv('TOKEN'))