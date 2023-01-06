import discord
import os

intents=intents=discord.Intents.all()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print("\nConnected")
    print(client.user)
@client.event
#async def on_message(message):
    #if message.author != client.user:
        #await message.channel.send(message.content) #echos msg

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
   f'Hi {member.name}, Welcome to "Java SMP"!')



my_secret = os.environ.get("DISCORD_BOT_SECRET")

client.run(my_secret)