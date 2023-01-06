import discord
import datetime

try:
    from rich import print # rich 라이브러리 설치 시 로그가 더 멋있어짐
except:
    pass

from bot_base.command import bot
from persona import use_persona


KST = datetime.timezone(datetime.timedelta(hours=9)) # UTC+9 대한민국 (KST)


@bot.event # 봇이 실행될 때
async def on_ready():
    bot.is_on_message_running = False

    print('\nLogged on as', bot.user)
    print('------')


@bot.event # 서버에서 메세지를 감지했을 때
async def on_message(message: discord.message.Message):
    # don't respond to ourselves and prevent overlap
    if message.author == bot.user or bot.is_on_message_running:
        return

    bot.is_on_message_running = True
    
    author, sharp_num = str(message.author).split('#') # 이름#1234 형태를 #을 기준으로 분리
    now = message.created_at.astimezone(KST).replace(microsecond=0)
    
    print()
    print(f'{now}, {message.guild} - {message.channel}') # 메세지 올라온 시각 / 서버 / 채널
    print(author, message.content, sep=': ') # 메세지 친 사람 / 메세지 내용
    
    if message.content.startswith(bot.command_prefix):
        await bot.process_commands(message)
    else:
        await use_persona(message)

    print('------')
    bot.is_on_message_running = False
