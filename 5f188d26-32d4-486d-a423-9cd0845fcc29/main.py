

import discord,random,asyncio,os
from datetime import datetime
from discord.ext import commands

token = '#mytokenhere'
bot=commands.Bot(command_prefix='!')

send_time='01:41' #time is in 24hr format
message_channel_id='0000000000000' #channel ID to send images to

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

async def time_check():
    await bot.wait_until_ready()
    message_channel=bot.get_channel(message_channel_id)
    while not bot.is_closed:
        now=datetime.strftime(datetime.now(),'%H:%M')
        if now.hour() == 1 and now.minute() == 52:
            message= 'a'
            await message_channel.send(message)
            time=90
        else:
            time=1
        await asyncio.sleep(time)

bot.loop.create_task(time_check())


bot.run('import discord,random,asyncio,os
from datetime import datetime
from discord.ext import commands

token = '#mytokenhere'
bot=commands.Bot(command_prefix='!')

send_time='01:41' #time is in 24hr format
message_channel_id='0000000000000' #channel ID to send images to

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

async def time_check():
    await bot.wait_until_ready()
    message_channel=bot.get_channel(message_channel_id)
    while not bot.is_closed:
        now=datetime.strftime(datetime.now(),'%H:%M')
        if now.hour() == 1 and now.minute() == 52:
            message= 'a'
            await message_channel.send(message)
            time=90
        else:
            time=1
        await asyncio.sleep(time)

bot.loop.create_task(time_check())


bot.run('ODU2OTMwMzAzMDk1NDcyMTM5.YNIMiQ.x4S4PztZtAbs4wtha8EZgu9q4NU')