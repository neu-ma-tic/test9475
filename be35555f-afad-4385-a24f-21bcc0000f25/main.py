import os
import asyncio
import random
import requests
import Discord
from discord.ext import commands
from runforever import runforever
from imgurpython import ImgurClient


client = commands.Bot(command_prefix='!')
client.remove_command('help')
bot_channel = "499767223192387584"
test_channel ="499745396633894912"
bot_channel = test_channel
triggers = ['love you','love u', 'ily', 'luv u', 'luv you'
]
clientID = os.environ.get("CLIENT_ID")
secretID = os.environ.get("CLIENT_SECRET")
imgurClient = ImgurClient(clientID, secretID)

messages = ["I love how you always make me laugh whenever I’m sad","I love how you get me ice cream whenever I'm sad","I love how caring you are","I love how you understand me","I love you because you're so smart","I love that you watch weird documentaries","I love you because of your cool wheelchair dance moves","I love you because you make me want to be a better person","I love the little things you do for me","I love laying next to you",
"I love your hugs","I love holding your hand","I love when we share milkshakes","I love it when you protect me from sketchy homeless people","I love your voice","I love everything about you", "I love the fact that you can move your nostrils", "I love you because you're so weird", "I love that you don't freak out about things","I love you because you keep me calm", "I love the way you may me feel all giddy", "I love being with you","I love your hugs","I love your kisses","I love when you tag me in dog posts",
"I love your memes","I love your smile","I love that you never say no to things I want to do", "I love that I can be myself around you",
"I love how you laugh","I love how tall you are",
"I love your kind heart","I love how chill you are","I love looking at your face","I love being with you", "I love your fornite dances", "I love when you cuddle with me", "I love how you always eat my food", "I love that you listen to me"
]

@client.event
async def on_ready():
    print("client ready")
    print(client.user)

@client.command()
async def loveme():
    channel = client.get_channel(bot_channel)
    await client.send_message(channel, "💕 " + random.choice(messages)+ " 💕")
@client.command()
async def sendpic():
    channel = client.get_channel(bot_channel)
    image_links = []
    for image in imgurClient.get_album_images("OEvj0D1"):
      image_links.append(image.link)
    
    embed_img = discord.Embed(
      colour = discord.Colour.green()
    ) 
    embed_img.set_image(url=random.choice(image_links))
    embed_img.set_author(name = "😳Sending pic...")
    embed_img.set_footer(text="...received😳")
    await client.send_message(channel,embed=embed_img)

@client.command()
async def kissme(): 
    channel = client.get_channel(bot_channel)
    embed_gif = discord.Embed(
      colour = discord.Colour.red()
    ) 
    embed_gif.set_image(url="http://i.imgur.com/mPbWj6F.gif")
    embed_gif.set_author(name = "💕Sending kiss...")
    embed_gif.set_footer(text="...received💕")
    await client.send_message(channel,embed=embed_gif)

@client.command()
async def meme():
  channel = client.get_channel(bot_channel)
  meme_links = []
  for image in imgurClient.subreddit_gallery("memes", sort='hot', window='week', page=0):
    if(image.is_album == False and image.type !='image/gif' and image.link.endswith('.mp4') == False):
      meme_links.append(image.link)   
  embed_img = discord.Embed(colour=0x408080
  ) 
  embed_img.set_image(url=random.choice(meme_links))
  embed_img.set_author(name = "🍆Sending dank meme...")
  embed_img.set_footer(text="...received👅")
  await client.send_message(channel,embed=embed_img)

@client.command()
async def pepe():
  channel = client.get_channel(bot_channel)
  meme_links = []
  for image in imgurClient.subreddit_gallery("pepe", sort='hot', window='week', page=0):
    if(image.is_album == False and image.type !='image/gif'and image.link.endswith('.mp4') == False):
      meme_links.append(image.link)   
  embed_img = discord.Embed(colour=0x00d500
  ) 
  embed_img.set_image(url=random.choice(meme_links))
  embed_img.set_author(name = "🐸Sending rare pepe meme...")
  embed_img.set_footer(text="...received💦")
  await client.send_message(channel,embed=embed_img)  

@client.command()
async def aww():
  channel = client.get_channel(bot_channel)
  aww_links = []
  for image in imgurClient.subreddit_gallery("aww", sort='hot', window='week', page=0):
    if(image.is_album == False and image.type !='image/gif' and image.link.endswith('.mp4') == False):
      aww_links.append(image.link)   
  embed_img = discord.Embed(colour=0xe36fac
  ) 
  embed_img.set_image(url=random.choice(aww_links))
  embed_img.set_author(name = "🐶Sending cuteness...")
  embed_img.set_footer(text="...received🤗")
  await client.send_message(channel,embed=embed_img)


@client.command(pass_context=True)
async def trump(ctx,arg):  
  if arg:
    channel = client.get_channel(bot_channel)
    response = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q=" + arg)
    data = response.json()
    print(data['message'])
  else:
    channel = client.get_channel(bot_channel)
    response = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
    data = response.json()
    print(data['message'])

@client.command()
async def help():
  channel = client.get_channel(bot_channel)
  embed = discord.Embed(
    colour = discord.Colour.blue()
  ) 
  embed.set_author(name = '🔔 Help')
  embed.add_field(name = '!loveme', value='💕 sends 1 of the million reasons why I love Jim')
  embed.add_field(name = '!kissme', value='😘 sends a special kiss')
  embed.add_field(name = '!sendpic', value='😳 sends a pic of me')
  embed.add_field(name = '!meme', value='🍆 sends a dank meme')
  embed.add_field(name = '!aww', value='🐶 sends a cute picture(mostly doggies!)')
  embed.add_field(name = '!pepe', value='🐸 sends a rare pepe meme')
  await client.send_message(channel, embed=embed)

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        message.content = message.content.lower()
        for t in triggers:
          if t in message.content:
            channel = client.get_channel(bot_channel)
            await client.send_message(channel, "💕 " + random.choice(messages) + " 💕")
        await client.process_commands(message)

runforever()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)