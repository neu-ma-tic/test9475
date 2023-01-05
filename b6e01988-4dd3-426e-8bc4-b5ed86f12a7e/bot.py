from discord.ext import commands

bot = commands.Bot(command_prefix='&&')

bot.lavalink_nodes = [
    {
        "host": "losingtime.dpaste.org", 
        "port": 2124, 
        "password": "SleepingOnTrains",
    }
]


@bot.event
async def on_ready():
    print('Bot is ready to play some music.')
    bot.load_extension('dismusic')
    bot.load_extension("dch")
    
bot.run("TOKEN")
