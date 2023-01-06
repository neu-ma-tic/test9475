import random

import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from persona.last_chat_reminder import remind_last_chat


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def ping(ctx: Context):
    await ctx.send(f'pong! {round(round(ctx.bot.latency, 4)*1000)}ms') # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.


@bot.command(name='뽑기')
async def random_choose(ctx: Context, number: int = None, n_choice: int = None):
    if number is None and n_choice is None:
        await ctx.message.reply('```!뽑기 [총 숫자] [뽑을 숫자]```')
    elif n_choice is None:
        choice = random.sample(range(1, number+1), 1)
        await ctx.message.reply(f'뽑은 숫자\n{sorted(choice)}')
    else:
        choice = random.sample(range(1, number+1), n_choice)
        await ctx.message.reply(f'뽑은 숫자\n{sorted(choice)}')


@bot.command(name='마지막채팅')
async def lastchat(ctx: Context, member: str = None):
    if member is None:
        await ctx.message.reply('```!마지막채팅 [유저이름]```')
    else:
        await remind_last_chat(ctx.message, member)
