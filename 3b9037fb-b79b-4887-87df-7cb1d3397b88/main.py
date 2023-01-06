import discord

client = discord.Client()

@client.event
async def on_ready():
  print('we have loggen in as {0.user}'
  .format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return



    client.run()