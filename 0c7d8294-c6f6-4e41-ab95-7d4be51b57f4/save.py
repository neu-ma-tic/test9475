  
import discord
import os
import asyncio


delete = 1

def read_file (drop_file) :
  if os.stat(drop_file).st_size != 0:
    f=open(drop_file,"r+")
    data=f.readline()
    f.truncate(0)
    f.close()
    return data

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.bg_drop())


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def bg_drop(self):
        await self.wait_until_ready()
        channel_3090_fe = self.get_channel(817504026894663721) # channel ID goes here
        channel_3080_fe = self.get_channel(817440964511662163) # channel ID goes here
        channel_3070_fe = self.get_channel(817503955970031657) # channel ID goes here
        channel_3060ti_fe = self.get_channel(817503991649927198) # channel ID goes here

        while not self.is_closed():

            link_3090 = read_file('3090_fe.json')
            if link_3090 != None : 
              await channel_3090_fe.send('{}'.format(link_3090))
              await asyncio.sleep(1) # task runs every second

            link_3080 = read_file('3080_fe.json')
            if link_3080 != None : 
              await channel_3080_fe.send('{}'.format(link_3080))
              await asyncio.sleep(1) # task runs every second

            link_3070 = read_file('3070_fe.json')
            if link_3070 != None : 
              await channel_3070_fe.send('{}'.format(link_3070))
              await asyncio.sleep(1) # task runs every second
            
            link_3060ti = read_file('3060ti_fe.json')
            if link_3060ti != None : 
              await channel_3060ti_fe.send('{}'.format(link_3060ti))
              await asyncio.sleep(1) # task runs every second 
    
  

client = MyClient()
client.run(os.getenv('TOKEN'))




  

