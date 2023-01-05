import discord
import os

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "-Translate":
        await message.channel.send("Translating...")
    
    if message.content == "-Help":
        await message.channel.send("> My purpose is to translate your sentences. Use this syntax (Careful it's case sensitive): -Translate 'Word or sentence to translate' to 'Language to translate into'")
    
    if message.content.startswith("-Translate"):
      SplitInput = message.content.split("'")
      StrToTr = SplitInput[1]
      LgToTr = SplitInput[3]
    
    if message.content == "-Test":
      TranslatedStr = os.system('powershell -Command "Invoke-WebRequest https://translate.google.ca/ "')
      await message.channel.send(TranslatedStr) 
      






BotToken = os.environ['BotToken']
client.run(BotToken)
