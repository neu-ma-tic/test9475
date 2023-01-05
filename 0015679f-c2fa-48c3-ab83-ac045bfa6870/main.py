import keep_alive
import discord, asyncio
from discord.ext import commands, tasks
import threading, time
import sys
import os

p = "!"
bot, general = commands.Bot(command_prefix="!", description='ur mom'), None


@bot.event
async def on_ready():
    global general
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Game(name=" ROMAN HELLOOOOOO <3"))
    general = bot.get_channel(887212326007230474)
    print('IM READY')


def actions(id):
    pinger[id][1] = True
    while pinger[id][1]:
        bot.loop.create_task(general.send(f'<@{id}>'))
        time.sleep(1)


#766426244862312518

pinger = {}


@bot.event
async def on_message(message):
    id, content = message.author.id, message.content.lower()
    if message.author != bot.user and content.startswith('hello'):
        await message.channel.send('Hello!')
    elif content == p + 'ping':
        await message.channel.send(f'Pong! {round(bot.latency, 1)}')
    elif content == p + 'start':
        pinger[id] = [threading.Thread(target=actions, args=(id, )), False]
        pinger[id][0].start()
    elif content == p + 'stop':
        pinger[id][1] = False


class Command:
    def __init__(self, _):
        self.cmd = None

    def register_self(self):
        from command_registry import registry
        registry.register(self.cmd, self.__class__)

    def unregister_self(self):
        from command_registry import registry
        registry.unregister(self.cmd)

    async def execute(self, *args, **kwargs):
        pass


keep_alive.keep_alive()
bot.run('OTAzODgxNzI1NTg1Nzg4OTQ5.YXzbdA.qyMHDOQfQkCvt21OJld3ZSNVDs4')
