# Imports
import discord
from discord.utils import get
from discord.ext import commands
# Credentials
print("Enter Token: ")
TOKEN = input()
# Create bot
client = commands.Bot(command_prefix='/')
# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command(pass_context=True)
@commands.has_role("can set custom role")
async def customrole(ctx, *, name):
        
        guild=ctx.guild
        if discord.utils.get(guild.roles, name=name):
            await ctx.send("Role already exists")
            member = ctx.author
            role = get(ctx.guild.roles, name=name)
            await member.add_roles(role)
            role2 = get(ctx.guild.roles, name='can set custom role')
            await member.remove_roles(role2)
        else:
            await guild.create_role(name=name)
            await ctx.send(f'Role `{name}` has been created')
            member = ctx.author
            role = get(ctx.guild.roles, name=name)
            await member.add_roles(role)
            role2 = get(ctx.guild.roles, name='can set custom role')
            await member.remove_roles(role2)

# Run the bot
client.run(TOKEN)
