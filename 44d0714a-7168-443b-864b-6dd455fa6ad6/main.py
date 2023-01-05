from email import message
from typing_extensions import Self
import keep_alive
import discord
import random
import json
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = discord.Client()
bot = commands.Bot(command_prefix='!',intents=intents)
with open('setting.json','r',encoding='utf_8') as jfile:
    jdata = json.load(jfile)




@bot.event
async def on_ready():
    print("Link Start!")



@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['wchannle code']))
    await channel.send(f'歡迎人類ID{member}')
    print(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['wchannle code']))
    await channel.send(f'さようなら{member}')
    print(f'{member} leave!')

@bot.command()
async def 領域展開(ctx):
    random_pic = random.choice(jdata['領域展開回圖'])
    pic = discord.File(random_pic)
    await ctx.send(file= pic)






#回復訊息
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == client.user:
        return
    if "qq" in message.content:
        await message.channel.send('拍拍')
    if "笑死" in message.content:
        await message.channel.send('哈哈哈')

    if "早安" in message.content:
        await message.channel.send('good morning')

    if "午安" in message.content:
        await message.channel.send('good afternoon')
    if "晚安" in message.content:
        await message.channel.send('good night')
    if message.content == 'cibot':
        await message.channel.send('?') 
    if "先睡" in message.content:
        await message.channel.send('那我也先下了zzz')
    if "變態" in message.content:
        await message.channel.send(random.choice(jdata['變態回圖']))
    if message.content == 'are u sure?':
        await message.channel.send('sure')
    if message.content == 'ping':
        await message.channel.send(f'{round(bot.latency*1000)}(ms)')
    if message.content == '現在該說甚麼':
        await message.channel.send('thx')
    if message.content == 'are u sure?':
        await message.channel.send('sure')
    if "cibot你覺得呢" in message.content:
        random_r = random.choice(["前者","後者"])
        await message.channel.send(random_r)
    if message.content == '領域展開!':
        await message.channel.send(random.choice(jdata['領域展開回圖']))
        

keep_alive.keep_alive()      
bot.run(jdata['TOKEN'])