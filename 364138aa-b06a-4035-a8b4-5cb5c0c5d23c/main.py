from discord import Intents
from discord.ext import commands
import os
from keep_running import keep_running

from pokemon import Teams, Champion, Tournament, PokeDex

intents = Intents().all()
bot = commands.Bot(command_prefix='g!', intents = intents)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("Sorry I don't recognize that command. Use g!help to see a list of commands")

bot.name = 'Gerald'
bot.add_cog(Teams(bot))
bot.add_cog(Champion(bot))
bot.add_cog(Tournament(bot))
bot.add_cog(PokeDex(bot))


keep_running()
bot.run(os.getenv('TOKEN'))