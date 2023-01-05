import discord, json, os, keep_alive
from discord.ext import commands

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


# @bot.event
# async def on_ready():
#     print(">> Bot is online <<")

for Filename in os.listdir('./cmds'):
    if Filename.endswith('py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

    
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done')

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(jdata['TOKEN'])
