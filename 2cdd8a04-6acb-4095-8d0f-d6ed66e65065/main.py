from webserver import keep_alive
import os
import discord
from discord.ext import commands
import random

prefix = '.'
bot = commands.Bot(command_prefix=prefix)  #тестовый префикс
bot.remove_command('help')


@bot.event
async def on_ready():
    print('бот в онлайне')

    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Streaming(
            name='.help / ФПК РЖД',
            url='https://discord.gg/s6gxMRPT5Z'))


@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title='📜 | help',
                           description=f'''
		привет мой префикс : {prefix}
		вот список моих команд
		```
―-―-―-―ФПК РДЖ―-―-―-―
{prefix}ping - pong
{prefix}game - ссылка на игру
{prefix}team - тима
{prefix}adhelp - команды для администраторов сервера```
		''',
                           color=0x466db3)
    await ctx.send(embed=embed1)


@bot.command()
async def adhelp(ctx):
    embed7 = discord.Embed(title='🔗 | админ команды',
                           description=f'''
        ```
―-―-―-―ФПК РДЖ―-―-―-―
{prefix}clear - очистка чата
{prefix}say - скачать от лица бота
{prefix}news - сделать оповещение(спамит в указанный канал 5 раз 
вашим сообщение)
пример {prefix}news :
{prefix}news @everyone начался рейс все заходим в плейс```
		''',
                           color=0x466db3)
    await ctx.send(embed=embed7)


@bot.command()
async def team(ctx):
    embed11 = discord.Embed(title='🔨 | команда',
                            description='''
		```
Mironsue#4356 - создатель
roman_666#4218 - создатель
NightSp#0687 - создатель
! Snickers#8719 - кодер```
		''',
                            color=0x466db3)
    await ctx.send(embed=embed11)


@bot.command()
async def ping(ctx):
    embed4 = discord.Embed(title='🏓 | pong',
                           description='pong!',
                           color=0x466db3)
    await ctx.send(embed=embed4)


@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, arg):
    await ctx.message.delete()
    embed2 = discord.Embed(title='✅', description=arg, color=0x466db3)
    await ctx.send(embed=embed2)


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=10000):
    await ctx.channel.purge(limit=amount)
    embed3 = discord.Embed(title='🗑 | clear',
                           description='чат успешно очищен✔',
                           color=0x466db3)
    await ctx.send(embed=embed3)


@bot.command()
@commands.has_permissions(administrator=True)
async def news(ctx, *, text):
    for i in range(5):
        embed8 = discord.Embed(title='оповещения',
                               description=text,
                               color=0x466db3)
        await ctx.send(embed=embed8)


@bot.command()
async def game(ctx):
    embed12 = discord.Embed(
        title='🔗 | ссылка на игру',
        description='https://www.roblox.com/games/10020083926/unnamed',
        color=0x466db3)
    await ctx.send(embed=embed12)


bot.command()


async def gg(ctx, *, text):
    danet = ['да ✔', 'нет❌']
    embed13 = discord.Embed(title='50/50',
                            description=f'''		
		```
		вопрос : {text}
		мой ответ : 
		{random.choice(danet)}```
		''',
                            color=0x466db3)
    await ctx.send(embde=edmbed13)


@bot.command()
async def ball(ctx, *, text):
    rball = [
        'мой ответ да✔', 'нет я так не думаю ❌', 'затрудняюсь овтетить...😶',
        'нехочу говорить😈', 'возможно возможно...🤔',
        'я сам хз что ответь, может да может нет, хз💀'
    ]
    embed14 = discord.Embed(title='🔮 | рандом ответ',
                            description=f'''
	    воспрос был задон :
	    {text}
	    мой ответ :
	    {random.choice(rball)}''')
  
keep_alive()
bot.run('OTkzNTgzMjcxNTE2NTgyMDM5.G2Ummg.BCSESGoorpCrdlu0AKkBMc-8PN1jxs4ixkVndE')