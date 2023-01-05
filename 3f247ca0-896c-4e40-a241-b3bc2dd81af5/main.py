import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import asyncio
import random

Client = discord.Client()
bot_prefix = "DG!"
client = commands.Bot(command_prefix=bot_prefix)

''''''

# EVENT- tells you when the bot is up
@client.event
async def on_ready():
    print("The Devils Guard has logged on!")
    print(client.user.name)
    print(client.user.id)
    print("------")
    await client.change_presence((name=" with a large axe"))
    print("Logged in as " + client.user.name)

# listing the servers in IDLE
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

#stop the bot from replying to itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # simple hello response command
    if message.content.startswith("DG!hello", "Hello Devil Guard"):
        msg = "Hello {0.author.mention} How are you today?".format(message)
        await client.send_message(message.channel, msg)
    await client.process_commands(message)

# random text response command  
@client.command(name="ping",
                description="random comand",
                brief="why?",
                pass_context=True)
async def ping(ctx):
    await client.say("pong")


client.loop.create_task(list_servers())
client.run("NTAyMzA0NDc2MTU4NDkyNjky.Dw9NGg.zPNSFd3NGH4L2wfYhb0345hKcbc")