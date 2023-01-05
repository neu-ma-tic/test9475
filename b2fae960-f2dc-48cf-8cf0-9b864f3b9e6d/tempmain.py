import discord
import os
import hashlib
import json
from discord.ext import commands
from datetime import datetime
import random

class Blockchain():
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.blockCount = 0
        self.transactionCount = 0
        self.transactionString = ""
        self.blockString = ""
    
    def userTransactionHistory(self, username):
      string = ""
      
      for transaction in self.pendingTransactions:
        if transaction.sender == username or transaction.receiver == username:
          string += transaction.displayTransactions() + "\n"
      return string



    def addTransaction(self, sender, receiver, amount):
        self.pendingTransactions.append(Transaction(sender, receiver, amount))
        self.transactionString = self.pendingTransactions[-1].displayTransactions()
        self.transactionCount += 1
        self.blockString = ""

        if self.transactionCount % 3 == 0:
            self.addBlock()
            #self.pendingTransactions.clear()
            #self.transactionCount = 0
        
    def addBlock(self):
        if self.blockCount == 0:
            genesisBlock = Block("0", self.pendingTransactions[0:self.transactionCount], self.blockCount)
            self.chain.append(genesisBlock)
            print(self.displayOneBlock())
            self.blockCount += 1
        else:
            newBlock = Block(self.getPrevBlockHash(), self.pendingTransactions[self.transactionCount-3:], self.blockCount)
            self.chain.append(newBlock)
            print(self.displayOneBlock())
            self.blockCount += 1

    def getPrevBlockHash(self):
        return self.chain[self.blockCount-1].hash

    def displayOneBlock(self):
        block = self.chain[self.blockCount]
        string = f"Block #{self.blockCount}\n\n"
        string += f"\tTime created: {block.time}\n" 
        string += f"\tPrevious Block Hash: {block.prevHash}\n"
        string += f"\tCurrent Block Hash: {block.hash}\n\n" 
        

        #transactionJSON = []
        for transaction in block.transactions:
            # temp = {
            #     "sender": transaction.sender
            # }
            # transactionJSON.append(temp)
            # string += f"Transaction ID: {transaction.hash}\n"
            # string += f"\Time: {self.time}\n"
            # string += f"\tSender: {transaction.sender}\n"
            # string += f"\tReceiver: {transaction.receiver}\n"
            # string += f"\tAmount: {transaction.amount}\n\n"
            string += transaction.displayTransactions()
            
        self.blockString = string


class Block():
    def __init__(self, prevHash, transactions, index):
        self.prevHash = prevHash
        self.transactions = transactions
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.index = index
        self.hash = self.calculateHash()

    def calculateHash(self):
        transactionString = list(map(str, self.transactions))
        hashString = self.prevHash + ("").join(transactionString) + str(self.index) + str(self.time)
        #return hashlib.sha256(hashString.encode().hexdigest())
        return hashlib.sha256(json.dumps(hashString).encode('utf-8')).hexdigest()

class Transaction():
    def __init__(self, sender, receiver, amount):
        self.sender = sender 
        self.receiver= receiver
        self.amount = amount
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.hash = self.calculateHash()
        

    def calculateHash(self):
        hashString = self.sender + self.receiver + str(self.amount) + str(self.time)
        #return hashlib.sha256(hashString.encode('utf-8').hexdigest())
        return hashlib.sha256(json.dumps(hashString).encode('utf-8')).hexdigest()
    
    def displayTransactions(self):
      string = f"Transaction ID: {self.hash}\n"
      string += f"\tTime: {self.time}\n"
      string += f"\tSender: {self.sender}\n"
      string += f"\tReceiver: {self.receiver}\n"
      string += f"\tAmount: {self.amount}\n"

      return string
#_________________________________________________________Discord____________________________________________________________________________________________

users = {}
client = commands.Bot(command_prefix = '!')
coins = Blockchain()

botCom = client.get_channel(830546871189110834)
botRead = client.get_channel(830624577624473600)
@client.event
async def on_ready():
  print('Bot is ready')
  '''
  embed = discord.Embed(title = "BC Bot Commands", description = "", color = 0x00ff00)
  embed.add_field(name = "!pay @mention [amount] :", value = "Pay discord user [amount]", inline = False)
  embed.add_field(name = "!balance :", value = "Displays balance of user", inline = False)
  embed.add_field(name = "!history :", value = "Displays all transactions of user", inline = False)
  embed.add_field(name = "!hello:", value = "Greets back", inline = False)
  await botCom.send(embed=embed)
 
  embedB = discord.Embed(name = "BC Bot", description = "", color = 0x00ff00)
  embedB.add_field(name = "BC Bot is a discord bot that implements block chain to simulate 'fake' cryptocurrency, which can be interacted by and between Discord users")
  await botRead.send(embed=embedB)
  '''

@client.command()
async def playgg(ctx):
      if ctx.channel.id == 830660169208692736:
          channelG = client.get_channel(830660169208692736)
          await channelG.send("Choose a number between 1-10. Enter numerical values only. \nYou have **multiple chances** to try! **:)**")

         # generates a random number and turns it into a string
          number1 = random.randint(1,10)        
          number2 = str(number1)
          guess = await client.wait_for_message(channel=channelG)
          if guess == number2:
            await channelG.send(f'Correct answer {ctx.message.author.name}, you were awarded 10 gold')
          else:
            await channelG.send(f'Incorrect answer {ctx.message.author.name}, 5 coins have been taken from you')

          # def check(m):
          #     return m.content == number2 and m.channel == channelG 
          
          # msg = await client.wait_for('message', check=check) #waits for the check function to return true
          # if ctx.message.author.name not in users:
          #   users[ctx.message.author.name] = 110
          # else:
          #   users[ctx.message.author.name] += 10
          # await channelG.send(f'Correct answer {ctx.message.author.name}, you were awarded 10 gold'.format(msg))

      else:
       await ctx.send("Go to **Guessing Game** channel to play")


