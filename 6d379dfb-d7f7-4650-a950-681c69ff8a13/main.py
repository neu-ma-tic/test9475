import discord
from discord.ext import commands
from webserver import keep_alive
import os

client = discord.Client()
keywords=[]
cuswords=[]







@client.event
async def on_message(message):
    for i in range(len(cuswords)):
        if cuswords[i] in message.content:
                  await message.channel.send(f'{(message.author.mention)} Please Watch your Language.Your Previous Messege will be Reviewed by <@&{858524176822566933}> and if you have used any Offencive Language you will Get a Warning ')
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            await message.channel.send(f'{(message.author.mention)} O YEAHHH!!')
    if message.content.startswith('!!help'):
        await message.channel.send(f'<@&{858524176822566933}> Mr {(message.author.mention)} is having some trouble here')

keep_alive()


my_secret = os.environ['Discord_Top_Secret']

client.run(my_secret)

