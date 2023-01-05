import facts
import meme
import swmeme
import discord
import random
import os
import time
import discord.ext
import random
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

# please no memes in general


jokes = ["Why did the chicken cross the road?..........To get to the other side!", "Ur ugly, just joking ur pretty...... ugly!", "What did the duck say when she bought liptick?......... Put it on my bill!", "I hate Russian dolls, they're so full of themselves!", "What do you say to the lemon who is sick......Here is some lemon aid ", "What do bees do if they need a ride?....... Wait at the buzz stop!", "Why did the can crusher quit his job? Because it was soda pressing!", "I just went to an emotional wedding. Even the cake was in tiers.", "Why do seagulls fly over the sea? Because if they flew over the bay, they're bagels!", "What do you call birds who stick together? Vel-crows.","hello this is owen speaking I hacked into the code to add this here LOL."]#list of jokes
#PIgeONPIGEONGPIGEONPIGEONPIGEONPIGEONPIGEONPIGEONPIGEONPIGEONPIGEONPIGEON
dark_jokes = ["Why should you get a black xbox?..........Because it runs faster", "dark humour is like food, not everyone gets it", "I just read that someone gets stabbed every 52 seconds, poor guy"]#list of dark jokes

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here



@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online

# the problem is ABOVE this line - for some reason the event "on_ready" isn't firing, so either Python is failing to realise the fact that the bot is online, or Discord isn't sending Python confirmation that the bot is online.

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return 'SQUIDN'

def run():
    app.run(host='0.0.0.0', port=8080)

def b():
    server = Thread(target=run)
    server.start()
    
@client.command()
async def joke(ctx):
    await ctx.send(random.choice(jokes))
@client.command()
async def darkjoke(ctx):
    await ctx.send(random.choice(dark_jokes))
@client.command()
async def fact(ctx):
    await ctx.send(facts.TrueFacts)
@client.command()
async def swmeme(ctx):
    await ctx.send(swmeme.swmemes)
@client.command()
async def meme(ctx):
    await ctx.send(meme)

@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions

        
    except:
        await ctx.send("bot does not have the kick members permission!")

print(facts.TrueFacts)



# PLACE ALL NSFW/VIOLENT GAY PORNO COMMANDS BETWEEN THESE LINES!!!




# PLACE ALL NSFW/VIOLENT GAY PORNO COMMANDS BETWEEN THESE LINES!!!


client.run(os.getenv("TOKEN"))
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!