@client.command()
async def rps(ctx):
  if ctx.channel.id == 830660298440572958:
    channelR = client.get_channel(830660298440572958)
    game_list = ['Rock', 'Paper', 'Scissors']
    computer = 0
    command = 0
    computer_choice = random.choice(game_list)
    await channelR.send("Input Rock, Paper, or Scissors")
    def check(command):
      return command.author == ctx.author and command.channel == ctx.channel
      
    command = await client.wait_for('message', check=check)

    if ctx.message.author.name not in users:
        users[ctx.message.author.name] = 100
        
    if command.content == computer_choice:
        await channelR.send("Tie")
    elif command.content == 'Rock':
        if computer_choice == 'Scissors':
          await channelR.send("" + command.content + " (You) verses " + computer_choice + " (Computer).\n\n**Player won!** You gained 10 gold.")
          users[ctx.message.author.name] += 10
        else:
          await channelR.send("" + command.content + " (You) verses " + computer_choice + " (Computer).\n\n**Computer won!**.")
          users[ctx.message.author.name] -= 10
          await channelR.send(f"{ctx.message.author.name} has lost 10 coins")
    elif command.content == 'Paper':
        if command.content == 'Rock':
          await channelR.send("" + command.content + " (You) verses " + computer_choice + " (Computer).\n\n**Player won!** You gained 10 gold.")
          users[ctx.message.author.name] += 10
        else:
          await channelR.send("" + command.content + " (You) verses " + computer_choice + " (Computer).\n\n**Computer won!**.")
          users[ctx.message.author.name] -= 10
          await channelR.send(f"{ctx.message.author.name} has lost 10 coins")
    elif command.content == 'Scissors':
        if computer_choice == 'Paper':
          await channelR.send("" + command.content + " (You) verses " + computer_choice + " (Computer).\n\n**Player won!** You gained 10 gold.")
          users[ctx.message.author.name] += 10
        else:
          await channelR.send("" + command.content + " (You) verses " + computer_choice + " (Computer).\n\n**Computer won!**.")
          users[ctx.message.author.name] -= 10
          await channelR.send(f"{ctx.message.author.name} has lost 10 coins")
    else:
        await channelR.send("Incorrect input, input command again to play.")
  else:
    await ctx.send("Go to **Rock Paper Scissors** channel to play")


@client.command()
async def pay(ctx, member: discord.Member, a: int): # pay other members of the discord 'x' amount of blocks
  
  channel = client.get_channel(830546793539305484)
  channel2 = client.get_channel(830552658954682419)

  if (member.name != ctx.message.author.name): # if the user's name isn't the mentioned name
    if ctx.message.author.name not in users:
      users[ctx.message.author.name] = 100
      
    if member.name not in users:
      users[member.name] = 100 + a
    else:
      users[member.name] += a
      
    if users[ctx.message.author.name] < a:
      await ctx.send('Insufficient funds')
    else:
      users[ctx.message.author.name] -= a
      coins.addTransaction(ctx.message.author.name, member.name, a)

      await channel.send("```" + coins.transactionString + "```") # transaction channel
      
      if coins.blockString != "":
        # block channel
        await channel2.send("```" + coins.blockString + "```")
        
      await ctx.send(f'Successful Transaction, you now have {users[ctx.message.author.name]}')
            
  else:
    await ctx.send('You can not send coins to yourself')

@client.command()
async def balance(ctx): # show balance of user 
    if ctx.message.author.name not in users:
      users[ctx.message.author.name] = 100
      await ctx.send(f'{ctx.message.author.name} now has 100 amount of coins')
    else:
      await ctx.send(f'{ctx.message.author.name} has {users[ctx.message.author.name]} amount of coins')

@client.command()
async def hello(ctx): # bot says hello
  await ctx.send('Hello.')

@client.command()
async def history(ctx):
  try:
    if ctx.message.author.name not in users:
      users[ctx.message.author.name] = 100
    else:
      await ctx.send(coins.userTransactionHistory(ctx.message.author.name))
  except:
    await ctx.send(f"**{ctx.message.author.name}** has no transaction history!")
      
@client.command()
async def commands(ctx):
  embed = discord.Embed(title = "BC Bot Commands", description = "", color = 0x00ff00)
  embed.add_field(name = "!pay @mention [amount] :", value = "Pay discord user [amount]", inline = False)
  embed.add_field(name = "!balance :", value = "Displays balance of user", inline = False)
  embed.add_field(name = "!history :", value = "Displays all transactions of user", inline = False)
  embed.add_field(name = "!playgg :", value = "Play a guessing game to win gold", inline = False)
  embed.add_field(name = "!rps :", value = "Play Rock, Paper, Scissors to win gold", inline = False)
  embed.add_field(name = "!hello:", value = "Greets back", inline = False)
  await ctx.send(embed=embed)


client.run(os.getenv('TOKEN'))