import datetime
import discord


def local_time(datum = None):
  delta = 2
  if datum == None:
    return datetime.datetime.now() + datetime.timedelta(hours=delta)
  return datum + datetime.timedelta(hours=delta)

  
#TODO get_member_named
def find_member(username, tag, guild) -> discord.Member:
  for member in guild.members:
    if member.name == username and member.discriminator == tag:
      return member
  return None
  