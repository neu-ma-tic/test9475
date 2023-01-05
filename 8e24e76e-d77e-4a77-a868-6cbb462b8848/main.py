import discord
import os
from discord.ext import tasks

from discord.ext import commands
from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv()
TOKEN = 'ODI4MjA5ODI1MTc4NzE0MTYy.YGmQgQ.BzwDQp-jvI2pqaB3QJn3WN60-sY'

'''class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    @tasks.loop(seconds=5) # task runs every 5 seconds
    async def my_background_task(self):
        self.counter += 1
        #await channel.send(self.counter)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in  '''    


#client = MyClient()
client = commands.Bot(command_prefix='$$')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

async def on_message(message):
    if message.author == client.user:
        return

async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('This Command does not exist!')
        
@client.command(name='daily_quote',help='A daily quote from TréMC data base.')
async def daily_quote(ctx):
  response = 'test'
  await ctx.send(response)

client.run(TOKEN)
