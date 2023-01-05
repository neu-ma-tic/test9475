import discord
from discord.ext import commands
import requests
import json

class API(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['f1d'])
  async def f1drivers(self, ctx, year):
    url = f"https://f1-live-motorsport-data.p.rapidapi.com/drivers/standings/{year}"

    headers = {
        'x-rapidapi-host': "f1-live-motorsport-data.p.rapidapi.com",
        'x-rapidapi-key': "0cf2a71cafmshec19ddb6571aafap17707ajsnc73c0c69c950"
        }

    e = discord.Embed(title='F1 Driver standings:', color=discord.Color.red())
    e.set_footer(text='Bot created by Eggnogg')
    response = requests.request("GET", url, headers=headers)
    data = response.json()

    count = 0
    for i in data['results']:
      count += 1
      e.add_field(name=f'{count}:', value= f'Name: {i["driver_name"]}\nTeam: {i["team_name"]}\nPoints: {i["points"]}', inline=False)

    await ctx.send(embed=e)

  @commands.command(aliases=['f1con'])
  async def f1constructors(self, ctx, year):
    url = f"https://f1-live-motorsport-data.p.rapidapi.com/constructors/standings/{year}"

    headers = {
          'x-rapidapi-host': "f1-live-motorsport-data.p.rapidapi.com",
          'x-rapidapi-key': "0cf2a71cafmshec19ddb6571aafap17707ajsnc73c0c69c950"
          }

    e = discord.Embed(title='F1 Constructor standings:', color=discord.Color.red())
    e.set_footer(text='Bot created by Eggnogg')
    response = requests.request("GET", url, headers=headers)
    data = response.json()

    count = 0
    for i in data['results']:
      count += 1
      e.add_field(name=f'{count}:', value= f'Name: {i["team_name"]}\nPoints: {i["points"]}', inline=False)

    await ctx.send(embed=e)

  @commands.command()
  async def movie(self, ctx, *,name):

    url = "http://www.omdbapi.com/?i=tt3896198&apikey=774d4e49"

    querystring = {"t":name,'plot':'short'}

    response = requests.get(url, params=querystring).json()
    e = discord.Embed(title='Results:', color=discord.Color.red())
    
    
    print(response)
    try:
      e.add_field(name='Title:',value=response['Title'])
      e.add_field(name='Type:',value=response['Type'])
      e.add_field(name='Year:',value=response['Year'])
      e.add_field(name='Rated:',value=response['Rated'])
      e.add_field(name='Actors:',value=response['Actors'])
      e.add_field(name='Rating:',value=response['imdbRating'])
      e.add_field(name='Synopsis:',value=response['Plot'],inline=False)
      e.set_image(url=response['Poster'])
      await ctx.send(embed=e)
    except:
      await ctx.reply('Sorry this movie or series could not be found')



def setup(client):
  client.add_cog(API(client))
