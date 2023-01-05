import discord 
from discord.ext import *

class Commands(discord.ext.commands.Context):

  def __init__(self, ctx, FuncName, Arguments):
    self.FuncName = FuncName
    self.Arguments = Arguments
    self.ctx = ctx
    
  
  def Help(ctx):
    await ctx.message.channel.send('hello')

  def Donate(ctx):
    await ctx.message.channel.send('Donate!')

  def Checker(self, FuncName, Arguments):
    FuncName.strip().upper()
    if(FuncName == 'HELP'):
      self.Help(Arguments)
    elif(FuncName == 'DONATE'):
      self.Donate(Arguments)


class Event(object):

  def __init__(self,):
    pass


