import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')
# command_prefix為輸入機器人指令前要加的字串
# 指令跟監聽事件要放在bot後面，run前面
@bot.event
async def on_ready():
   print('機器人上線中。。。')
#@bot.command()
async def on_message(message):
   # 防止機器人接收到機器人傳的訊息
   if message.author != bot.user:
       channel = message.channel
       #content = message.content
       msgtime = message.created_at.today()
       await channel.send(f'時間{msgtime}')

@bot.command()
async def 大哥(ctx):
   await ctx.send('||不能說的男人：超負荷||')

@bot.command()
async def 哭阿(ctx):
   image = discord.File('test.png')
   await ctx.send(file=image)

@bot.command()
async def clear(ctx):
    await ctx.channel.purge(limit=3)

def is_bot(message):
    return message.author == bot.user
#如果是機器人的訊息則刪除
@bot.command()
async def clear_bot(ctx):
    await ctx.channel.purge(check=is_bot, limit=5)  

@bot.command()
async def 春日部(ctx):
    embed=discord.Embed(title="春日部防衛隊成員一覽", description="就是說你們", color=0xff8080)
    embed.set_author(name="BY哞哞")
    embed.add_field(name="超激大帥哥", value=f'棉花糖\n香蕉\nKen\n布魯大隊長叔公', inline=False)
    await ctx.send(embed=embed)

@bot.group()
async def buy(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('what do you want to buy?')
@buy.command()
async def apple(ctx):
    await ctx.send('buy **apple**!')
@buy.command()
async def banana(ctx):
    await ctx.send('buy **banana**!')

@bot.event
async def on_command_error(ctx, exception):
  await ctx.send(exception)

token = open('token.txt').readline()
bot.run(token)