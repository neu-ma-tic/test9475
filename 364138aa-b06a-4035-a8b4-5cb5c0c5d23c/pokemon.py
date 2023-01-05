from discord.ext import commands
from discord.utils import get
from replit import db
import requests
from discord import Embed
import math

def get_info(pokemon:str):
  try:
    api = "https://pokeapi.co/api/v2/pokemon/"
    post = api + pokemon
    return requests.get(post).json()
  except:
    return {}

def get_name(ctx, member_id):
  try:
    user = get(ctx.message.guild.members,id = member_id)
    return user.display_name
  except:
    return ctx.author.display_name


class Teams(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='add', help='Add a new Pokemon to your team (g!add <pokemon> <level>)')
  async def addPokemon(self, ctx, pokemon:str, level:int):
    pokemon = pokemon.lower()
    if level > 100 or level < 1:
      await ctx.send("Your pokemon's level must be between 1-100")
      return
    data = get_info(pokemon)
    if data:
      user = ctx.author
      base_total = 0
      stats = data["stats"]
      for stat in stats:
        base_total += stat["base_stat"]
      new_pokemon = {
              "name":pokemon,
              "level":level,
              "base_stat_total":base_total
            }
      if "teams" in db.keys():
        teams = db["teams"]
        for team in teams:
          if user.id == team["trainer"]:
            if len(team["pokemon"])<6:
              team["pokemon"].append(new_pokemon)
            elif len(team["pokemon"])>=6:
              await ctx.send(f"You can't have more than 6 pokemon on your team")
              return
            else:
              team["pokemon"] = [new_pokemon]
            db["teams"] = teams
            await ctx.send(f"{pokemon} was added to your team")
            return
      else:
        teams = []
      new_team = {
        "trainer":user.id,
        "pokemon":[new_pokemon]
      }
      teams.append(new_team)
      db["teams"] = teams
      await ctx.send(f"{pokemon} was added to your team")
      
    else:
      await ctx.send(f"{pokemon} is not a valid pokemon name")
      return

  @commands.command(name='level', help='Change the level of a pokemon on your team (g!level <pokemon> <level>)')
  async def levelPokemon(self, ctx, pokemon:str, level:int):
    pokemon = pokemon.lower()
    if level > 100 or level < 1:
      await ctx.send("Your pokemon's level must be between 1-100")
      return
    user = ctx.author
    if "teams" in db.keys():
      teams = db["teams"]
      for team in teams:
        if user.id == team["trainer"]:
          for p in team["pokemon"]:
            if p["name"] == pokemon:
              p["level"] = level
              db["teams"] = teams
              await ctx.send(f"Your {pokemon} is now level {level}")
              return
          await ctx.send(f"You don't have a {pokemon} on your team")
          return
    await ctx.send("You don't have a team registered")
        

  @commands.command(name='remove', help='Remove a pokemon from your team (g!remove <pokemon>)')
  async def removePokemon(self, ctx, pokemon:str):
    deleted_pokemon = pokemon.lower()
    user = ctx.author
    if "teams" in db.keys():
      teams = db["teams"]
      for team in teams:
        if user.id == team["trainer"]:
          for pokemon in team["pokemon"]:
            if pokemon["name"] == deleted_pokemon:
              team["pokemon"].remove(pokemon)
              await ctx.send(f"{deleted_pokemon} was removed from your team")
              db["teams"] = teams
              return
          await ctx.send(f"{deleted_pokemon} is not on your team")
      await ctx.send(f"You don't have a team yet")
    else:
      await ctx.send(f"You don't have a team yet")

  
  @commands.command(name='myteam', help='See your registered team')
  async def showTeam(self, ctx):
    user = ctx.author
    if "teams" in db.keys():
      teams = db["teams"]
      for team in teams:
        if user.id == team["trainer"]:
          team_info = []
          for pokemon in team["pokemon"]:
            team_info.append(f"{pokemon['name']}\tLv. {pokemon['level']}")
          await ctx.send(f"```\n{get_name(ctx, team['trainer'])}\'s Team:\n" + "\n".join(team_info) + "\n```")
          return
      await ctx.send(f"You don't have a team yet")
    else:
      await ctx.send(f"You don't have a team yet")

  @commands.command(name='allteams', help='See every registered team')
  async def showAll(self, ctx):
    if "teams" in db.keys():
      if "comp" in db.keys() and db["comp"] and db["comp"]["registration"]:
        await ctx.send("You cannot see other player's teams during tournament registration")
        return
      teams = db['teams']
      output = []
      for team in teams:
        name = get_name(ctx, team['trainer'])
        name = "test"
        team_info = []
        for p in team['pokemon']:
          team_info.append(f"{p['name']}\tLv. {p['level']}")
        output.append(f"```\n{name}\'s Team:\n" + "\n".join(team_info) + "\n```")
      await ctx.send(f"Player Team Summary:\n" + "\n".join(output))
        
    else:
      await ctx.send(f"There are no registered teams")

  @commands.command(name='clearall', help='Clear all registered team data (BotDev)')
  @commands.has_role("BotDev")
  async def clearTeams(self, ctx):
    db["champ"] = 0
    db["comp"] = {}

