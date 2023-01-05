import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$test'):
    embed=discord.Embed(title="need 6 for deep stone crypt")
    embed.set_author(name=message.author, url=message.author.avatar_url)
    embed.add_field(name="a", value="1. user 1\n2. user 2\n3. user 3", inline=False)
    embed.set_footer(text="Bot made by zogs#2418")
    await message.channel.send(embed=embed)

  if message.content.startswith('$raid'):
    title = message.content.split('$raid ',1)[1]
    embed=discord.Embed(title=title)
    embed.set_author(name=message.author)
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name="Roster", value="-{0}\n-{1}\n-{2}\n-{3}\n-{4}\n-{5}\n\n✅ to join", inline=False)
    embed.set_footer(text="Bot made by zogs#2418")
    thisMessage = await message.channel.send(embed=embed)
    await thisMessage.add_reaction("✅")

  if message.content.startswith('$emoji'):
    for emoji in client.emojis:
      print("Name:", emoji.name + ",", "ID:", emoji.id)

client.run(os.getenv('TOKEN'))