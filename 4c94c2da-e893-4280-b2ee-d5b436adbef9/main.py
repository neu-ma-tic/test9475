from keep_alive import keep_alive
import discord
import os


keep_alive()
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #игнорируем сообщения ботов
    if message.author.bot: 
        return

    #ответное приветствие
    if message.content.startswith('!hello'):
        await message.reply('Hello!', mention_author=True)




client.run(os.getenv('TOKEN'))