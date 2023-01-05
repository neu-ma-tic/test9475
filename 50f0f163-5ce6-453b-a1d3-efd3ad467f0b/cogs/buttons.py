
import discord
from discord.ext import commands
import random
from cogs.Economy import get_bank_data, update_bank, open_account







class FunGamesWithButtons(commands.Cog):
    def __init__(self, client):
      self.client=client

    @commands.command(aliases=['rockpapersissors'])
    async def rps(self,ctx,user:discord.Member=None,amount:int=None):
      if amount is None and user is None:
        response = ['Paper','Scissors','Rock']
        comp = random.choice(response)

        win = discord.Embed(title=f"{ctx.author.display_name}, You Won!",description=f'Status: **You have won**! The bot had chosen {comp}',color=discord.Color.random())
        lost = discord.Embed(title=f'{ctx.author.display_name}, You Lost!',description=f'Status: **You have lost!** Bot had chosen {comp}',color=discord.Color.random())
        out = discord.Embed(title=f"{ctx.author.display_name}, You didn't click on time ;-;",description='Status: **Timed out!** Click faster next time mate',color=discord.Color.random())
        yet = discord.Embed(title=f"{ctx.author.display_name}'s Rock Paper Scissors game!",description='Status: **You havent clicked on any button yet**',color=discord.Color.random())
        tie = discord.Embed(title=f"{ctx.author.display_name}, It's a tie!",description='Status: You have tied with the bot',color=discord.Color.random())

        class MyView(discord.ui.View):
          @discord.ui.button(emoji="<:rock:894796236396331008>", label="Rock", style=discord.ButtonStyle.primary)
          async def button_callback(self, button, interaction):
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)

          @discord.ui.button(emoji="🧻",label="Paper", style=discord.ButtonStyle.primary)
          async def second_button_callback(self, button, interaction):
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)
          @discord.ui.button(emoji="✂️",label="Scissors", style=discord.ButtonStyle.primary)
          async def third_button_callback(self, button, interaction):
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)
        view = MyView()
        await ctx.send(content="** **",embed=yet,view=view)
      elif amount != None and user == None:
        response = ['Paper','Scissors','Rock']
        comp = random.choice(response)

        win = discord.Embed(title=f"{ctx.author.display_name}, You Won!",description=f'Status: **You have won**! The bot had chosen {comp}',color=discord.Color.random())
        lost = discord.Embed(title=f'{ctx.author.display_name}, You Lost!',description=f'Status: **You have lost!** Bot had chosen {comp}',color=discord.Color.random())
        out = discord.Embed(title=f"{ctx.author.display_name}, You didn't click on time ;-;",description='Status: **Timed out!** Click faster next time mate',color=discord.Color.random())
        yet = discord.Embed(title=f"{ctx.author.display_name}'s Rock Paper Scissors game!",description='Status: **You havent clicked on any button yet**',color=discord.Color.random())
        tie = discord.Embed(title=f"{ctx.author.display_name}, It's a tie!",description='Status: You have tied with the bot',color=discord.Color.random())

        class MyView(discord.ui.View):
          @discord.ui.button(emoji="<:rock:894796236396331008>", label="Rock", style=discord.ButtonStyle.primary)
          async def button_callback(self, button, interaction):
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)

          @discord.ui.button(emoji="🧻",label="Paper", style=discord.ButtonStyle.primary)
          async def second_button_callback(self, button, interaction):
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)
          @discord.ui.button(emoji="✂️",label="Scissors", style=discord.ButtonStyle.primary)
          async def third_button_callback(self, button, interaction):
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)
        view = MyView()
        await ctx.send(content="** **",embed=yet,view=view)
      else:
        response = ['Paper','Scissors','Rock']
        comp = random.choice(response)

        win = discord.Embed(title=f"{ctx.author.display_name}, You Won!",description=f'Status: **You have won**! The bot had chosen {comp}',color=discord.Color.random())
        lost = discord.Embed(title=f'{ctx.author.display_name}, You Lost!',description=f'Status: **You have lost!** Bot had chosen {comp}',color=discord.Color.random())
        out = discord.Embed(title=f"{ctx.author.display_name}, You didn't click on time ;-;",description='Status: **Timed out!** Click faster next time mate',color=discord.Color.random())
        yet = discord.Embed(title=f"{ctx.author.display_name}'s Rock Paper Scissors game!",description='Status: **You havent clicked on any button yet**',color=discord.Color.random())
        tie = discord.Embed(title=f"{ctx.author.display_name}, It's a tie!",description='Status: You have tied with the bot',color=discord.Color.random())

        class MyView(discord.ui.View):
          @discord.ui.button(emoji="<:rock:894796236396331008>", label="Rock", style=discord.ButtonStyle.primary)
          async def button_callback(self, button, interaction):
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
              await open_rank(ctx.author)
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)

          @discord.ui.button(emoji="🧻",label="Paper", style=discord.ButtonStyle.primary)
          async def second_button_callback(self, button, interaction):
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)
          @discord.ui.button(emoji="✂️",label="Scissors", style=discord.ButtonStyle.primary)
          async def third_button_callback(self, button, interaction):
            if comp == response[2]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=lost,view=self)
            if comp == response[0]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=win,view=self)
            if comp == response[1]:
              for child in self.children:
                  child.disabled = True
              await interaction.response.edit_message(embed=tie,view=self)
        view = MyView()
        await ctx.send(content="** **",embed=yet,view=view)
      



    @commands.command()
    async def fight(self, ctx, opponent:discord.Member = None):
        health = {}
        turn = {}
        components = discord.ui.View()
        punch = discord.ui.Button(label = 'Punch', style = discord.ButtonStyle.blurple, custom_id = '30')
        kick = discord.ui.Button(label = 'Kick', style = discord.ButtonStyle.blurple, custom_id = '40')
        heal = discord.ui.Button(label = 'Heal', style = discord.ButtonStyle.green, custom_id = 'heal')
        end = discord.ui.Button(label = 'End', style = discord.ButtonStyle.red, custom_id = 'end')
        components.add_item(punch)
        components.add_item(kick)
        components.add_item(heal)
        components.add_item(end)
        players = [ctx.author, opponent]
        health[str(ctx.author.id)] = 100
        health[str(opponent.id)] = 100
        first_turn = random.choice(players)
        players.remove(first_turn)
        turn[str(first_turn.id)] = True
        turn[str(players[0].id)] = False
        em = discord.Embed(title = '⚔ Battle', description = 'Click on one of the buttons below!')
        em.add_field(name = f'{ctx.author} Health:', value = str(health[str(ctx.author.id)]) + ' HP')
        em.add_field(name = f'{opponent} Health:', value = str(health[str(opponent.id)]) + ' HP')
        em.color = discord.Colour.red()
        msg = await ctx.send(f'{first_turn.mention}', embed = em, view = components)
        def check(interaction):
            return interaction.message == msg
        while True:

            interaction = await self.client.wait_for('interaction',check = check, timeout = 30)

            if not turn[str(interaction.user.id)]:
                await interaction.response.send_message('It is not your turn.')
                await msg.edit(view = components)



def setup(client):
  client.add_cog(FunGamesWithButtons(client))