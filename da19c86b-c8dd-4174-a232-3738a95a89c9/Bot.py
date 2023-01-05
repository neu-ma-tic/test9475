import discord
import json
import requests
import os
from server import keep_alive
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.command() 
async def hello(ctx): 
    author = ctx.message.author 
    await ctx.send(f'Hello, {author.mention}!') 

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Random Dog') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Random Cat') 
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed) 

@bot.command()
async def pat(ctx):
    response = requests.get('https://some-random-api.ml/animu/pat') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Random Pat') 
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)
    
@bot.command()
async def quote(ctx):
    await ctx.send(get_quote()) 

bot.run(settings['token']) 

