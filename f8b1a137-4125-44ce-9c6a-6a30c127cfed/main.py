import discord 
import os

client = discord.Client()

@client.event

async def on_ready():
    print("We have logged in as {}".format(client))

@client.event

async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content('$hello'):
        await message.channel.send("Hello, it is nice to meet you!")

client.run(os.getenv('TOKEN'))