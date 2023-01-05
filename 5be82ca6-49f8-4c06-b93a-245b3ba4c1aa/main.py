import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()

@client.event
async def on_member_join(member):
    await member.channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


client.run(os.getenv("TOKEN"))