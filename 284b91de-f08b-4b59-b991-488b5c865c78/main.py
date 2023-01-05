import discord
import os
from replit import db
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!spy ', intents=intents)

game_active = False
spy = None
location = None
players = 0
players_voted = -1
suspended_players = []
channel = None
most_voted = ("", 0)


@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}")


@bot.command(name="add", help="Adds locations to the game")
async def add_location(ctx, location, *jobs):
    if [role for role in ctx.message.author.roles if role.name == "Spy"] == []:
        return await ctx.send("Missing role 'Spy'.")
    if "locations" in db.keys():
        locations = db["locations"]
        if location in locations.keys():
            #Exiting location if exists
            await ctx.send(
                f"Location {location} exists already. Remove this location first if you want to update it."
            )
        locations[location] = jobs
        db["locations"] = locations
    else:
        db["locations"] = {location: jobs}
    await ctx.send(f"Added {location} with {', '.join(jobs)} to the game.")


@bot.command(name="remove", help="Removes a location from the game")
async def remove_location(ctx, location):
    if [role for role in ctx.message.author.roles if role.name == "Spy"] == []:
        return await ctx.send("Missing role 'Spy'.")
    if "locations" in db.keys():
        locations = db["locations"]
        if location not in locations.keys():
            #Exiting if location not in Database
            return await ctx.send(f"Location {location} not found.")
        del locations[location]
        db["locations"] = locations
        await ctx.send(f"Removed {location} from the game.")
    else:
        await ctx.send("You need to add a location first!")


@bot.command(name="list", help="Lists all locations of the game")
async def list_locations(ctx, location=""):
    if "locations" in db.keys():
        locations = db["locations"]
        if len(locations) == 0:
            #Exiting if Database is empty
            return await ctx.send("You need to add a location first!")
        if location in locations.keys():
            out_str = "\n".join(locations[location])
            embed = discord.Embed()
            embed.add_field(name=location, value=out_str, inline=False)
            await ctx.send(embed=embed)
        elif location != "":
            await ctx.send(f"{location} not found in locations.")
        else:
            out_str = "\n".join(locations.keys())
            embed = discord.Embed()
            embed.add_field(name="Locations", value=out_str, inline=False)
            await ctx.send(embed=embed)
    else:
        await ctx.send("You need to add a location first!")


@bot.command(name="start", help="Starts a round of Spyfall")
async def start_game(ctx):
    global suspended_players
    suspended_players = []
    global game_active
    game_active = True
    reset()
    voice_state = ctx.author.voice
    if voice_state is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send(
            "You need to be in a voice channel to use this command!")
    if "locations" in db.keys():
        locations = db["locations"]
        chosen_location = random.choice(list(locations.keys()))
        global location
        location = chosen_location
        print("Location chosen is " + chosen_location)
    else:
        return await ctx.send("You need to add a location first!")
    joblist = list(locations[chosen_location]).copy()
    members = ctx.author.voice.channel.members
    chosen_member = random.choice(members)
    global spy
    spy = chosen_member.name
    print("Spy chosen is " + chosen_member.name)
    counter = 0
    multiplier = round(len(members) / len(joblist), 0)
    while counter < multiplier:
        joblist.append(joblist)
        counter += 1
    for member in members:
        if member == chosen_member:
            embed = discord.Embed()
            embed.add_field(name="Unkown", value="Spy", inline=False)
        else:
            rndm_job = random.randrange(0, len(joblist))
            embed = discord.Embed()
            embed.add_field(name=chosen_location,
                            value=joblist.pop(rndm_job),
                            inline=False)
        await member.send(embed=embed)
    await ctx.send("Roles assigned.")


@bot.command(name="vote", help="Creates a voting system to catch the spy")
async def vote_spy(ctx):
    global game_active
    if not game_active:
        return await ctx.send("Start a game before voting.")
    game_active = False
    members = ctx.author.voice.channel.members
    global players
    players = len(members)
    global channel
    channel = ctx
    for member in members:
        message = await ctx.send(member.name)
        await message.add_reaction('⬆')


@bot.event
async def on_reaction_add(reaction, user):
    global players
    global suspended_players
    global most_voted
    if reaction.count > most_voted[1]:
        most_voted = (reaction.message.content, reaction.count)
    if user not in suspended_players:
        global players_voted
        players_voted += 1
        suspended_players.append(user)
    if players == players_voted:
        global channel
        global spy
        if most_voted[0] == spy:
            await channel.send(f"Voting done. {most_voted[0]} was the spy.")
        else:
            await channel.send(f"Voting done. {most_voted[0]} was not the spy.")
        reset()


def reset():
    global spy
    global location
    global players
    global players_voted
    global suspended_players
    global channel
    global most_voted
    spy = None
    location = None
    players = 0
    players_voted = -1
    suspended_players = []
    channel = None
    most_voted = ("", 0)


bot.run(os.environ['token'])
