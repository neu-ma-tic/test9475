import discord


async def copycat(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    await channel.send(content) # 채널에 메세지 보내기
    return True
