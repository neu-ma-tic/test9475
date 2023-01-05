import discord
from discord.ext import commands
from utils.prefix import sdprefix


class help(commands.Cog):
  def __init__(self,client):
    self.client = client
  

  @commands.command()
  async def mhelp(self,ctx, topic=None):
    if topic==None:
      embed = discord.Embed(title='<:check:892315763581546527> Bot Program Help Commands',description=f'The prefix on this server is "{sdprefix(self.client,ctx.message)}"',color=discord.Color.random())
      embed.add_field(name='<:utilities:899482350117847040> Utility',value=f'`{sdprefix(self.client,ctx.message)}help utility`\nSome useful utilities & \ncommands')
      embed.add_field(name='<:moderation:893014872932089867> Moderation',value=f'`{sdprefix(self.client,ctx.message)}help moderation`\n Userful server moderation commands')
      embed.add_field(name=':video_game: Games',value=f"`{sdprefix(self.client,ctx.message)}help games`\nSome fun game\n commands for ou\nto play")
      embed.add_field(name='<:economy:894346237157998612> Economy',value=f"`{sdprefix(self.client,ctx.message)}help economy`\nA fun economy system\nto play with")
      embed.add_field(name=":musical_note: Music",value=f"`{sdprefix(self.client,ctx.message)}help music`\nPlay music in discord!")
      embed.add_field(name="<:command_block:894349809027252244> Misc",value=f"`{sdprefix(self.client,ctx.message)}help misc`\nSome more useful commands")
      embed.add_field(name="<:anime:899482117082337300> Anime",value=f"`{sdprefix(self.client,ctx.message)}help anime`\nFun anime related\ncommands")
      embed.add_field(name=":superhero: Roleplay",value=f"`{sdprefix(self.client,ctx.message)}help roleplay`\n Some fun roleplay\n commands")
      embed.add_field(name=":smiley_cat: Animal",value=f"`{sdprefix(self.client,ctx.message)}help animal`\nFind cute animal\npictures")
      embed.add_field(name='Premium lootbox',value="Subscribe to my pateron to get premium features!")
      embed.add_field(name=":laughing: New commands coming soon!",value="**Feel free to request for new features by joining** [my server](https://discord.gg/DQDxhpUJkH).",inline=False)
      
      prefix = sdprefix(self.client,ctx.message)

      utility = discord.Embed(title="<:utility:893012553444233257> Utility Commands",description=f'**Commands Usage**\n`[{sdprefix(self.client,ctx.message)}command] <arg/optional>`\n\nRank - `{prefix}rank <user>`')

      
      


      class mainmenu(discord.ui.View):
        @discord.ui.select(placeholder='📜Select Help Category/Section',min_values=1, max_values=1, options=[
          discord.SelectOption(label="Utility", description='Some useful utilities & commands', emoji="<:utilities:899482350117847040>"),
          discord.SelectOption(label='Moderation', description='Userful server moderation commands', emoji='<:moderation:893014872932089867>'),
          discord.SelectOption(label='Games', description='Some fun game commands for you to play', emoji='🎮'),
          discord.SelectOption(label='Economy',description='A fun economy system to play with',emoji="<:economy:894346237157998612>"),
          discord.SelectOption(label="Music",description="Play music in discord!",emoji="🎵"),
          discord.SelectOption(label="Misc",description="Some more useful commands",emoji="<:command_block:894349809027252244>"),
          discord.SelectOption(label="Roleplay",description="Some fun roleplay commands",emoji="🦸"),
          discord.SelectOption(label="Animal",description="Find cute animal pictures",emoji="😺"),
      ])
        async def select_callback(self, select, interaction):
          if select.values[0] == 'Utility':
            await interaction.response.send_message(content="** **",embed=utility)





      view = mainmenu()
      view.add_item(discord.ui.Button(label='Invite Link', url='https://discord.com/api/oauth2/authorize?self.client_id=763315062668001301&permissions=8&scope=bot%20applications.commands', style=discord.ButtonStyle.url))
      view.add_item(discord.ui.Button(label="Support Server", url='https://discord.gg/DQDxhpUJkH', style=discord.ButtonStyle.url))

      await ctx.send(content='** **',embed=embed,view=view)

def setup(client):
  client.add_cog(help(client))