class Champion(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='champ', help='See the current champion\'s team')
  async def showChamp(self, ctx):
    if "champ" in db.keys() and db["champ"] != 0 and "teams" in db.keys():
      champ = db["champ"]
      team_info = []
      champ_team = []
      for team in db["teams"]:
        if champ == team["trainer"]:
          champ_team = team["pokemon"]
      for pokemon in champ_team:
        team_info.append(f"{pokemon['name']}\tLv. {pokemon['level']}")
      await ctx.send(f"```\nChampion {get_name(ctx,champ)}\'s Team:\n" + "\n".join(team_info) + "\n```")
    else:
      await ctx.send(f"There is no champion yet! The next tournament will determine our first champion")

  @commands.command(name='setchamp', help='Declare yourself as the new champion for testing (BotDev)')
  @commands.has_role("BotDev")
  async def setChamp(self, ctx):
      user = ctx.author
      if "teams" in db.keys():
        for team in db["teams"]:
          if team["trainer"] == user.id:
            db["champ"] = user.id
            await ctx.send(f"You are now the champion")
            return
      await ctx.send(f"You don't have a registered team")

  @commands.command(name='delchamp', help='Remove the current champion (BotDev)')
  @commands.has_role("BotDev")
  async def delChamp(self, ctx):
    db["champ"] = 0
    await ctx.send(f"The champion title is now up for grabs")


