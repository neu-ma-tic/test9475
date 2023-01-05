import discord
from discord.ext import commands


def is_it_me(ctx):
    return ctx.author.id == 696617859580690512

def is_patron():
  print('not finished')

def me_andpeople(ctx):
  if ctx.author.guild_permissions.administrator:
    return True

  elif ctx.author.name == 'RunTheProgram':
    return True

  else:
    return False