import discord
from discord.ext import commands
import random
from discord.ui import Button,View
from cogs.Economy import open_account, get_bank_data,update_bank

class Games(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['tod','t-o-d'])
  async def truth_or_dare(self,ctx,user:discord.Member=None):
    if user is None:
      truth = Button(label="Truth",style=discord.ButtonStyle.green,emoji="<:truth:931783760477818920>")
      dare = Button(label="Dare",style=discord.ButtonStyle.danger,emoji="<:dare:931785433023643719>")
      embed = discord.Embed(title="Welcome to the game of Truth Or Dare!",description="Please choose truth or dare, choosing truth will return a question, and choosing dare will give you a dare <:truthordare:931783572539461662>",color=discord.Color.random())
      embed.set_footer(text="Truth or Dare?",icon_url="https://cdn.discordapp.com/attachments/849560726833987614/883566968496594974/494229933078478858.gif")
      view= View()
      view.add_item(truth)
      view.add_item(dare)
      await ctx.send(embed=embed,view=view)

    

  @commands.command(aliases=['8ball', '8b','magic8ball','magiceightball','eightball'])
  async def _8ball(self,ctx, *, question):
    reponses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(reponses)}')
    
  @commands.command(name='die', help='This command returns a random last words')
  async def die(self,ctx):
      responses = [
          'why have you brought my short life to an end',
          'i could have done so much more', 'i have a family, kill them instead'
      ]
      await ctx.send(random.choice(responses))
  @commands.command()
  async def gamble(self,ctx,amount: int=None):
    users = await get_bank_data()
    await open_account(ctx.author)
    if amount is None:
      choice = random.randint(1,6)
    
      dice_choice= random.randint(1,6)
      if choice > dice_choice:
        embed = discord.Embed(title = f":white_check_mark: You won! The bot program chose the number **{dice_choice}**",color=discord.Color.random())
        embed.set_footer(text=f"Dice rolled by {ctx.author.name}",icon_url = ctx.author.display_avatar)

        await ctx.send(embed=embed)
      elif choice == dice_choice:
        embed = discord.Embed(title = f"It was a tie! The bot program chose the number **{dice_choice}**",color=discord.Color.random())
        embed.set_footer(text=f"Dice rolled by {ctx.author.name}",icon_url = ctx.author.display_avatar)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title = f"<:wrong:892315645708996618> You lost :( The bot program chose the number **{dice_choice}**",color=discord.Color.random())
        embed.set_footer(text=f"Dice rolled by {ctx.author.name}",icon_url = ctx.author.display_avatar)
        await ctx.send(embed=embed)
    
    elif users[str(ctx.author.id)]["wallet"] < amount:
      await open_account(ctx.author)
      await ctx.send("<:bruh:887896562972389446> you don't even have that much money")
      await ctx.send("https://tenor.com/view/touchdown-bruh-really-gif-12484222")

    else:
      choice = random.randint(1,100)
    
      dice_choice= random.randint(1,100)
      if choice > dice_choice:
        embed = discord.Embed(title = f":white_check_mark: You won! The bot program chose the number **{dice_choice}**",description=f"You chose {choice},\nyou also won {amount}!!!!",color=discord.Color.random())
        embed.set_footer(text=f"Dice rolled by {ctx.author.name}",icon_url = ctx.author.display_avatar)
        users = await get_bank_data()
        await open_account(ctx.author)
        await update_bank(ctx.author,amount)
        await ctx.send(embed=embed)
      elif choice == dice_choice:
        embed = discord.Embed(title = f"It was a tie! The bot program chose the number **{dice_choice}**",description="You chose {choice}, You didn't lose anything, \nbut didn't win anything either <:bruh:887896562972389446>",color=discord.Color.random())
        embed.set_footer(text=f"Dice rolled by {ctx.author.name}",icon_url = ctx.author.display_avatar)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title = f"<:wrong:892315645708996618> You lost :( The bot program chose the number **{dice_choice}**",description=f'You chose {choice},\nyou also just lost {amount} <:oof:893037198323097680>',color=discord.Color.random())
        embed.set_footer(text=f"Dice rolled by {ctx.author.name}",icon_url = ctx.author.display_avatar)
        await ctx.send(embed=embed)
        users = await get_bank_data()
        await open_account(ctx.author)
        await update_bank(ctx.author,-amount)
        await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Games(client))