class Tournament(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  def make_matches(self, teams):
    byes =  int(len(teams) - math.pow(2, 
      math.floor(math.log(len(teams),2))))
    print(byes)
    bye_teams = teams[0:byes]
    teams = teams[byes:]
    matches = []
    for i in range(int(len(teams)/2)):
      matches.append([teams[i],teams[-1*i]])
    return matches, bye_teams


  @commands.command(name='create', help='Create a new tournament (g!create <tournament name>) (Admin)')
  @commands.has_role("BotDev")
  async def makeTournament(self, ctx, name:str):
    db["comp"] = {
      "name": name,
      "numteams": 0,
      "teams": [],
      "matchs":[],
      "registration": True
    }
    await ctx.send(f"@everyone The {name} tournament registration has started! Register your team before the deadline to participate in the competition. If you want to register your team, use !register and I'll message you privately to keep your team a secret until the competition starts. The team you register will be the team you use in the tournament. Swapping is not allowed after registration is completed. Evolving and leveling up is allowed, just enter the current levels of your pokemon at the time of registration (this is used for opponent matching). The champion title is up for grabs so bring your best team!")

  @commands.command(name='start', help='End registation and start the tournament (Admin)')
  @commands.has_role("BotDev")
  async def startTournament(self, ctx):
    if "comp" in db.keys() and db["comp"] != {}:
      if db["comp"]["registration"] or True:
        comp = db["comp"]
        comp["registration"] = False
        await ctx.send(f"Registration for the {db['comp']['name']} tournament is over")
        await ctx.send(f"@everyone The {db['comp']['name']} tournament has started!")
        ordered_teams = sorted(comp["teams"], key=lambda k: k['cp'], reverse = True) 
        print(ordered_teams)
        comp["teams"] = ordered_teams
        # matches, bye_teams = self.make_matches(ordered_teams)
        positions = []
        for t in ordered_teams:
          positions.append(f"{ordered_teams.index(t)+1}. {get_name(ctx, t['trainer'])}  CP: {t['cp']}")
        await ctx.send("Here are the seeded positions \n```" + "\n".join(positions) + "```")
        db["comp"] = comp
        return
    await ctx.send("There is no tournament in registration")

  @commands.command(name='force', help='Force team into tournament (BotDev)')
  @commands.has_role("BotDev")
  async def forceTeam(self, ctx, index: int):

    teams = db['teams']
    team = teams[index]
    comp = db["comp"]
    cp = 0
    for p in team["pokemon"]:
      if p["level"] < 50:
        cp += p["base_stat_total"]*p["level"]
      else:
        cp += p["base_stat_total"]*50
    team["cp"] = cp
    comp["teams"].append(team)
    comp["numteams"] += 1
    db["comp"] = comp

  @commands.command(name='compteams', help='See teams in tournament')
  async def seeTeam(self, ctx):
    if "comp" in db.keys() and db["comp"]:
      if db["comp"]["registration"]:
        await ctx.send("You cannot see other player's teams during tournament registration")
        return
      teams = db['comp']['teams']
      output = []
      for team in teams:
        name = get_name(ctx, team['trainer'])
        team_info = []
        for p in team['pokemon']:
          team_info.append(f"{p['name']}")
        output.append(f"```\n{name}\'s Team (Seed {teams.index(team)+1}):\n" + "\n".join(team_info) + "\n```")
      await ctx.send(f"Player Team Summary:\n" + "\n".join(output))
        
    else:
      await ctx.send(f"There are no registered teams")

  @commands.command(name='cancel', help='Cancel the current tournament (Admin)')
  @commands.has_role("BotDev")
  async def cancelTournament(self, ctx):
    if "comp" in db.keys() and db["comp"] != {}:
      db["comp"] = {}
      await ctx.send("The current tournament has been canceled")
      return
    await ctx.send("There is no tournament to cancel")

  @commands.command(name='info', help='See info on the current tournament')
  async def seeTournament(self, ctx):
    if "comp" in db.keys() and db["comp"] != {}:
      if db["comp"]["registration"]:
        await ctx.send(f"```\nThe {db['comp']['name']} tournament:\nThis tournament is still open for registration\nThere are {db['comp']['numteams']} teams registered```")
        return
      else:
        await ctx.send("The tournament is underway!")
        return
    await ctx.send("There is no active tournament. You can ask an Admin to start a new tournament")

  @commands.command(name='register', help='Register for the current tournament')
  async def registerTournament(self, ctx):
    if "comp" in db.keys() and db["comp"] != {}:
      if db["comp"]["registration"]:
        user = ctx.author
        await user.send(f"Hi {user.display_name}! Let's register your team for the tournament")
        await user.send("```Commands:\ng!myteam\tSee your current team\ng!add <pokemon> <level>\tAdd a new pokemon to your team\ng!level <pokemon> <level>\tChange the level of your pokemon\ng!remove <pokemon>\tRemove a pokemon from your team\ng!confirm\tConfirm your team for registration (this will lock in your team for the tournament)```")
        await user.send("When you confirm your team for registration, the team registered is the team you must use in the tournament. Swapping our pokemon is not allowed and you will be disqualified if you enter a tournament battle with the wrong team. Register the levels of your pokemon at the time of your registration. This is only used for initial matching at the start of the tournament. Your pokemon are allowed to evolve or level up before the tournament starts and between battles.")
        return
      else:
        await ctx.send("Registration for the current tournament has ended")
        return
    await ctx.send("There is no active tournament. You can ask an Admin to start a new tournament")

  @commands.command(name='confirm', help='Confirm your team for regisration')
  async def confirmTournament(self, ctx):
    user = ctx.author
    if "comp" in db.keys() and db["comp"] != {}:
      if db["comp"]["registration"]:
        if "teams" in db.keys():
          for team in db["teams"]:
            if team["trainer"] == user.id:
              if len(team["pokemon"]) != 6:
                await ctx.send("You need 6 pokemon on your team to register")
                return
              else:
                comp = db["comp"]
                cp = 0
                for p in team["pokemon"]:
                  if p["level"] < 50:
                    cp += p["base_stat_total"]*p["level"]
                  else:
                    cp += p["base_stat_total"]*50
                team["cp"] = cp
                comp["teams"].append(team)
                comp["numteams"] += 1
                db["comp"] = comp
                print(cp)
                await ctx.send("Your team has been registered! Good luck in the tournament")
                return
        await ctx.send("You don't have a team yet")
        return
      await ctx.send("Registration for the current tournament has ended")
    await ctx.send("There are no active tournaments")

class PokeDex(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name='dex', help='Get information on a pokemon (g!dex <pokemon>)')
  async def dexEntry(self, ctx, pokemon:str):
    pokemon = pokemon.lower()
    data = get_info(pokemon)
    if data:
      types = []
      for t in data['types']:
        types.append(t['type']['name'])
      abilities = []
      for a in data['abilities']:
        if a['is_hidden']:
          abilities.append(a['ability']['name']+" (hidden)")
        else:
          abilities.append(a['ability']['name'])
      stats = []
      ev = ""
      for s in data['stats']:
        stat = f"{s['stat']['name']}: {s['base_stat']}"
        stats.append(stat)
        if s['effort']:
          ev = f"EV Yield: {s['effort']} {s['stat']['name']}"
      description = "\nType: " + "/".join(types) + "\nAbilities:\n\t" + "\n\t".join(abilities) + "\nStats:\n\t" + "\n\t".join(stats) + f"\n{ev}"
      image = data['sprites']['other']['official-artwork']['front_default']
      embed = Embed(title=pokemon.upper())
      embed.set_image(url=image)
      embed.set_footer(text = description)
      await ctx.send(embed=embed)
    else:
      await ctx.send(f"{pokemon} is not a valid pokemon")

  