import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have loggen in as {0.user}' .format(client))

  @client.event
  async def on_message(message):
    if message.author ==client.user:
      return

    if message.contentstartswitch('$hello'):
      awa