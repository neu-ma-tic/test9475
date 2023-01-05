import os, discord, random, time
from replit import db
from discord.ext import commands
from keep_alive import keep_alive
import mathgame

client = discord.Client()
 
def flagSwitch(flag):
  newFlag = not flag
  return newFlag


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == ('$hello'):
    await message.channel.send('hello!')

  if message.content == ('$invite'):
    await message.channel.send('<https://discord.com/api/oauth2/authorize?client_id=836275304963375114&permissions=8&scope=bot>')  
  
  if message.content == ('$test'):
    mathgame.game()
    num1 = mathgame
    await message.channel.send(num1)
    await message.channel.send(num1)
    await message.channel.send(num1)
    await message.channel.send(num1)


  if message.content == ('$mathgame'):
    flag = True
    while flag == True:
      timeElapsed = 0
      startTime = time.time()
      num1 = random.randint(0,21)
      num2 = random.randint(0,21)
      answer = num1 * num2
      await message.channel.send("What is " + str(num1) + " times " + str(num2) + " ?")

      while timeElapsed < 10:
        if message.content == str(answer):
          await message.channel.send(message.author + "is correct!")  #this part doesn't work
          timeElapsed = 100
        if message.content == ('$quit'): #this doesn't work either, not sure what to do
          flagSwitch(flag)
          await message.channel.send(flag)
        timeElapsed = time.time() - startTime
#       await message.channel.send(timeElapsed)

      else: 
        await message.channel.send("Sorry but you've ran out of time.")
      
    await message.channel.send("The game has ended.")
  

keep_alive() 
client.run(os.environ['TOKEN'])




   # channel = message.channel
  

  #  def check(m):
   #   return m.content == str(answer) and m.channel == channel
    #try: 
     # if message.content == ('$quit'):
       # print('hi')
       # flag = False
  
      #msg = await client.wait_for('message', #check=check, timeout = 10.0)

 #   except asyncio.TimeoutError:
  #    await message.channel.send("Sorry but you've ran out of time.")
#    else:  
  #    await message.channel.send(" {.author} is correct!".format(msg))
    
  