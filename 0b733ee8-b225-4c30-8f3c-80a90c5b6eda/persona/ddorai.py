import discord
import random
import time


eojjeol_stack = 0
eojjeol_flows = ['어쩔티비', '저쩔티비', '어쩔냉장고', '저쩔세탁기', '어쩔스타일러', '저쩔가습기', '어쩔초고속진공블랜딩믹서기']


async def ddorai(message: discord.message.Message):
    global eojjeol_stack, eojjeol_flows

    content = message.content
    channel = message.channel

    if content == 'ping':
        await message.reply('pong')

    elif content == '응~':
        await channel.send('아니야~')

    elif content == '...':
        await channel.send('점점점...')
    
    elif content.rstrip('!') in ['와', 'WA']:
        await message.reply('샌즈' + '!' * content.count('!'))

    elif '샌즈' in content:
        await message.reply('와! 언더테일 아시는구나!')
        time.sleep(0.8)
        await channel.send('겁.나.어.렵.습.니.다.')

    elif content == '어쩔초고속진공블랜딩믹서기' or (
        ('어쩔' in content or '저쩔' in content) and eojjeol_stack >= 3):
        await message.reply('어쩔어쩔~ 저쩔저쩔~')
        time.sleep(0.8)
        await channel.send('안물티비~ 안궁티비~ 뇌절티비~')
        time.sleep(0.8)
        await channel.send('우짤래미~ 저짤래미~ 쿠쿠루삥뽕')
        time.sleep(0.8)
        eojjeol_stack = 0

    elif content in eojjeol_flows:
        text = eojjeol_flows[eojjeol_flows.index(content)+1]
        await message.reply(text)
        eojjeol_stack += 1
    
    else:
        ran = random.randint(1, 20)
        if ran == 1:
            await channel.send('어쩔티비')
        elif ran == 2:
            await channel.send('띠용')
        elif ran == 3:
            await channel.send('뿡')
        elif ran == 4:
            await message.pin()
        else:
            return False

    return True # 전송한 메세지 - 있음:True / 없음:False
        