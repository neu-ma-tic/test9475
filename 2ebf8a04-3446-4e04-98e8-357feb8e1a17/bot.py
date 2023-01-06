import discord
from discord.ext import commands 
from keep_alive import keep_alive
import json,random,os,time
from collections import OrderedDict

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot = commands.Bot(command_prefix='-')#召喚bot  召喚指令前綴



#async def Funcname(parameter_list):
@bot.event #decorator 
async def on_ready():
    print(">>Bot is online<<")
      

  
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unLoaded {extension} done.')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reLoaded {extension} done.')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')




if __name__ == "__main__":
    keep_alive()
    bot.run(jdata['TOKEN'])#arguments放token   json資料->字典