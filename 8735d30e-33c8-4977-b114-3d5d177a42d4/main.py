import discord
from discord.ext import commands
from webserver import keep_alive
import os

#client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix="!", description="Federal Investigation Bureau")

@bot.event
async def on_ready():
    activity = discord.Game(name="www.vio-v.com", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Der FIB Bewerbungsbot steht zu Ihren Diensten!")


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def bw(ctx, name: str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="Bewerbung von " + str(name),
        description=
        "Hallo <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104>! \r\n Bitte stimmt über die folgende Person ab: \r\n\r\n"
        + "**" + str(name) + "**",
        color=0x003b8f)
    embed.set_thumbnail(url="https://i.ibb.co/PTnLgPL/FIB.png")
    embed.set_footer(text='Federal Investigation Bureau')
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🟢')
    await msg.add_reaction('🟡')
    await msg.add_reaction('🔴')
    await msg.add_reaction('🔵')
    await ctx.send(
        'TAG: <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104>'
    )
    await ctx.channel.purge(limit=1)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def leaderab(ctx, *, name: str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="Leaderabstimmung über " + str(name),
        description=
        "Hallo <@&777891119694086205> und <@&777890866509512734>! \r\n Bitte stimmt über das folgende Thema ab: \r\n\r\n"
        + "**" + str(name) + "**",
        color=0x003b8f)
    embed.set_thumbnail(url="https://i.ibb.co/PTnLgPL/FIB.png")
    embed.set_footer(text='Federal Investigation Bureau')
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🟢')
    await msg.add_reaction('🟡')
    await msg.add_reaction('🔴')
    await ctx.send('TAG: <@&777891119694086205> , <@&777890866509512734>')
    await ctx.channel.purge(limit=1)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def clear(ctx, amount: str):
    if amount == 'nichtusen':
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=int(amount) + 1)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def hilfe(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="Befehlsliste",
        description=
        "**!bw [NAME VOM BEWERBER] **= Bewerbungsabstimmung starten\r\n"
        "**!probe [NAME DES TRAINEES] **= Probewochen Abstimmung\r\n"
        "**!leaderab [NAME] **= Leaderabstimmung starten\r\n"
        "**!clear [Anzahl der Nachrichten] **= Löscht Nachrichten\r\n",
        color=0x003b8f)
    embed.set_thumbnail(url="https://i.ibb.co/PTnLgPL/FIB.png")
    embed.set_footer(text='Federal Investigation Bureau')
    msg = await ctx.send(embed=embed)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def probe(ctx, *, name: str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="Abstimmung Probewochen",
        description=
        "Hallo <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104>! \r\n Bitte bewertet die folgenden Personen: \r\n\r\n"
        + "**" + str(name) + "**",
        color=0x003b8f)
    embed.set_thumbnail(url="https://i.ibb.co/PTnLgPL/FIB.png")
    embed.set_footer(text='Federal Investigation Bureau')
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🟢')
    await msg.add_reaction('🟡')
    await msg.add_reaction('🔴')
    await ctx.send(
        'TAG: <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104>'
    )
    await ctx.channel.purge(limit=1)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def academy_mi(ctx, *, name: str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="Academy - Interessenten",
        description=
        "Hallo <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104> ! \r\n Diese Woche möchten sich folgende Akademiker ins Federal Investigation Bureau übernehmen lassen:\r\n\r\n"
        + "**" + str(name) + "**",
        color=0x003b8f)
    embed.set_thumbnail(url="https://i.ibb.co/PTnLgPL/FIB.png")
    embed.set_footer(text='Federal Investigation Bureau')
    msg = await ctx.send(embed=embed)
    await ctx.send(
        'TAG: <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104>'
    )
    await ctx.channel.purge(limit=1)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def academy_sa(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="Academy - Übernahmen",
        description=
        "Hallo <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104>! \r\n Folgende Akademiker stehen zur Auswahl übernommen zu werden.\r\nIch möchte nochmal darauf hinweisen, das die Neins **zu begründen** sind.\r\n\r\n",
        color=0x003b8f)
    embed.set_thumbnail(url="https://i.ibb.co/PTnLgPL/FIB.png")
    embed.set_footer(text='Federal Investigation Bureau')
    msg = await ctx.send(embed=embed)
    await ctx.send(
        'TAG: <@&777891553892106241> , <@&777891504232333333> und <@&777891307511087104>'
    )
    await ctx.channel.purge(limit=1)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ac(ctx, name: str):
    #await message.channel.send(str(name))
    await ctx.channel.purge(limit=1)
    msg = await ctx.send(str(name))
    await msg.add_reaction('🟢')
    await msg.add_reaction('🟡')
    await msg.add_reaction('🔴')
  

keep_alive()
TOKEN = os.environ['DISCORD_BOT_SECRET']
bot.run(TOKEN)