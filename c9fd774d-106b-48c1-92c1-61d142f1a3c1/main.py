import discord, random, time, math
from discord.ext import commands
from PIL import Image 
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = "&")
print("Bot is ready")

member_ID  = []

comList = []
comList_n = []
MM= []

Vote_Count = []

vote = 0

@bot.command()
async def Reset(ctx):
  global comList 
  global comList_n
  global Vote_Count
  global member_ID
  global vote
  global MM

  MM = []
  member_ID  = []
  comList = []
  comList_n = []
  Vote_Count = []
  vote = 0

  await ctx.send(f'The votes have been reset by {ctx.author.mention}!')


@bot.command()
async def Join(ctx, *, args="nothing"):
  global comList 
  global comList_n
  global Vote_Count
  global MM
  
  
  for x in comList:
    
    if(x == ctx.author.id):
      await ctx.send(f'{ctx.author.mention} You can not join twice!')
      return

  for x in comList_n:
    
    if(x == ctx.author.id):
      await ctx.send(f'{ctx.author.mention} You can not join twice!')
     
      return    
  
  
  await ctx.send(f'{ctx.author.mention} Joined the race!')
  MM.append(args)
  Vote_Count.append(0)
  comList_n.append(ctx.author.id)
  comList.append(ctx.author)

  print('\a')
  print("Com list: ", comList_n)
  
  print("Join")

@bot.command()
async def ShowList(ctx):
  global comList 
  global MM

  for x in range(len(comList)):
   await ctx.send(f"{comList[x].mention} joined and said: {MM[x]}!")
    
  
@bot.event
async def on_command_error(ctx, error):
  print("Invalid command")
  print(error)

@bot.event
async def on_command(ctx):
  print("the " + ctx.command.name + " command was invoked")



@bot.command()
async def Vote(ctx, user: discord.Member):
  global member_ID 
  global comList_n 
  global comList
  global Vote_Count
  global vote
  yay = False

  

  for x in member_ID:  
    if(x == ctx.author.id):
      await ctx.send(f'{ctx.author.mention} You can not vote twice!')
      return
   
  for x in range(len(comList_n)):  
    
    if(comList_n[x] == user.id):

      if(comList_n[x] == ctx.author.id):
        await ctx.send(f'{ctx.author.mention}, You cant vote to youself! Dont think about yourself only!')
        return
      else:
        await ctx.send(f"{ctx.author.mention} Succsfuly voted to {user.mention}")
        yay = True
        vote += 1
        Vote_Count[x] += 1


     

  if(yay == False):
    await ctx.send('The persen you voted towrds is not on the list! Type: "&ShowList" to see for who you can vote for!')
    return


  member_ID.append(ctx.author.id)

  print('\a')
  print("voter list: ", member_ID )
  
  print("Voted!")

@bot.command()
async def Check(ctx):
  print("")
  

@bot.command()

async def Winner(ctx):
 
  global member_ID 
  global comList_n 
  global comList
  global Vote_Count
  global vote
  global MM

  biggest = 0
  biggest_ = comList[0]
  biggest__ = []
  MM = []
  draw = False
  for i in range(len(Vote_Count)):
    if(Vote_Count[i] > biggest):
      biggest__.append(comList[i])
      biggest = Vote_Count[i]
      biggest_ = comList[i]
    elif(Vote_Count[i] == biggest):
      biggest__.append(comList[i])
      draw = True

  await ctx.send(f"The voting has ended with {vote} total votes!")

  if(draw == False):

   await ctx.send(f"The winner is {biggest_.mention} with {biggest} votes!")
   await ctx.send("---------------------")
   await ctx.send('The votes have been reset!')
  else:
    await ctx.send(f"It's a draw! Between {biggest__[0].mention} and {biggest__[1].mention} with {biggest} votes each!")
    await ctx.send("---------------------")
    await ctx.send('The votes have been reset!')



  member_ID  = []
  comList = []
  comList_n = []
  Vote_Count = []
 
  vote = 0

keep_alive()
bot.run('Nzk3NzQ1OTY3NTkxMDYzNTYy.X_q81A.z-INJHQncvwfzqNoNUN5VMzHg80')


