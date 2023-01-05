import discord
import os
from joke import get_joke,search_joke
from meme import get_meme,generate_meme

my_secret = os.environ['TOKEN']

client = discord.Client()

#get_images()
#generate_meme("Condescending-Wonka","cat","dumb")
#get_meme()
generate_meme()

#register event, also call back
@client.event
#onready event, call when the bot being used
async def on_ready():
    print("We are {0.user}".format(client))


@client.event
#message from bot
#triggered when message is received
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    #Convert joke

    try:
      if msg.startswith('$tell me a joke'):
        await message.channel.send(get_joke())
      if msg.startswith('$tell me a {0} joke'.format(msg.split()[3]) or '$tell me an {0} joke'.format(msg.split()[3])):
        await message.channel.send(search_joke(msg.split()[3]))
    
      #convert meme
      if msg.startswith("$send me a meme"):
        await message.channel.send(get_meme())
      
   
      
        #await message.channel.send("```\nEnter the command below in code block\n ... \n{meme type}\n{top}\n{bottom}```")
        """
      if msg.starswith("```\n{0}\n{1}\n{2}\n```".format(msg.splitlines()[1],msg.splitlines()[2],msg.splitlines()[3])):
          print(msg.splitlines()[1])
          print(msg.splitlines()[2])
          print(msg.splitlines()[3])
          """
          
      

        #await message.channel.send(generate_meme(msg.splitlines()[1],msg.splitlines()[2],msg.splitlines()[3]))
        
    except:
      print("Your command is invalid")

    



  
#run the bot
client.run(my_secret)
