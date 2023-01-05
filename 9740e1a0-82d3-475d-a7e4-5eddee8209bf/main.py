import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=";")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("Love You!"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Lệnh gì lạ dị cha. ;help xem lại đi cha")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Câu cú thiếu kìa cha. ;help xem lại đi cha")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Hông đủ quyền bẹn ơi")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Tui hông đủ quyền bẹn ơi!")
    else:
        print("error not caught")
        print(error)


@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    try:
        client.load_extension(f"cogs.{extension}")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send(extension + " is loaded")
    except commands.ExtensionNotFound:
        await ctx.send(extension + " not found")
    else:
        client.load_extension(f'cogs.{extension}')


@client.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    try:
        client.load_extension(f"cogs.{extension}")
    except commands.ExtensionNotFound:
        await ctx.send(extension + " not found")
    else:
        await ctx.send(extension + " is unloaded")
        client.unload_extension(f"cogs.{extension}")


@client.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    try:
        client.load_extension(f"cogs.{extension}")
    except commands.ExtensionNotFound:
        await ctx.send(extension + " is not found")
    else:
        await ctx.send(extension + " is reloaded")
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODgwMDg1NTMwMTY2MDU5MDQ5.YSZJhQ.CX6qvlxMptqHatG1tH7FNfkj4d0')
