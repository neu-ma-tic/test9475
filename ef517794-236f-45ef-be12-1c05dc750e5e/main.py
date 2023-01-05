import discord
import os #to use secret variables

token = os.environ['token']

client = discord.Client()

@client.event
async def on_message(message):#this is to detect messages
  if message.author == client.user: #if the author of the msg is the bot
    return #dont do anything n just return

  if message.content.startswith("=hello"): #if user sends =ping
    msg = 'Hello!' #set the message to pong
    await message.reply(msg, mention_author = True) 
    #sends the message to reply to the author

  if message.content.startswith("=greet"):
    msg = "hello " + message.author.name #says hello and adds the author of the message next to it
    await message.reply(msg, mention_author = True)
     #sends the message to reply to the author

@client.event
async def on_ready(): #will run when the discord is online
    print('Logged on as CatKiss!') #say its online

      
try:
  client.run(token) #try running the bot if its wrong token say its the wrong token
except:
  print("Wrong TOKEN!")
#to log into the bot client