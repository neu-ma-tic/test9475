import os
from dotenv import load_dotenv, find_dotenv
from typing import List, Optional

import requests
import bs4

from pycoingecko import CoinGeckoAPI
from discord.ext import commands
import discord

from keep_alive import keep_alive

token = os.environ['TOKEN']
# dict of symbols cryptocurrency
dict_of_symbols = {}
with open("symbols.txt", mode='r') as file:
    content = file.readlines()
for elem in content:
    ind = elem.find('\t')
    ind2 = elem.find("\n")
    dict_of_symbols[elem[ind + 1:ind2]] = elem[:ind]


intents = discord.Intents.default()  # setting the visible list of members
intents.members = True  # setting the visible list of members
# command_prefix - sign of command, intents - to make list of members visible, help_command to write my own help_command
bot = commands.Bot(command_prefix='--', intents=intents, help_command=None)

cg = CoinGeckoAPI()


def get_quote() -> str:
    """ Returns a daily quote from site: brainyquote """
    res = requests.get('https://www.brainyquote.com/quote_of_the_day')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    lst = soup.select('.qotd-wrapper-cntr')[0]

    return str(lst.get_text()).replace('\n', "")


def get_eur_gbp_usd() -> List[str]:
    """ returns list of eur gbp usd in current price """
    res = requests.get('https://mybank.pl/kursy-walut/')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    lst = soup.select('.box_mini')

    return [str(lst[0].text[5:9]), str(lst[1].text[5:9]), str(lst[2].text[5:9])]


@bot.command()
async def test(ctx):
    """ test command """
    await ctx.send("Thanks for testing me! :D")


@bot.command()
async def hello(ctx):
    """ command to mention and say hello to user """
    await ctx.send(f"{ctx.author.mention} hello!")


@bot.command(name="help")
async def help(ctx):
    """ command to display list of all bot commands """
    emb = discord.Embed(title="List of bot commands:", color=0x99aab5)
    emb.add_field(name="--hello", value="command to said hello")
    emb.add_field(name="--joined", value="command to check when you joined server")
    emb.add_field(name="--raport", value="command to check EUR GBP USD price")
    emb.add_field(name="--q", value="command to check today's quote")
    emb.add_field(name="--price (crypto-symbol) (currency)",
                  value="command to check cryptocurrency price, default currency "
                        "is USD")
    await ctx.send(embed=emb)


@bot.command()
async def price(ctx, symbol: str, currency: Optional[str] = None):
    """ Check current price of cryptocurrency

    Parameters:
    symbol: str
        symbol of cryptocurrency you want check
    currency: Optional[str]
        the currency you want (default is USD)

   """
    try:
        token = "".join(dict_of_symbols[symbol.upper()].lower())
        if currency is None:
            price = cg.get_price(ids=token, vs_currencies='usd')[token]['usd']
            emb = discord.Embed(title=token.capitalize() + " price:", description=str(price) + " $", color=0x00ff00)
        else:
            price = cg.get_price(ids=token, vs_currencies=str(currency))[token][str(currency)]
            emb = discord.Embed(title=token.capitalize() + " price:", description=str(price) + f" {currency.upper()}",
                                color=0x00ff00)
        await ctx.send(embed=emb)
    except:
        await ctx.send("Put a correct crypto name!")


@bot.command()
async def joined(ctx):
    """ command to check the date of joining to the server"""
    await ctx.send(f"You joined at: {str(ctx.author.joined_at)[:16]}")


@bot.command()
async def raport(ctx):
    """ command to check eur gbp usd prices """
    emb = discord.Embed(title="$ Currencies raport $", colour=15844367)
    emb.add_field(name="EUR", value=get_eur_gbp_usd()[0])
    emb.add_field(name="GBP", value=get_eur_gbp_usd()[1])
    emb.add_field(name="USD", value=get_eur_gbp_usd()[2])
    await ctx.send(embed=emb)


@bot.command(name="q")
async def daily_quote(ctx):
    """ command to check today's quote """
    q = get_quote()
    emb = discord.Embed(title="Daily Quote", colour=0x3498db)
    emb.add_field(name="Quote for today:", value=q)
    await ctx.send(embed=emb)


@bot.event
async def on_message(message):
    """ command to do something while member send a message """

    # command to send message if uniqe user(id) wrote something
    # if str(message.author.id) == "123456789123456789":
    #    await message.channel.send("xyz")

    # command to send message if uniqe user(nickname) wrote something
    # if str(message.author).startswith("nickname"):
    #    await message.channel.send("xyz")

    # server guild
    # guild = message.guild

    # members of guild(server)
    # members = guild.fetch_members(limit=150)

    # printing members of server
    # async for member in members:
    #    print(member)

    # printing roles of every member
    # async for member in members:
    #    print(member.roles)

    # catch some role
    # my_role = message.guild.roles[5]

    # add roles to user (need permission!)
    # var = discord.utils.get(message.guild.roles, name="role")
    #   await member.add_roles(my_role)

    # do is necessary for simultaneous operation bot.command and on_message
    await bot.process_commands(message)

keep_alive()
bot.run(token)