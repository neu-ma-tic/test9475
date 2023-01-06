import os
import requests
import urllib.parse
import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Logged on as {}!".format(bot.user.name))

@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  await bot.process_commands(message)
  
@bot.event
async def on_member_join(member):
  role = discord.utils.get(member.guild.roles, id=887167264921628703)
  await member.add_roles(role)
  await member.send("Weclome {}".format(member.name))
  print("{} was given a role {}".format(member.name, role))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Invalid command. Try using** `!help` **to figure out commands!**")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Please pass in all requirements.**')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**You dont have all the requirements or permissions for using this command :angry:**")

@bot.command()
async def find(ctx, media_type, *data):

  await ctx.message.delete()

  if len(data) == 0:
    msg = "Wrong! try this :smile: `!find {} The Little Mermaid (1989)`".format(media_type)
    await ctx.send(msg)
    return

  if len(data) > 1:

    data = " ".join(data[:])
    safe_string = urllib.parse.quote_plus(data)

    query = 'https://api.themoviedb.org/3/search/movie?api_key={}&include_adult=false&query={}'.format(os.environ['tmdb'],safe_string)
    response = requests.get(query)
    if response.status_code == 200:

      data = response.json()
      results = data['results']

      print('Total Results: {}'.format(len(results)))
      print('Orginal Title: {}'.format(results[0]['id']))
      print('           ID: {}'.format(results[0]['original_title']))

    else:
      msg = "unable to search due to error"

    print(msg)

    #await ctx.send(msg)
  else:
    data=data[0]
    if data.isdigit():
      msg = "search for movie by id"
    else:
      msg = "search for movie by string"

    await ctx.send(msg)

bot.run(os.environ['sauce'])