import discord
import math
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import platform
import sqlite3

bot = commands.Bot(command_prefix='*', self_bot=True, help_command=None)

print("Loading up the self-bot script..\n")

print("Welcome to Discord SelfBot!")
print("Go to your Discord window logged in on your browser and press CTRL + Shift + I")
print("Then go to the Applications tab > Local Storage > discord.com")
print("Scroll down on the key value table and press F5 to refresh the tab")
print("You should see a token that appears briefly at the bottom of the table, try to copy it, that will be your user token!\n")

token = input("Please enter your user token here: ")

print("Starting the bot now (this may take a few seconds)...\n")

print("The prefix for this selfbot is '!'")
print("The bot is technically running and most commands can be used except !about, but due to selfbotting Discord API issues,")
print("it will take 5 minutes for the bot on ready to fire up, only then will the uptime start counting and hence !about be usable.")

print("To set logging channel, go to logs.py and replace the number in line 17 to the channel ID you want to log on. (preferably a hidden channel, obviously)")

# --------------------------------

help_extensions = ['help']

startup_extensions = ['commands', 'logs']

if __name__ == "__main__":  # Loads all extension specified above on bot start-up.

    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print(f'{extension}.py successfully loaded!')
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Failed to load extension {extension}\n{exc}')

@bot.event  # Console printing to indicate that Ghost-chan is up and active.
async def on_ready():

    print("Logging in as " + str(bot.user))
    print('Loading...')
    print(str(bot.user) + " has connected to Discord!")
    print("Selfbot is ready to go!")
    print("Current Discord Version: " + discord.__version__)
    print("Number of servers currently connected to Selfbot:")
    print(len([s for s in bot.guilds]))
    print("Number of players currently connected to Selfbot:")
    m = sum(guild.member_count for guild in bot.guilds)
    print(m)

    seconds = 0

    while True:

        global uptime
        seconds += 1
        minutes = seconds / 60
        hours = seconds / 3600
        days = seconds / 86400

        await asyncio.sleep(1)

        if seconds < 60:

            uptime = (str(seconds) + str("s"))

        elif 60 < seconds < 3600:

            uptime = f"{math.floor(minutes)}m {(int(seconds) - math.floor(minutes) * 60)}s"

        elif 3600 < seconds < 86400:

            uptime = ("{0}h {1}m {2}s".format(math.floor(hours), (int(minutes) - math.floor(hours) * 60),
                                              int(seconds) - math.floor(minutes) * 60))

        else:

            uptime = ("{0}d {1}h {2}m {3}s".format(math.floor(days), (int(hours) - math.floor(days) * 24),
                                                   (int(minutes) - math.floor(hours) * 60),
                                                   int(seconds) - math.floor(minutes) * 60))


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def about(ctx):
    async for guild in bot.fetch_guilds(limit=150):

        len([s for s in bot.guilds])

    m = sum(guild.member_count for guild in bot.guilds)
    m2 = ('{:,}'.format(m))  # Formatting integers to have , in them (e.g. 99,999)

    embed = discord.Embed(color=0x4797b1)

    embed.add_field(name="**Info**", value=f"**Uptime:** {uptime}", inline=True)
    embed.add_field(name="**Counts**", value="{0} Users\n{1} Servers".format(m2, str(len([s for s in bot.guilds]))), inline=True)
    #embed.set_thumbnail(url="") # Insert the URL for your selfbot's thumbnail and remove the # comment sign!
    embed.set_footer(text="Made with Discord.py :: " + discord.__version__ + " and Python :: " + platform.python_version() + " | " + str(ctx.message.author), icon_url="https://i.imgur.com/UzTCxvF.png")

    await ctx.send(embed=embed)

# --------------------------------



bot.remove_command('help')

if __name__ == "__main__":  # Loads all extension specified above on bot start-up.
    for extension in help_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Failed to load extension {extension}\n{exc}')

bot.run(f"{token}", bot=False, reconnect=True)
