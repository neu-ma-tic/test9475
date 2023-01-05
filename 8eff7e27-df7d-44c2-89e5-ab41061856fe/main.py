#This is your main python file

import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = "K ")
client.remove_command('help')

@client.event
async def on_ready():
        print("Bot is now online!")
       
#HERE IS AN EXAMPLE COMMAND - THIS IS NOT NEEDED BUT EVERYTHING ELSE IS <--------------
#Help Command
@client.command(pass_context=True)
async def help(ctx):
        author = ctx.message.author

        embed = discord.Embed(
                colour = discord.Colour.orange()
        )

        embed.set_author(name='M692s Pet | The 100 Subscriber Bot - Help and Other Documentation')
        embed.add_field(name='<help', value='I thought you knew this one already!!', inline=False)
        embed.add_field(name='<clear amount', value='Delete messages. <clear will delete 1 message, but you can customise how many you want to delete by writing how many after the command. e.g. <clear 25', inline=False)       
        embed.add_field(name='<8ball message', value='The magic 8ball will decide on the outcome of your quesiton or query.', inline=False)
        embed.add_field(name='<extendlife', value='Extend my life by keeping my code active. If im not used for a few hours i time out and shutdown until my friend M692 can fire me back up again!', inline=False)
        embed.add_field(name='Support us', value='https://streamelements.com/m692-5029/tip', inline=False)
        
        await client.send_message(author, embed=embed)
        await client.say("Message sent to your DMs!")


keep_alive()
client.loop.create_task(change_status())
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(NzA2MTM1NjM3MTQwNzAxMTk0.XrFfdw.oX8oW4UJcqRUnvo6Odxz-C9sHLQ)