import os, random
from replit import db
import discord
import pytesseract
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='$')
 
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
  await ctx.send('hello!')

#@bot.command()
#async def invite(ctx):
#  await ctx.send('<https://discord.com/api/oauth2/authorize?client_id=836275304963375114&permissions=8&scope=bot>')


@bot.command(name='analyze')
async def on_message(context):
    # manage if context.message.attachments is empty
    image_url = context.message.attachments[0].url
    # improve image format detection
    image_format_jpg = image_url[-3:]
    image_format_jpeg = image_url[-4:]
    image_format_png = image_url[-3:]
    if image_format_jpg.lower() == 'jpg' or image_format_jpeg.lower() == 'jpeg' or image_format_png.lower() == 'png':
        try:
          await context.send("works")
          pytesseract.pytesseract.tesseract_cmd = context.message
          print(pytesseract.image_to_string(context.message)
        except:
            error = discord.Embed(
                title="Ops.. Something went wrong", description="I'm sorry, something went wrong. Please, try again.")
            error.colour = 0xff0000
            await context.message.channel.send(embed=error)
            raise discord.DiscordException
    else:
        invalid_format = discord.Embed(
            title="Invalid format", description="I'm sorry, this format is not supported. Please, try again with a .jpg or .jpeg!")
        invalid_format.colour = 0xff0000
        await context.message.channel.send(embed=invalid_format)

keep_alive() 
bot.run(os.environ['TOKEN2'])


