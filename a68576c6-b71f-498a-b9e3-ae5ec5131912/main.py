# The id to add bot is BlackJackBot#8047
import discord
import os
import random
from discord.ext import commands
import time

bot = commands.Bot(command_prefix="$")

global total

global thirdDealerCard
global fourthDealerCard
global fifthDealerCard

thirdDealerCard = 0
fourthDealerCard = 0
fifthDealerCard = 0

@bot.event
async def on_ready():
    print("I'm in, type $deal To play a game of Black Jack!")
    print("You can also do $rules")
    #print(total)
    print(bot.user)

@bot.event
async def on_message(message):
  
  if message.content == "$deal":
    await firstCard(message)

  if message.content == "$rules":
    await message.channel.send('1. Both the dealer and player can only have up to five cards in one game \n 2. The dealer must hit if their total is 16 or below \n 3. dealer will stand on 17 or above \n 4. if the dealer has a higher total then you without going over 21 they win and vice versa \n 5. You have 30 seconds to make each desicion \n 6. have fun!')

  if message.author == bot.user:
    return
    
@bot.event
async def firstCard(message):
  global firstPlayerCard
  firstPlayerCard = random.randint(1, 11)
  await message.channel.send("Your card is " + str(firstPlayerCard))
  time.sleep(2)
  await dealerFirstCard(message)
  return firstPlayerCard

@bot.event
async def dealerFirstCard(message):
  global firstDealerCard
  firstDealerCard = random.randint(1, 11)
  await message.channel.send("The dealer's card is " + str(firstDealerCard))
  time.sleep(2)
  await secondCard(message)
  return firstDealerCard

@bot.event
async def secondCard(message):
  global secondPlayerCard
  secondPlayerCard = random.randint(1, 10)
  await message.channel.send("Your second card is " + str(secondPlayerCard))
  time.sleep(2)
  global total
  total = firstPlayerCard + secondPlayerCard
  if total == 21:
    await playerWin(message)
  
  else:
    await dealerSecondCard(message)

@bot.event
async def dealerSecondCard(message):
  global secondDealerCard 
  secondDealerCard = random.randint(1, 11)
  await hitStand(message)
  return dealerSecondCard

@bot.event
async def hitStand(message):
  await message.channel.send("Your total is now " + str(total))
  time.sleep(2)
  await message.channel.send("Would you like to hit or stand?")
  time.sleep(2)
  await message.channel.send("To hit, type: $hit, to stand, type: $stand")

  msg = await bot.wait_for("message", timeout=30)

  if msg.content == "$hit":
    await thirdPlayerCard(message)

  if msg.content == "$stand":
    await revealDealerSecond(message)

@bot.event
async def revealDealerSecond(message):
  await message.channel.send("The dealer's second card is " + str(secondDealerCard))
  time.sleep(2)
  await stand(message)

@bot.event
async def stand(message):
  global dealerTotal
  dealerTotal = firstDealerCard + secondDealerCard 
  await message.channel.send("The dealer's total is " + str(dealerTotal)) 
  time.sleep(2)

  if dealerTotal < 17:
    await dealerThirdCard(message)

  if dealerTotal >= 17:
    await playTree(message)

@bot.event
async def playTree(message):

  if dealerTotal == 21:
    await dealerWin(message)

  if dealerTotal > 21:
    await playerWin(message)

  if dealerTotal >= 17 and dealerTotal > total and dealerTotal <= 21:
    await dealerWin(message)

  if dealerTotal >= 17 and dealerTotal < total and total <= 21:
    await playerWin(message)

  if dealerTotal == total and dealerTotal >= 17:
    await push(message)

@bot.event 
async def thirdPlayerCard(message):
  global thirdPlayerCard
  thirdPlayerCard = random.randint(1, 11)
  await message.channel.send("Your third card is " + str(thirdPlayerCard))
  time.sleep(2)
  total = firstPlayerCard + secondPlayerCard + thirdPlayerCard
  await message.channel.send("Your total is now " + str(total))
  time.sleep(2)

  if total > 21:
    await message.channel.send("You have busted...")
    await dealerWin(message)

  if total == 21:
    await playerWin(message)
  
  if total < 21:
    await thirdCont(message)

  
