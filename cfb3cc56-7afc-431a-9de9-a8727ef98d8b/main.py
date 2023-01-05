import discord


client=discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

    if message.content.startswith('%hi'):
      await message.channel.send('Hello!')

      
client.run ('ODUzOTE0MTE3NDI4ODcxMjA4.YMcTfg.Gjw0s7QiC7YhcJXLBU2Bm7_JIv8')
