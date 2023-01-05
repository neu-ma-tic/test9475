import discord
from discord.ext import commands
import os
import requests
import json
import random
from replit import db
from keepalive import keep_alive

import ffmpeg
#stream = ffmpeg.input('input.mp4')
#stream = ffmpeg.hflip(stream)
#stream = ffmpeg.output(stream, 'output.mp4')


#client = discord.Client()
client = commands.Bot(command_prefix = '.')

sad_words = [
    "sad", "depressed", "deflated", "unhappy", "hate", "angry", "depressing"
]

thisisalist = ["this", "blhaalalalhbblala", "umn mr dean you think we're comediens?"]

starter_encouragements = ["Cheer up!", "Hang in there!", "You got this big guy!"]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)



def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]
  
def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('I logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        msg = message.content
        
        if msg.startswith('$hello'):
            await message.channel.send('Hello!')
        
        if msg.startswith('$inspire'):
            quote = get_quote()
            await message.channel.send(quote)
        
        if db["responding"]:
          options = starter_encouragements
          if "encouragements" in db.keys():
            options = options + db["encouragements"]

          if any(word in msg for word in sad_words):
            if 


            if message contains " " 
            Make what came before a word
            add word to my list





            await message.channel.send(random.choice(options))
          
        if msg.startswith("$new"):
          encouraging_message = msg.split("$new ",1)[1]
          update_encouragements(encouraging_message)
          await message.channel.send("New encouraging message added!")
        if msg.startswith("$del"):
          encouragements = []
          if "encouragements" in db.keys():
            index = int(msg.split("$del",1)[1]) #don't need space here because converting to integer
            delete_encouragements(index)
            encouragements = db["encouragements"]
            await message.channel.send(encouragements)
        if msg.startswith("$list"):
          encouragements = []
          if "encouragements" in db.keys():
            encouragements = db["encouragements"]
          await message.channel.send(encouragements)
        
        if msg.startswith("$responding"):
          value = msg.split("$responding ", 1)[1]
          if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
          else:
            db["responding"] = False
            await message.channel.send("Responding is off.")
        if msg.startswith("$echo"):
          value = msg.split("$echo ", 1)[1]
          await message.channel.send(value)
        if msg.startswith("$join"):
          await join(message.author)
        if msg.startswith("$leave"):
          await leave(message.author)
        if msg.startswith("$ping"):
          await ping(message.author)
        
#https://www.youtube.com/watch?v=MbhXIddT2YY
@client.command()


async def ping(ctx):
  await ctx.channel.send('Pong!')

async def join(ctx):
  channel = ctx.message.author.voice.voice_channel
  await client.join_voice_channel(channel)
async def leave(ctx):
  server = ctx.message.server
  voice_client = client.voice_client_in(server)
  await voice_client.disconnect()


    
        

          
            


        

keep_alive()
client.run(os.getenv('TOKEN'))
