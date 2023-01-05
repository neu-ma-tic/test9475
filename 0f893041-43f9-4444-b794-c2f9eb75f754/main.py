import discord 
import os 
from random import randrange
import requests 
import json
from replit import db


client = discord.Client()

 
@client.event
async def on_ready(): 
  print("We have logged in as {0.user}"
  .format(client))

  users = ["nva#7465", "ngphlinh#1205", "tialuadien2003#8485", "Bích Ngọc#8534", "ChoiChoi#0908"]

  text = ["Nói ít thôi", "Câm mồm vào", "Trật tự", "Im mẹ mồm đi", "T vả vỡ mồm m đấy", "m bị ngu", "đần độn", "t kick m luôn đấy"]

  badSentences = ["Bị đao", "Ngu vcl", "Con gà", "Kém", "Thằng này đần vl"]

  userHurryUp = ["ĐÂU R", "ĐÂU RỒI", "BỚP THẾ", "LÊN ĐÊ", "LÊN", "NHANH", "NHANH NHẸN", "NHANH NHẸN LÊN", "BỚP", "BOP", "BOP THE", "BỚP VCL", "LE ME", "LỀ MỀ", "LỀ MỀ VCL", "LAU LA"]

  hurryUp = ["Lề mề vcl", "Nhanh cme lên nào", "lâu la lề mề nghỉ mẹ đê"]

  contentBngoc = ["Chơi trc đê không cần chờ", "Bị ngu"]

  callBngoc = ["BNGOC DAU", "BAN M DAU", "B M DAU"]

  
  # bot_speak = True



  @client.event
  async def on_message(message):  
    if message.author == client.user: 
      return 

    

    # if str(message.author) == "Vuanhngo#6164":
    #   if message.content == ("/stop"):
    #     bot_speak = False
    #     await message.channel.send("Stopped")
    #   elif message.content == ("/cont"): 
    #     await message.channel.send("Started")
    #     bot_speak = True
      

    # if(bot_speak == True): 
    #action to list of users 
    for username in users: 
      if str(message.author) == username: 
        index = randrange(len(text))
        speak = text[index]
        await message.channel.send(speak)
      
    content = message.content.upper()

    if content == ("TRẦN ĐỨC ANH") or content == ("TRAN DUC ANH"):
      speak2 = badSentences[randrange(len(badSentences))]
      await message.channel.send(speak2)

    
    # for i in callBngoc: 
    #   if content == i: 
    #     speak4 = contentBngoc[randrange(len(contentBngoc))]
    #     await message.channel.send(speak4)

    # for e in callBngoc: 
    #   if e in message.content.upper():
    #     speak4 = contentBngoc[randrange(len(contentBngoc))]
    #     await message.channel.send(speak4)

    #Speed up 
    hurry = False 

    for myCommand in userHurryUp: 
      if myCommand in message.content.upper(): 
        hurry = True 

    if(hurry == True): 
      speak3 = hurryUp[(randrange(len(hurryUp)))]
      await message.channel.send(speak3)
      hurry = False 

    if client.user.mentioned_in(message):
        await message.channel.send("Gọi cái đầu puoi gi ? ")
      
    # if message.content.startswith('/new'): 
    #   cursing = message.splits("/new ",1)[1]
    #   update_cursingwords(cursing)
    #   await message.channel.send("Updated")
client.run("ODk1NTE4ODAzMzYwOTA3MzE0.YV5u4A.ViMpPTQCMo4_RfdRu0QNgUy9hUc") 
