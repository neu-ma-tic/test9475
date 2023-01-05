import discord
import os
import requests
import json
import datetime
import random
from replit import db

global Happy
global Sad
global Angry
global Cheer


client = discord.Client()

Sad = ["buồn","Buồn" "trầm cảm","tramkam",":<","=((","=(((","=((((("]

Angry = ["Cọc","cọk","cáu","Cáu","Tức","tứk",")):<","):<"]

Cheer = ["Dzui lơn bạn êi","Dzui lơn đê cóa j đou phải buồn =))","Dzui lơn =))",  ]

Happy = ["cọc quời =))","Đừng có cọc mờ","Bình tõm nèo =))""Bình tõm đê =))","Cọc là mink ban ad =))",            ]

H = ["Hào ","hào","bot","@Haos"]

Calls = [" Sao ???", "Hể ?? =))","Đợi tí nó rep cho , chắc nó bận  , đợi đi",   ]






tday = datetime.date.today()
tdel = datetime.timedelta (days=7)
wfn = (tdel + tday)
awago = (tday - tdel)
dt = datetime.datetime.today ()
t = (dt.time())

def get_quote():
  response = requests.get ('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0] ['q'] +"        " "-" + json_data [0] ['a'] +  "-"
  return(quote)


def update_Cheer(Cheer_message):
  if "Cheer" in db.keys():
    Cheers = db["Cheer"]
    Cheers.append(Cheer_message)
    db["Cheer"] = Cheer
  else:
    db["Cheer"] = [Cheer_message]

def delete_Cheer(index):
  Cheer = db["Cheer"]
  if len(Cheer) > index:
    del Cheer[index]
  db["Cheer"] = Cheer


def update_Sad(Sad_message):
  if "Sad" in db.keys():
    Sad = db["Sad"]
    Sad.append(Sad_message)
    db["Sad"] = Sad
  else:
    db["Sad"] = [Sad_message]

def delete_Sad(index):
  Sad = db["Sad"]
  if len(Sad) > index:
    del Sad[index]
  db["Sad"] = Sad

def update_Happy(Happy_message): 
  
  if "Happy" in db.keys():
    Happy + db["Happy"]
    Happy.append(Happy_message)
    db["Happy"] = Happy

  else:
    db["Happy"] = [Happy_message]

def delete_Happy(index):
  Happy = db["Happy"]
  if len(Happy) > index:
    del Happy[index]
  db["Happy"] = Happy

def update_Angry(Angry_message):
  global Angry
  if "Angry" in db.keys():
    Angry + db["Angry"]
    Angry.append(Angry_message)
    db["Angry"] = Angry
  else:
    db["Angry"] = [Angry_message]

def delete_Angry(index):
  Angry = db["Angry"]
  if len(Angry) > index:
    del Angry[index]
  db["Angry"] = Angry

def update_Call(Call_message):
  global Calls
  if "Calls" in db.keys():
    Calls + db["Calls"]
    Calls.append(Call_message)
    db["Calls"] = Calls
  else:
    db["Calls"] = (Call_message)

def delete_Call(index):
  Calls = db["Calls"]
  if len(Calls) > index:
    del Calls[index]
  db["Calls"] = Calls

@client.event
async def on_ready():
  print ('we have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    Sad = ["buồn","Buồn" "trầm cảm","tramkam",":<","=((","=(((","=((((("]

    Angry = ["Cọc","cọk","cáu","Cáu","Tức","tứk",")):<","):<"]

    Cheer = ["Dzui lơn bạn êi","Dzui lơn đê cóa j đou phải buồn =))","Dzui lơn =))",  ]

    Happy = ["cọc quời =))","Đừng có cọc mờ","Bình tõm nèo =))""Bình tõm đê =))","Cọc là mink ban ad =))",            ]

    H = ["Hào ","hào","bot","@Haos"]

    Calls = [" Seo ???", "Hể ?? =))","Đợi tí nó rep cho , chắc nó bận ad , đợi đi",   ]

    msg = message.content
    
  if any (word in msg for word in Angry ):
    await message.channel.send(random.choice(Happy))
     

  if any (word in msg for word in Sad):
    await message.channel.send(random.choice(options))
    
  if any (word in msg for word in H ):
    await message.channel.send(random.choice(Calls))

    if msg.startswith(".newCh"):
      Cheer_message = msg.split(".newCh ",1)[1]
      update_Cheer(Cheer_message)
      await message.channel.send("New cheer added")
    
    if msg.startswith(".delCh"):
      Cheer = []
      if "Cheer" in db.keys():
        index = int (msg.split(".delCh",1)[1])
        delete_Cheer(index)
        Cheer = db["Cheer"]
      await message.channel.send(Cheer)
    
    
    if msg.startswith(".newsad"):
      Sad_message = msg.split(".newsad ",1)[1]
      update_Sad(Sad_message)
      await message.channel.send("New sad added")
    
    if msg.startswith(".delsad"):
      Sad = []
      if "Sad" in db.keys():
        index = int (msg.split(".delsad",1)[1])
        delete_Cheer(index)
        Sad = db["Sad"]
      await message.channel.send(Sad)

    if msg.startswith(".newh"):
      Happy_message = msg.split(".newh ",1)[1]
      update_Happy(Happy_message)
      await message.channel.send("New Happy added")
    
    if msg.startswith(".delh"):
      Happy = []
      if "Happy" in db.keys():
        index = int (msg.split(".delh",1)[1])
        delete_Happy(index)
        Happy = db["Happy"]
      await message.channel.send(Happy)

    if msg.startswith(".newa"):
        Angry_message = msg.split(".newa ",1)[1]
        update_Angry(Angry_message)
        await message.channel.send("New Angry word added")
    
    if msg.startswith(".dela"):
        Angry = []
        if "Angry" in db.keys():
          index = int (msg.split(".dela",1)[1])
          delete_Angry(index)
          Angry = db["Angry"]
    await message.channel.send(Angry)
      
    if msg.startswith(".newMe"):
        Cheer_message = msg.split(".newMe ",1)[1]
        update_Call(Call_message)
        await message.channel.send("New call added")
    
    if msg.startswith(".delMe"):
      Calls = []
      if "Call" in db.keys():
        index = int (msg.split(".delMe",1)[1])
        delete_Call(index)
        Calls = db["Calls"]
      await message.channel.send(Calls)


    if message.content == ('.supa inspire'):
      quote = get_quote()
      await message.channel.send(quote)

    if message.content == ('.date'):
      await message.channel.send (tday)
    
    if message.content == ('.wfn'):
      await message.channel.send (wfn)

    if message.content == ('.awago'):
      await message.channel.send (awago)

    if message.content == ('.dtime'):
      await message.channel.send (dt)
    if message.content == ('.time'):
      await message.channel.send (t)
    
async def on_message(message):
  if message.author == client.user:
      return
       
  Angrys = Angry
  if "Angry" in db.keys():
    Angrys = Angrys + db["Angry"]

  options = Cheer
  if "Cheer" in db.keys():
     options = options + db["Cheer"]
    



  msg = message.content
  if any (word in msg for word in Angry ):
    await message.channel.send(random.choice(Happy))
     

  if any (word in msg for word in Sad):
    await message.channel.send(random.choice(options))
    
  if any (word in msg for word in H ):
    await message.channel.send(random.choice(Calls))

    if msg.startswith(".newCh"):
      Cheer_message = msg.split(".newCh ",1)[1]
      update_Cheer(Cheer_message)
      await message.channel.send("New cheer added")
    
    if msg.startswith(".delCh"):
      Cheer = []
      if "Cheer" in db.keys():
        index = int (msg.split(".delCh",1)[1])
        delete_Cheer(index)
        Cheer = db["Cheer"]
      await message.channel.send(Cheer)
    
    
    if msg.startswith(".newsad"):
      Sad_message = msg.split(".newsad ",1)[1]
      update_Sad(Sad_message)
      await message.channel.send("New sad added")
    
    if msg.startswith(".delsad"):
      Sad = []
      if "Sad" in db.keys():
        index = int (msg.split(".delsad",1)[1])
        delete_Cheer(index)
        Sad = db["Sad"]
      await message.channel.send(Sad)

    if msg.startswith(".newh"):
      Happy_message = msg.split(".newh ",1)[1]
      update_Happy(Happy_message)
      await message.channel.send("New Happy added")
    
    if msg.startswith(".delh"):
      Happy = []
      if "Happy" in db.keys():
        index = int (msg.split(".delh",1)[1])
        delete_Happy(index)
        Happy = db["Happy"]
      await message.channel.send(Happy)

    if msg.startswith(".newa"):
        Angry_message = msg.split(".newa ",1)[1]
        update_Angry(Angry_message)
        await message.channel.send("New Angry word added")
    
    if msg.startswith(".dela"):
        Angry = []
        if "Angry" in db.keys():
          index = int (msg.split(".dela",1)[1])
          delete_Angry(index)
          Angry = db["Angry"]
    await message.channel.send(Angry)
      
    if msg.startswith(".newMe"):
        Cheer_message = msg.split(".newMe ",1)[1]
        update_Call(Call_message)
        await message.channel.send("New call added")
    
    if msg.startswith(".delMe"):
      Calls = []
      if "Call" in db.keys():
        index = int (msg.split(".delMe",1)[1])
        delete_Call(index)
        Calls = db["Calls"]
      await message.channel.send(Calls)




client.run  (os.environ['token'])
keys = db.keys()


