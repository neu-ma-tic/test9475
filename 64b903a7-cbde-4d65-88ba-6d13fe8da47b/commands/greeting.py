import discord, requests

from discord.ext import commands
from io import BytesIO
from replit import db
from hashlib import md5
from PIL import Image, ImageDraw, ImageFont

class Greeting(commands.Cog, description='Under construction'):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  def inDB(self, guild_id: int, option: str):
      m_key = f'{guild_id}join' if option == 'join' else f'{guild_id}leave'
      key = md5(m_key.encode()).hexdigest()
      #print(key)
      if key in db:
        return (db[key]['channel'], db[key]['img'], db[key]['textfill'], db[key]['textoutline'])
      return None


  @commands.Cog.listener()
  async def on_member_join(self, member: discord.Member):
    value = self.inDB(member.guild.id, 'join')
    if not value or member.bot:
      return
    m_channel, m_image, fill, outline = value
    channel = await self.bot.fetch_channel(m_channel)

    avatar_bytes = requests.get(str(member.avatar_url), stream=True).raw
    avatar = Image.open(avatar_bytes).convert("RGB")

    alpha = Image.new("L", avatar.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse([(0, 0), avatar.size], fill=255, outline='white', width=3)
    avatar.putalpha(alpha)

    avatar = avatar.resize((340, 340))

    banner_bytes = requests.get(m_image, stream=True)
    banner = Image.open(banner_bytes.raw).convert("RGBA")
    banner = banner.resize((1200, 675))
    overlay = Image.new("RGBA", banner.size, 0)
    width, height = banner.size
    w, h = avatar.size
    overlay.paste(avatar, ((width - w) // 2, (height - h) // 2 - 100))
    banner.alpha_composite(overlay)

    draw = ImageDraw.Draw(banner)
    
    text = f'Welcome to {member.guild.name}\n{member.name}'
    font = ImageFont.truetype('font/JustBecause.ttf', 60)
    wtext, htext = draw.textsize(text, font=font)

    posX, posY = (width - wtext) // 2, height // 2 + (height // 2 - htext) // 2

    draw.text((posX - 2, posY - 2), text, font=font, fill=outline, align="center")
    draw.text((posX + 2, posY - 2), text, font=font, fill=outline, align="center")
    draw.text((posX - 2, posY + 2), text, font=font, fill=outline, align="center")
    draw.text((posX + 2, posY + 2), text, font=font, fill=outline, align="center")

    draw.text((posX, posY), text, font=font, fill=fill, align="center")  

    img_byte_arr = BytesIO()
    banner.convert('RGB').save(img_byte_arr, format='PNG')
    byte_value = img_byte_arr.getvalue()
    img_file = BytesIO(byte_value)
    await channel.send(file=discord.File(img_file, f'Welcome {member.name}.png'))


  @commands.Cog.listener()
  async def on_member_remove(self, member: discord.Member):
    value = self.inDB(member.guild.id, 'leave')
    if not value or member.bot:
      return
    m_channel, m_image, fill, outline = value
    channel = await self.bot.fetch_channel(m_channel)

    avatar_bytes = requests.get(str(member.avatar_url), stream=True).raw
    avatar = Image.open(avatar_bytes).convert("L")

    alpha = Image.new("L", avatar.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse([(0, 0), avatar.size], fill=255, outline='white', width=3)
    avatar.putalpha(alpha)

    avatar = avatar.resize((340, 340))

    banner_bytes = requests.get(m_image, stream=True)
    banner = Image.open(banner_bytes.raw).convert("RGBA")
    banner = banner.resize((1200, 675))
    overlay = Image.new("RGBA", banner.size, 0)
    width, height = banner.size
    w, h = avatar.size
    overlay.paste(avatar, ((width - w) // 2, (height - h) // 2 - 100))
    banner.alpha_composite(overlay)

    draw = ImageDraw.Draw(banner)
    
    text = f'Farewell {member.name}\n{member.guild} will miss you'
    font = ImageFont.truetype('font/JustBecause.ttf', 60)
    wtext, htext = draw.textsize(text, font=font)

    posX, posY = (width - wtext) // 2, height // 2 + (height // 2 - htext) // 2

    draw.text((posX - 2, posY - 2), text, font=font, fill=outline, align="center")
    draw.text((posX + 2, posY - 2), text, font=font, fill=outline, align="center")
    draw.text((posX - 2, posY + 2), text, font=font, fill=outline, align="center")
    draw.text((posX + 2, posY + 2), text, font=font, fill=outline, align="center")

    draw.text((posX, posY), text, font=font, fill=fill, align="center")  

    img_byte_arr = BytesIO()
    banner.convert('RGB').save(img_byte_arr, format='PNG')
    byte_value = img_byte_arr.getvalue()
    img_file = BytesIO(byte_value)
    await channel.send(file=discord.File(img_file, f'Goodbye {member.name}.png'))



  @commands.command(description='Set a greeting text channel')
  @commands.has_guild_permissions(manage_channels=True)
  async def greetingchannel(self, ctx: commands.Context, channel: discord.TextChannel):
    to_channel = commands.TextChannelConverter()
    try:
      m_channel = await to_channel.convert(ctx, str(channel))
      value = m_channel.id
      m_key = f'{ctx.guild.id}join'
      key = md5(m_key.encode()).hexdigest()
      db[key] = {
        'channel': value,
        'img': 'https://g4.img-dpreview.com/5ADC4BE97EF846F2B04F94C0E90F0F0E.jpg',
        'textfill': 'white',
        'textoutline': 'black'
      }
      return await ctx.send('Success\nGreeting channel has been set')
    except commands.BadArgument:
      return await ctx.send('Not a valid channel')
    except commands.ChannelNotFound:
      return await ctx.send('Channel not found')

  @greetingchannel.error
  async def greetingchannel_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
      return await ctx.send("You don't have manage channels permission")

  @commands.command(description='Set a leaving text channel')
  @commands.has_guild_permissions(manage_channels=True)
  async def leavingchannel(self, ctx: commands.Context, channel: discord.TextChannel):
    to_channel = commands.TextChannelConverter()
    try:
      m_channel = await to_channel.convert(ctx, str(channel))
      value = m_channel.id
      m_key = f'{ctx.guild.id}leave'
      key = md5(m_key.encode()).hexdigest()
      db[key] = {
        'channel': value,
        'img': 'https://g4.img-dpreview.com/5ADC4BE97EF846F2B04F94C0E90F0F0E.jpg',
        'textfill': 'white',
        'textoutline': 'black'
      }
      return await ctx.send('Success\nLeaving channel has been set')
    except commands.BadArgument:
      return await ctx.send('Not a valid channel')
    except commands.ChannelNotFound:
      return await ctx.send('Channel not found')

  @leavingchannel.error
  async def leavingchannel_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
      return await ctx.send("You don't have manage channels permission")

  @commands.command(description='Delete both leaving and greeting channel')
  @commands.has_guild_permissions(manage_channels=True)
  async def glchanneldel(self, ctx: commands.Context):
    greet = f'{ctx.guild.id}join'
    leave = f'{ctx.guild.id}leave'
    greetkey = md5(greet.encode()).hexdigest()
    leavekey = md5(leave.encode()).hexdigest()
    if greetkey not in db and leavekey not in db:
      return await ctx.send('You have not set any channel for greeting or leaving')
    if greetkey in db:
      del db[greetkey]
    if leavekey in db:
      del db[leavekey]
    return await ctx.send('Successfully deleted greeting or leaving channel')

  @glchanneldel.error
  async def glchanneldel_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
      return await ctx.send("You don't have manage channels permission")

  @commands.command(description='Set an image for greeting\nSuggested ratio 16:9 or size 1200x675', help='greetingimage')
  @commands.has_guild_permissions(manage_channels=True)
  async def greetingimage(self, ctx: commands.Context):
    m_key = f'{ctx.guild.id}join'
    key = md5(m_key.encode()).hexdigest()
    if key not in db:
      return await ctx.send('You have to set a greeting channel first')
    if not ctx.message.attachments:
      return await ctx.send('Please attach an image (suggested ratio 16:9 size 1200x675)')
    for attachment in ctx.message.attachments:
      if attachment.content_type in ('image/jpeg', 'image/jpg', 'image/png'):
        db[key]['img'] = attachment.proxy_url
        return await ctx.send('Successfully set a greeting image')
    else:
      return await ctx.send('Please provide a picture')
  
  @greetingimage.error
  async def greetingimage_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
      return await ctx.send("You don't have manage channels permission")

  @commands.command(description='Set an image for leaving\nSuggested ratio 16:9 or size 1200x675', help='leavingimage')
  @commands.has_guild_permissions(manage_channels=True)
  async def leavingimage(self, ctx: commands.Context):
    m_key = f'{ctx.guild.id}leave'
    key = md5(m_key.encode()).hexdigest()
    if key not in db:
      return await ctx.send('You have to set a leaving channel first')
    if not ctx.message.attachments:
      return await ctx.send('Please attach an image (suggested ratio 16:9 size 1200x675)')
    for attachment in ctx.message.attachments:
      if attachment.content_type in ('image/jpeg', 'image/jpg', 'image/png'):
        db[key]['img'] = attachment.proxy_url
        return await ctx.send('Successfully set a leaving image')
    else:
      return await ctx.send('Please provide a picture')
  
  @leavingimage.error
  async def leavingimage_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
      return await ctx.send("You don't have manage channels permission")