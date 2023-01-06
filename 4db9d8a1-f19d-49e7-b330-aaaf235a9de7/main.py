import discord
from discord.ext import commands
from flaskapp import run
import os

client = commands.Bot(command_prefix = "?")
client.remove_command('help')


@client.event
async def on_ready():
	await client.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.listening,
	        name=("?help | Demonix's World")))
	print("Bot is ready!")

@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 786539019273240576:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

    if payload.emoji.name == '1_':
      role = discord.utils.get(guild.roles, name='13+')
    elif payload.emoji.name == '2_':
      role = discord.utils.get(guild.roles, name='<13')
    
    if role is not None:
      member = payload.member
      if member is not None:
        await member.add_roles(role)

    else:
      print('member not found')

@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if message_id == 786539019273240576:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

    if payload.emoji.name == '1_':
      role = discord.utils.get(guild.roles, name='13+')
    elif payload.emoji.name == '2_':
      role = discord.utils.get(guild.roles, name='<13')
    
    member = guild.get_member(payload.user_id)
    await member.remove_roles(role)
    print('done')

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		error1 = discord.Embed(
		    title="ERROR", description="Hey! You can't do that.")
		error1.set_thumbnail(
		    url=
		    "https://media.discordapp.net/attachments/715315067440070768/784010485384871976/20201203_115608.png?width=475&height=475"
		)
		await ctx.send(embed=error1, delete_after=3)
		await ctx.message.delete()
	elif isinstance(error, commands.MissingRequiredArgument):
		error2 = discord.Embed(
		    title="ERROR", description="Please enter all arguments.")
		error2.set_thumbnail(
		    url=
		    "https://media.discordapp.net/attachments/715315067440070768/784010485384871976/20201203_115608.png?width=475&height=475"
		)
		await ctx.send(embed=error2, delete_after=3)
		await ctx.message.delete()
	else:
		error3 = discord.Embed(
		    title="ERROR", description="No command found :( try: ?help")
		error3.set_thumbnail(
		    url=
		    "https://media.discordapp.net/attachments/715315067440070768/784010485384871976/20201203_115608.png?width=475&height=475"
		)
		await ctx.send(embed=error3, delete_after=3)
		await ctx.message.delete()


#Main


@client.command()
async def roles(ctx):
	selfrole = discord.Embed(title="<a:dancin:786152371326812177> Reaction Roles! <a:dancin:786152371326812177>", destription="Click the reaction to get your role! (Bot have to be online)", color=0xffff00)
	selfrole.add_field(name="Age Roles", value="<:1_:786537175222321202> = 13+, <:2_:786537232467099668> = <13")
	await ctx.send(embed=selfrole)

@client.command()
async def ping(ctx):
	pinger = discord.Embed(title="**Pong!**", color=0xffff00)
	pinger.add_field(
	    name="My ping is:", value=f"{round(client.latency * 1000)}ms!")
	pinger.set_thumbnail(
	    url=
	    "https://media.discordapp.net/attachments/775268733425418240/784318159914139668/1f3d3.png"
	)
	await ctx.send(embed=pinger)


@client.command()
async def info(ctx):
	inform = discord.Embed(
	    title=" ",
	    description=
	    "Hej jestem nowym wielofunkcyjnym botem! Jestem online 24/7 i ciągle się rozwijam.",
	    color=0x00ffff)
	inform.add_field(name="Discord.py version:", value="1.5.1")
	inform.add_field(name="Python version:", value="3.8.2")
	inform.set_author(name="Bot Info!")
	await ctx.send(embed=inform)


@client.command()
async def help(ctx):
	helper = discord.Embed(title=" ", color=0x00ff00)
	helper.set_author(name="Commands list")
	helper.set_thumbnail(
	    url=
	    "https://media.discordapp.net/attachments/715315067440070768/783824179752730624/20201202_224325.png?width=468&height=468"
	)
	helper.add_field(name="Main", value="help, ping, info", inline=False)
	helper.add_field(
	    name="Moderation",
	    value="ban/unban, kick, mute/unmute, clear",
	    inline=False)
	helper.add_field(name="Tools", value="gstart, lock/unlock", inline=False)
	await ctx.send(embed=helper)


#Moderation


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	kicker = discord.Embed(
	    title=" ", description=f"**Reason:** {reason}", color=0xff0000)
	kicker.set_author(
	    name=f"{member} has been kicked!", icon_url=f"{member.avatar_url}")
	kicker.set_thumbnail(url=f"{ctx.author.avatar_url}")
	kicker.add_field(name="Kicked by: ", value=f"{ctx.author.mention}")
	await ctx.send(embed=kicker)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	banner = discord.Embed(
	    title=" ", description=f"**Reason:** {reason}", color=0xff0000)
	banner.set_author(
	    name=f"{member} has been banned!", icon_url=f"{member.avatar_url}")
	banner.set_thumbnail(url=f"{ctx.author.avatar_url}")
	banner.add_field(name="Banned by: ", value=f"{ctx.author.mention}")
	await ctx.send(embed=banner)


#Tools

@client.command()
async def set_reaction(ctx, role: discord.Role=None, msg: discord.Message=None, emoji=None):
    if role != None and msg != None and emoji != None:
        await msg.add_reaction(emoji)
        bot.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))
        
        async with aiofiles.open("reaction_roles.txt", mode="a") as file:
            emoji_utf = emoji.encode("utf-8")
            await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

        await ctx.channel.send("Reaction has been set.")
        
    else:
        await ctx.send("Invalid arguments.")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
	await ctx.message.delete()
	await ctx.channel.purge(limit=amount)
	clearer = discord.Embed(
	    title=" ",
	    description=f"**Requested by:** {ctx.author.mention}",
	    color=0xff9900)
	clearer.set_author(name=f"Deleted {amount} messages!")
	await ctx.send(embed=clearer)


run()
client.run(os.environ.get('TOKEN'))
