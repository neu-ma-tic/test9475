import discord
from discord.ext import commands
import aiohttp
from PIL import Image
from io import BytesIO

def is_it_me(ctx):
    return ctx.author.id == 696617859580690512

class utility(commands.Cog):
  def __init__(self,client):
    self.client = client

  


  

  @commands.command()
  @commands.check(is_it_me)
  async def server(self,ctx,guild_name:int=None):
    if guild_name is not None:
      guild = self.client.get_guild(guild_name)
      link = await guild.text_channels[0].create_invite(max_age = 300)
      await ctx.send("Here is an instant invite to your server: " + str(link))
    else:
      index = 0
      for i in self.client.guilds:
        await ctx.send(f"{i.name} - {i.id}")
        index += 1
      await ctx.send(index)


  @commands.command(pass_context=True)
  async def react(self,ctx, emoji:discord.PartialEmoji):
    if emoji.is_custom_emoji():
        processed_emoji = self.client.get_emoji(emoji.id)
    else:
        processed_emoji = emoji.name;
    await ctx.message.add_reaction(processed_emoji)

  @commands.command(aliases=['copy_emoji'])
  async def copyemoji(self,ctx, emojid:discord.PartialEmoji):
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_emojis:
      if emojid.is_custom_emoji():
        processed_emoji = self.client.get_emoji(emojid.id)
        emoji = await guild.create_custom_emoji(image=processed_emoji, name=processed_emoji.name)
        await ctx.send(f'Successfully created emoji: <:{emoji.name}:{emoji.id}>, id: `<:{emoji.name}:{emoji.id}>`')

  @commands.command()
  async def emoji_id(self,ctx,emoji:discord.Emoji):
    await ctx.send(f'id: `<:{emoji.name}:{emoji.id}>`')
  @commands.command(aliases=['create_emoji','upload_emoji'])
  async def addemoji(self,ctx, url: str, *, name):
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_emojis:
      async with aiohttp.ClientSession() as ses:
        async with ses.get(url) as r:
          
          try:
            img_or_gif = BytesIO(await r.read())
            b_value = img_or_gif.getvalue()
            if r.status in range(200, 299):
              emoji = await guild.create_custom_emoji(image=b_value, name=name)
              await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>, id: `<:{name}:{emoji.id}>`')
              await ses.close()
            else:
              await ctx.send(f'Error when making request | {r.status} response.')
              await ses.close()
              
          except discord.HTTPException:
            await ctx.send('File size is too big!')

  @commands.command()
  async def deleteemoji(ctx, emoji: discord.Emoji):
    if ctx.author.guild_permissions.manage_emojis:
      await ctx.send(f'Successfully deleted (or not): {emoji}')
      await emoji.delete()

  @commands.command()
  async def create_invite(ctx,time_out:int):
      """Create instant invite"""
      link = await ctx.channel.create_invite(max_age = time_out)
      await ctx.send("Here is an instant invite to your server: " + link)

  

def setup(client):
  client.add_cog(utility(client))