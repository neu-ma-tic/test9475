import discord
import aiofiles
from discord.ext.commands import cooldown, BucketType
import random
import datetime
import os
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
import json
from music import Player

intents = discord.Intents.default()
intents.members = True

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, intent=intents, case_insensitive=True)
client.warnings = {}
client.sniped_messages = {}

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", color=discord.Color.red())
        await ctx.send(embed=em)

os.chdir(r'C:\Users\adrian\Downloads\Python Proj\Project')
client.remove_command('help')
status = cycle(['Gabs Revamped Discord Bot!', 'Type ".help" for support!'])

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users


async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

@client.command()
async def bal(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.red())
    em.add_field(name = "Wallet balance",value = wallet_amt)
    em.add_field(name = "Bank balance",value = bank_amt)
    await ctx.send(embed = em)

@client.command()
@commands.cooldown(1,30,commands.BucketType.default)
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(201)

    await ctx.send(f"Somone gave you {earnings} coins!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@client.command()
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount.")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("You don't have that much money bozo!")
        return
    if amount<0:
        await ctx.send("Amount must be postive idiot.")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"You withdrew {amount} coins!")

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {guild.name}")

@client.command()
async def help_eco(ctx):
    embed = discord.Embed(
        title = 'Help Economy',
        description = 'A description of all the bots Economy commands.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Potential#5976')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/895800918245802037/896859238847094784/image0.png')
    embed.set_author(name='The Unnormal Bot')
    embed.add_field(name='Beg', value='Begs someone to give you money.', inline=False)
    embed.add_field(name='Bal', value='Checks your acccount balance.', inline=False)
    embed.add_field(name='Withdraw', value='Takes money from your bank into your wallet.', inline=False)

    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help General',
        description = 'A description of all the bots General commands..',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Potential#5976')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/895800918245802037/896859238847094784/image0.png')
    embed.set_author(name='The Unnormal Bot')
    embed.add_field(name='Help', value='Shows this message.', inline=False)
    embed.add_field(name='8ball', value='Ask any question and the 8ball shall answer.', inline=False)
    embed.add_field(name='snipe', value='Snipes the last message someone deleted.', inline=False)
    embed.add_field(name='emojify', value='emojifies anything you say.', inline=False)
    embed.add_field(name='Ping', value='Checks your ping.', inline=False)
    embed.add_field(name='Help_music', value='Commands for Music.', inline=False)
    embed.add_field(name='Help_mod', value='Commands for Moderation', inline=False)
    embed.add_field(name='Help_eco', value='Commands for the bots Economy', inline=False)

    await ctx.send(embed=embed)

@client.command()
async def help_music(ctx):
    embed = discord.Embed(
        title = 'Help Music',
        description = 'A description of all the bots Music commands.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Potential#5976')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/895800918245802037/896859238847094784/image0.png')
    embed.set_author(name='The Unnormal Bot')
    embed.add_field(name='Join', value='Makes the bot join vc.', inline=False)
    embed.add_field(name='Leave', value='Makes the bot disconnect from the vc.', inline=False)
    embed.add_field(name='Play', value='Plays music.', inline=False)
    embed.add_field(name='Skip', value='Skips the song playing now.', inline=False)
    embed.add_field(name='Queue', value='A list of all the songs in queue.', inline=False)
    embed.add_field(name='Search', value='Finds a song.', inline=False)

    await ctx.send(embed=embed)

@client.command()
async def help_mod(ctx):
    embed = discord.Embed(
        title = 'Help Moderation',
        description = 'A description of all the bots Moderation commands.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Potential#5976')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/895800918245802037/896859238847094784/image0.png')
    embed.set_author(name='The Unnormal Bot')
    embed.add_field(name='Clear', value='clears messages within the limit of 100.', inline=False)
    embed.add_field(name='Kick', value='Kicks any user specified.', inline=False)
    embed.add_field(name='Ban', value='Bans any user specified.', inline=False)
    embed.add_field(name='Prefix', value='Changes the botx prefix.', inline=False)
    embed.add_field(name='Unban', value='Unbans a member on the guild.', inline=False)
    embed.add_field(name='warn', value='Gives a warning towards a specified user..', inline=False)
    embed.add_field(name='warnings', value='Checks the warning of a specified user.', inline=False)

    await ctx.send(embed=embed)

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Gabs Newly Developed Bot!'))
    print('Bot is ready.')
    for guild in client.guilds:
        client.warnings[guild.id] = {}

        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id)]]

@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}

@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    if reason is None:
        return await ctx.send("Please provide a valid reason for warning this user.")

    try:
        first_warning = False
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

@client.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        await ctx.send("This user has no warnings.")

@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def gstart(ctx, mins : int, *, prize: str):
    embed = discord.Embed(title = "Giveaways", description = f"{prize}", colour = ctx.author.colour)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

    embed.add_field(name = "Ends at:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} minutes from now.")

    my_msg = await ctx.send(embed = embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins*60)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")

async def setup():
    await client.wait_until_ready()
    client.add_cog(Player(client))

client.loop.create_task(setup())

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(manage_messages=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix Changed to: {prefix}')

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def emojify(ctx,*,text):
    emojis = []
    for s in text.lower():
        if s.isdecimal():
            num2emo = {'0':'zero','1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
            emojis.append(f':{num2emo.get(s)}:')
        elif s.isalpha():
            emojis.append(f':regional_indicator_{s}:')
        else:
            emojis.append(s)
    await ctx.send(''.join(emojis))


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete ya bozo.')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                'It is decidedly so.',
                'Without a doubt,'
                'Yes = definitely,'
                'You may rely on it.',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later',
                'Better not to tell you.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Do not count on it.',
                'My reply is no.',
                'My sources say no',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run('ODk2MTgzNjU2NDc1OTMwNjc1.YWDaEQ.gp82ZMNFwoGHsDR0WgqnPJVBcxM')
