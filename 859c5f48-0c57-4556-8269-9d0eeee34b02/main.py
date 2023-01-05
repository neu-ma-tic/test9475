import os
botname = "Rick Astley"

from os import system
from datetime import datetime


token1 = os.environ['token1']
import discord
import pyjokes

client = discord.Client()
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    mesg = (message.content).lower()
    if message.author == client.user:
        return

    if (message.content.startswith('$hello')):
        await message.channel.send(f"Hello {message.author.name}")
        print("Hello sent.")
    elif (message.content.startswith('$joke')):
        await message.channel.send(f"{pyjokes.get_joke('en','all')}")
        print("Sent a joke")
    elif (message.content.startswith('$help')):
        await message.channel.send(
            f"{botname} made to make you a linux geek\nType $hello for saying me hello\nType $joke so that i can tell you a joke"
        )
        print("Sent help")
    elif (message.content.startswith('$time')):
        await message.channel.send(f'Time = {datetime.now()}')
    elif ("bitch" in mesg or "fuck" in mesg or "chutiye" in mesg or "bhanchod" in mesg or "asshole" in mesg or "bastard" in mesg or "wotdefok" in mesg or "lawada" in mesg or "bhenchod" in mesg or "lawade" in mesg or "arschloch" in mesg or "schlingel" in mesg or "moron" in mesg):
        await message.delete()
        await message.channel.send(f"**{message.author.name}** used abusive word. Message has been deleted.")
        print(f"{message.author.name} used abusive word")
    elif (mesg == "rickroll"):
        await message.channel.send("https://giphy.com/gifs/rick-roll-g7GKcSzwQfugw")
    elif (message.content.startswith('$java')):
    	messg = message.content.replace("$java" , "")
    	await message.channel.send("Compiling java...")
    	f = open("mn.java", "w")
    	f.write(f'''{messg}''')
    	system(f"javac ./mn.java && java mn > output.txt")
    	print(messg)
    	f.close()
    	f = open("output.txt","r")
    	ans = f.read()
    	await message.delete()
    	await message.channel.send(f" >> {ans}")
    	f.close()
client.run(token1)