@bot.event
async def thirdCont(message):
  await message.channel.send("Would you like to hit again?")
  time.sleep(2)
  await message.channel.send("To hit, type: $hit1, to stand, type: $stand")
  
  msg = await bot.wait_for("message", timeout=30)

  if msg.content == "$hit1":
    await fourthPlayerCard(message)

  if msg.content == "$stand":
    await stand(message)
  
@bot.event 
async def fourthPlayerCard(message):
  global fourthPlayerCard
  fourthPlayerCard = random.randint(1, 11)
  await message.channel.send("Your fourth card is " + str(fourthPlayerCard))
  time.sleep(2)
  total = firstPlayerCard + secondPlayerCard + thirdPlayerCard + fourthPlayerCard

  if total > 21:
    await message.channel.send("You have busted...")
    await dealerWin(message)
  
  if total == 21:
    await playerWin(message)

  if total < 21:
    await fourthCont(message)

  @bot.event
  async def fourthCont(message):
    await message.channel.send("Your total is now " + str(total))
    time.sleep(2)
    await message.channel.send("Would you like to hit again?")
    time.sleep(2)
    await message.channel.send("To hit, type: $hit2, to stand, type: $stand")

    msg2 = await bot.wait_for("message", timeout=30)

    if msg2.content == "$hit2":
      await fifthPlayerCard(message)

    if msg2.content == "$stand":
      await stand(message)

@bot.event 
async def fifthPlayerCard(message):
  global fifthPlayerCard
  fifthPlayerCard = random.randint(1, 11)
  await message.channel.send("Your fifth card is " + str(fifthPlayerCard))
  time.sleep(2)
  total = firstPlayerCard + secondPlayerCard + thirdPlayerCard + fourthPlayerCard + fifthPlayerCard
  await message.channel.send("Your total is now " + str(total))
  time.sleep(2)
  await stand(message)
  return fifthPlayerCard

@bot.event
async def dealerThirdCard(message):
  global thirdDealerCard
  thirdDealerCard = random.randint(1, 11)
  await message.channel.send("The dealer's third card is " + str(thirdDealerCard))
  time.sleep(2)
  dealerTotal = firstDealerCard + secondDealerCard + thirdDealerCard
  await message.channel.send("The dealer's total is now " + str(dealerTotal))
  time.sleep(2)
  
  if dealerTotal <= 16:
    await dealerFourthCard(message)

  if dealerTotal > 16:
    await playTree(message)

  if dealerTotal > 21:
    await playerWin(message)

  if dealerTotal == 21:
    await dealerWin(message)
  
@bot.event
async def dealerFourthCard(message):
  global fourthDealerCard
  fourthDealerCard = random.randint(1, 11)
  await message.channel.send("The dealer's fourth card is " + str(fourthDealerCard))
  time.sleep(2)
  dealerTotal = firstDealerCard + secondDealerCard + thirdDealerCard + fourthDealerCard
  await message.channel.send("The dealer's total is now " + str(dealerTotal))
  time.sleep(2)
  
  if dealerTotal <= 16:
    await dealerFifthCard(message)

  if dealerTotal > 16:
    await playTree(message)

  if dealerTotal > 21:
    await playerWin(message)

  if dealerTotal == 21:
    await dealerWin(message)

@bot.event
async def dealerFifthCard(message):
  global fifthDealerCard
  fifthDealerCard = random.randint(1, 11)
  await message.channel.send("The dealer's fifth card is " + str(fifthDealerCard))
  time.sleep(2)
  dealerTotal = firstDealerCard + secondDealerCard + thirdDealerCard + fourthDealerCard + fifthDealerCard
  await message.channel.send("The dealer's total is now " + str(dealerTotal))
  time.sleep(2)

  if dealerTotal < 16:
    await playTree(message) 

  if dealerTotal > 16:
    await playTree(message)

  if dealerTotal > 21:
    await playerWin(message)

  if dealerTotal == 21:
    await dealerWin(message)

@bot.event
async def dealerWin(message):
  await message.channel.send("You have lost...")



@bot.event
async def playerWin(message):
  await message.channel.send("Congrats, you won!")



@bot.event
async def push(message):
  await message.channel.send("You pushed")
 
  







my_secret = os.environ['-LnYuiZWF70BXnxd2zVpQIofN-uDd_Bi']

bot.run(my_secret)
