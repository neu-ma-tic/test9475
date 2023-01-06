import discord

TOKEN = 'ODg4ODU2MDM0MTg4MzUzNTQ4.YUYxsA.__tBvXKmEbsr6lau6aj7QHMhHLY'

client = discord.Client()

badWordList = ['idiot', 'moran']

@client.event
async def on_ready():
  print('I am connected to discord! - {}'.format(client.user))
  for guild in client.guilds:
    print("{} {} - member count: {:d}".format(guild.name, guild.id, guild.member_count))
    print(len(guild.members))
    for member in guild.members:
      print(" - {} {}".format(member.name, member.id))
    
    banned_users = await guild.bans()
    for ban_entry in banned_users:
            user = ban_entry.user
            await guild.unban(user)



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  for word in badWordList:
    if word in message.content:
#        await message.channel.send("Warning: " + message.author.name + ", you are not being respectful, and please do not do that again!")
  #      await message.delete()
  #      break
#        await message.guild.ban(message.author)
      channel = message.channel
      msgs = await channel.history(limit=10).flatten()
      print(msgs)
      await message.delete()
      await channel.send("Disrepectful behavior will be banned!!!", delete_after = 5)
      await channel.send(message.author.id)
#        await message.author.ban()

client.run(TOKEN)