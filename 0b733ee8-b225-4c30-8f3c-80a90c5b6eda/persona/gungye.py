import discord
import time


state = 0
achoo = False
sin = False


async def gwansimbeop(message: discord.message.Message):
    global state, achoo, sin
    
    content = message.content
    channel = message.channel

    if '궁예' in content and state == 0:
        await channel.send('그래, 내가 궁예다.')
        time.sleep(1)
        await channel.send('도대체 그대들이 이 나라의 벼슬아치들인지,')
        time.sleep(1)
        await channel.send('아니면 뒷간의 똥막대기인지')
        time.sleep(1)
        await channel.send('그걸 알 수가 없단 말이야.')
        state = 1

    elif ('에취' in content or '콜록' in content or 'achoo' in content) and not achoo:
        await message.reply('누구인가?')
        time.sleep(2)
        await channel.send('지금 누가 기침 소리를 내었어?')
        achoo = True

    elif achoo and not sin:
        await channel.send('참으로 딱하구나.')
        time.sleep(1)
        await channel.send('짐이 지금 관심법을 하고 있는데,')
        time.sleep(1)
        await channel.send('어찌 기침을 할 수 있느냐 이 미련한 것아아!!')
        sin = True

    elif sin:
        await channel.send('내가 가만히 보니,')
        time.sleep(1)
        await channel.send('니놈 머릿속엔 마구니가 가득찼구나.')
        time.sleep(1)
        await channel.send('더 이상의 대사는 없다')
        state = 0
        achoo = False
        sin = False
    
    elif state == 1:
        await channel.send('그대들 모두 하나같이')
        time.sleep(1)
        await channel.send('똥으로 가득차있어, 똥 말이야')
        state = 2
    
    else:
        return False

    return True # 전송한 메세지 - 있음:True / 없음:False
