import discord
import asyncio
from discord.ext import commands
from sqlite3 import connect
TOKEN = input()
conn = connect("test.db")
cursor = conn.cursor()
bot = commands.Bot(command_prefix='8')
def processSQLite(req : str):
  req.replace("%", "percent")
  cursor.execute(req)

teams = ["Programming", "Mechanical", "Electrical", "Business & Scouting"]
@bot.command()
async def register(ctx, team: str, graduation_date : int, band_member : int, other: str):
  channel = ctx.message.channel
  print(type(channel))
  print("registering")
  ctx.send("Registering")
  try:
    pass
    #await processSQLite("INSERT INTO userdat (uid,team,")
  except:
    print("ERROR")
    return
  member = ctx.message.author
  global teams
  if not (team in teams):
    print("Not a team. F")
    return
  team_role = discord.utils.get(ctx.message.guild.roles, name=team)
  age_group = "Alumni"
  year = graduation_date
  from datetime import datetime
  now = datetime.now()
  curYear = int(now.year)
  diff = year - curYear
  if diff >= 3:
    age_group = "Freshman"
  elif diff == 2:
    age_group = "Sophomore"
  elif diff == 1:
    age_group = "Junior"
  elif diff == 0:
    age_group = "Senior"
  print(f"age: {age_group}")
  age_role = discord.utils.get(ctx.message.guild.roles, name=age_group)
  await member.add_roles(team_role, age_role)
  if not other == "None":
    print("Adding Other")
    await member.add_roles(discord.utils.get(member.server.roles, name=other))
  if band_member == 1:
    print("Adding Band Role")
    band_role = discord.utils.get(member.server.roles, name="Band Cult")
    await member.add_roles(band_role)
    
  


bot.run(TOKEN)