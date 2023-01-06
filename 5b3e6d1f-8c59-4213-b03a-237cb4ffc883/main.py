import discord
from discord import channel # 將dc的模組導入
from discord.ext import commands
import json
import random
import os
import keep_alive


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix = '#' , intents = intents) # 機器人指令的指令字首

@bot.event # 機器人開機
async def on_ready():
    print(">> Bot is online <<")



@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension}')
    
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension}')
    
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension}')

for filename in os.listdir('./cmds'): # 導入所有的模組
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}') # 將最後的.py去除，只保留檔案名稱的部分

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])