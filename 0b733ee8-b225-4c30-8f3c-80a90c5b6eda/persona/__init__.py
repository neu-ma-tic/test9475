import discord

from persona.copycat import copycat
from persona.ddorai import ddorai
from persona.gif_villain import gif_villain
from persona.gungye import gwansimbeop
from persona.last_chat_reminder import save_last_chat
from persona.pingpong import pingpong


# 페르소나 적용하는 곳 (위에서부터 하나씩 실행됨)
# 페르소나 함수 규칙: 메세지 보내면 return True
personas = [ 
    gwansimbeop,
    ddorai,
    gif_villain,
]

async def use_persona(message: discord.message.Message):
    message_sended = False
    
    for persona in personas:
        if not message_sended: # 여러 페르소나가 동시에 메세지를 보내지 않게 만들기
            message_sended = await persona(message)
        else:
            break
    
    save_last_chat(message)
