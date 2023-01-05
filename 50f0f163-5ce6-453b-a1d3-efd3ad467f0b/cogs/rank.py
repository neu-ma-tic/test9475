import discord
from discord.ext import commands, tasks
import pymongo
from pymongo import MongoClient
import os

cluster_url = os.environ.get("mongocluster")
rank_cluster = MongoClient(cluster_url)
db = rank_cluster['discord']
racol = db['leveling']

async def get_level(guild, user):
  levels = racol.find({"guild":str(guild),"user":str(user)})
  for i in levels:
    return i["levels"]
async def get_xp(guild, user):
  levels = racol.find({"guild":str(guild),"user":str(user)})
  for i in levels:
    return i["xp"]

async def open_rank(user, guild):
    if racol.find({"guild":str(guild),"user":str(user)}).count() > 0:
      return False
    else:
        racol.insert_one({"guild": str(guild), "user":str(user), "levels":1,"xp":0})
    return True



class rank(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author == self.client.user:
        return
    if message.guild.id == 681882711945641997:
      return
    await open_rank(message.author.id,message.guild.id)
    racol.update_one({"guild":str(message.guild.id),"user":str(message.author.id)},{"$inc":{"xp":5}})
    
    
    txp = 100 * await get_level(message.guild.id, message.author.id)

    if await get_xp(message.guild.id, message.author.id) >= txp and 'spam' not in message.channel.name:
      try:
        racol.update_one({"guild":str(message.guild.id),"user":str(message.author.id)},{"$inc":{"levels":1}})
        racol.update_one({"guild":str(message.guild.id),"user":str(message.author.id)},{"$set":{"xp":0}})
        await message.channel.send(f'Well done **{message.author.name}**! ! You leveled up to **level: {await get_level(message.guild.id, message.author.id)}!**')
        if await get_level(message.guild.id, message.author.id) == 5:
          guild = message.guild
          ActiveRole = discord.utils.get(guild.roles, name="Active Program(lvl 5+)")
          await message.author.add_roles(ActiveRole)
        if await get_level(message.guild.id, message.author.id) == 10:
          guild = message.guild
          MegaRole = discord.utils.get(guild.roles, name="Mega Active Program(lvl 10+)")
          await message.author.add_roles(MegaRole)
        if await get_level(message.guild.id, message.author.id) == 15:
          guild = message.guild
          SuperRole = discord.utils.get(guild.roles, name="Super Active Program(lvl 15+)")
          await message.author.add_roles(SuperRole)
        if await get_level(message.guild.id, message.author.id) == 20:
          guild = message.guild
          UltimateRole = discord.utils.get(guild.roles, name="Ultimate Active Program(lvl 20+)")
          await message.author.add_roles(UltimateRole)
      except:
        pass


  @commands.command()
  async def rank(self,ctx, member:discord.Member = None):
    
    if member == None:
      await open_rank(ctx.author.id, ctx.guild.id)
      txp = 100 * await get_level(ctx.guild.id, ctx.author.id)
      xp = await get_xp(ctx.guild.id, ctx.author.id)
      level = await get_level(ctx.guild.id, ctx.author.id)


      levelsandxp = racol.find({"guild": str(ctx.guild.id)})
      all_levels = []
      for i in levelsandxp:
        all_levels.append(i["levels"] + i["xp"])
        

      all_levels.sort(reverse=True)
      rank = 1
      for x in all_levels:
        if (await get_level(ctx.guild.id,ctx.author.id) + await get_xp(ctx.guild.id,ctx.author.id)) == x:
          break

        rank += 1
        


      tbox = 20
      sxp = xp/txp
      boxes = int(sxp*tbox)
      embed = discord.Embed(title="{}'s level  stats".format(ctx.author.name), color=discord.Color.random())
      embed.add_field(name="Name", value=ctx.author.mention, inline=True)
      embed.add_field(name="XP", value=f"{xp}/{txp}", inline=True)
      embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
      embed.add_field(name="level", value=f"{level}")
      embed.add_field(name="Progress Bar [lvl]", value=boxes * ":blue_square:" + (tbox-boxes) * ":white_large_square:",
                          inline=False)
      try:
        embed.set_thumbnail(url=ctx.author.display_avatar)
      except:
        embed.set_thumbnail(url='https://static.wikia.nocookie.net/discordian-republic/images/1/10/3.png/revision/latest?cb=20210327224009')
      
      await ctx.send(embed=embed)
    else:
        await open_rank(member.id, member.guild.id)
        txp = 100 * await get_level(ctx.guild.id, member.id)
        xp = await get_xp(member.guild.id, member.id)
        level = await get_level(ctx.guild.id, member.id)



        levelsandxp = racol.find({"guild": str(ctx.guild.id)})
        all_levels = []
        for i in levelsandxp:
          all_levels.append(i["levels"] + i["xp"])
          

        all_levels.sort(reverse=True)

        rank = 1
        for x in all_levels:
          if (await get_level(ctx.guild.id,member.id) + await get_xp(ctx.guild.id,member.id)) == x:
            break

          rank += 1
            
          


        tbox = 20
        sxp = xp/txp
        boxes = int(sxp*tbox)
        embed = discord.Embed(title="{}'s level  stats".format(member.name), color=discord.Color.random())
        embed.add_field(name="Name", value=member.mention, inline=True)
        embed.add_field(name="XP", value=f"{xp}/{txp}", inline=True)
        embed.add_field(name="Rank", value=f"{rank}/{member.guild.member_count}", inline=True)
        embed.add_field(name="level", value=f"{level}")
        embed.add_field(name="Progress Bar [lvl]", value=boxes * ":blue_square:" + (tbox-boxes) * ":white_large_square:",
                              inline=False)
        try:
          embed.set_thumbnail(url=member.display_avatar)
        except:
          embed.set_thumbnail(url='https://static.wikia.nocookie.net/discordian-republic/images/1/10/3.png/revision/latest?cb=20210327224009')
        await ctx.send(embed=embed)


  @commands.command(aliases = ["lb"])
  async def leaderboard(self,ctx,x = 5):
        await open_rank(ctx.author.id, ctx.guild.id)
        levelsandxp = racol.find({"guild": str(ctx.guild.id)})
        all_levels = []
        all_names = []
        for i in levelsandxp:
          all_levels.append(i["levels"])
          all_names.append(self.client.get_user(int(i['user'])))
          
        
        all_levels.sort(reverse=True)

        index = 0
        em = discord.Embed(title = f"{ctx.guild.name}'s Leader Board" , description = "This is decided on the basis of how active you are on the server",color = discord.Color.random())

        for j, i  in zip(all_levels,all_names):
          if index == x:
                break
          else:
                index += 1
              
                em.add_field(name = f"{index}. {i}" , value = f"Level {j}",  inline = False)
        
        em.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.display_avatar)
        await ctx.send(embed = em)

def setup(client):
  client.add_cog(rank(client))
  