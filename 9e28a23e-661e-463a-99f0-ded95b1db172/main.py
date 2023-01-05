import os

from floor_price import FloorPrice
from keep_alive import keep_alive

from dotenv import load_dotenv
from discord.ext import commands


load_dotenv('bot.env')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

url_ape = 'https://api.opensea.io/api/v1/collection/gamblingapesofficial'
url_0xv = 'https://api.opensea.io/api/v1/collection/0xvampire-project'

@bot.command(name='floor')
async def nine_nine(ctx):

    apesFloor = FloorPrice(url_ape)
    vampFloor = FloorPrice(url_0xv)


    await ctx.send(f'The floor price for Gambling Apes is {apesFloor} ETH\nThe floor price for 0xVampires is {vampFloor} ETH')
    
keep_alive()
bot.run(TOKEN)