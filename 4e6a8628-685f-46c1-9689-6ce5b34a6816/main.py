import discord

TOKEN = 'OTk5MjY4OTQxMzcxMjg5NzUx.Gh3d0I.q_h3AYv6qrkRo6omu6p2pFvL36jCGLIHQHX5AU'

client = discord.Client()
@client.event
async def on_ready():
   print("{0.user is online!".format(client

@client.event
async def on_message(message):
         if message.author == client.user:
  return
elif message.content.startswith("%rules")
await message.channel.send("1.No swearing 2. Be nice and don't be toxic 3. Use commands in the right part of the server!")

client.run(TOKEN)

python3 Desktop/discordBot.py