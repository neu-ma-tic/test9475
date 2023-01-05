import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print('-----Mickey------')


@client.event
async def on_message(message):
    if not message.content.lower().startswith('?test'):
        return
    await client.send_message(message.channel, "Olá!")


client.run('ODYxNzgxMzEyNTgzMTA2NTYw.YOOyZA.PWQGPAY1cJyno121Qu4Ehu2xaKo')