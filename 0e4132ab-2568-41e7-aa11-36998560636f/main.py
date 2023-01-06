import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.authro == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send('Hello!')

client.run('ODU4NzE2ODcyMjk1MDU1MzYw.YNiMaA.Q8dEiLa66kYRctsQv0qM6i0MS7I')
