
import discord
from discord.ext import commands
from discord.utils import get
from replit import db

class Jobs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name='job', help='See your job title')
  async def seeJob(self, ctx):
    if "jobs" in db.keys():
      jobs = db["jobs"]
      active_jobs = []
      roles = ctx.author.roles[1:]
      for r in roles:
        if r.name in jobs:
          active_jobs.append(r.name)
      if active_jobs:
        await ctx.send(f"```\n{ctx.author.display_name}\'s Jobs:\n" + "\n".join(active_jobs) + "\n```")
      else:
        await ctx.send("Looks like you\'re unemployed. We don't give handouts so get a job!")

  @commands.command(name='job-set', help='Start a new job')
  async def giveRole(self,ctx, role_name):
    role = get(ctx.message.guild.roles, name=role_name)
    if 'jobs' in db.keys() and role:
      jobs = db['jobs']
      if role.name in jobs:
        await ctx.author.add_roles(role)
        await ctx.send(f"Hey {ctx.author.display_name} you are now a {role}")
    else:
      await ctx.send(f"Hmmm, doesn't look like {role_name} is on the job list")

  @commands.command(name='job-quit', help='Quit your job')
  async def quitRole(self,ctx, role_name):
    role = get(ctx.message.guild.roles, name=role_name)
    if 'jobs' in db.keys() and role:
      jobs = db['jobs']
      if jobs:
        active_jobs = []
        roles = ctx.author.roles[1:]
        for r in roles:
          if r.name in jobs:
            active_jobs.append(r.name)
        if role.name in active_jobs:
          await ctx.author.remove_roles(role)
          await ctx.send(f"You are no longer employed as a {role.name}")
        else:
          await ctx.send("You can't quit a job you don't have silly")

      else:
        await ctx.send(f"Hmmm, doesn't look like {role_name} is on the job list")
    else:
      await ctx.send(f"Hmmm, doesn't look like {role_name} is on the job list")

  @commands.command(name='job-list', help='See a list of all job titles')
  async def seeRoles(self,ctx):
    if 'jobs' in db.keys():
      jobs = db['jobs']
      if jobs:
        await ctx.send("```\nJob List:\n" + "\n".join(jobs) + "\n```")
      else:
        await ctx.send("There are no jobs on the job list. Maybe we should add some")

  @commands.command(name='job-add', help='Add new Job titles for town members (ADMIN)')
  @commands.has_role("Admin")
  async def addRoles(self,ctx,job):
    if 'jobs' in db.keys():
      jobs = db['jobs']
      if job in jobs:
        await ctx.send(f"{job} is already on the job list")
        return
      jobs.append(job)
      db['jobs'] = jobs
      await ctx.guild.create_role(name=job)
      await ctx.send(f"I added a new role for the {job} job!")
    else:
      db['jobs'] = [job]
      await ctx.guild.create_role(name=job)
      await ctx.send(f"I added a new role for the {job} job!")
    

  @commands.command(name='job-remove', help='Delete an existing job (ADMIN)')
  @commands.has_role("Admin")
  async def delRoles(self,ctx,job):
    if 'jobs' in db.keys():
      jobs = db['jobs']
      if jobs == []:
        await ctx.send("There are no jobs... so you can't delete that... Silly Goose")
      role = get(ctx.message.guild.roles, name=job)
      if job in jobs:
        del jobs[jobs.index(job)]
        db['jobs'] = jobs
        if role:
          await role.delete()
        await ctx.send(f"{job} was removed from the job list")
      else:
        await ctx.send(f"{job} is not on the job list")
    else:
      await ctx.send("There are no jobs... so you can't delete that... Silly Goose")

class Profile(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  def _getProfile(self, user: discord.Member):
    if "jobs" in db.keys():
      jobs = db["jobs"]
      active_jobs = []
      job_status = ''
      roles = user.roles[1:]
      for r in roles:
        if r.name in jobs:
          active_jobs.append(r.name)
      if active_jobs:
        job_status = ', '.join(active_jobs)
      else:
        job_status = 'unemployed'
      name = user.display_name
      return "```\nUser Profle:\n" + "\nName: "+ name + "\nJobs: " + job_status + "\n```"
    return

  

class Info(commands.Cog):

  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name='commands', help='Sends server plugin commands link')
  async def comInfo(self,ctx):
    link = "https://github.com/catch441/Ultimate_Economy/wiki"
    await ctx.send(link)
        