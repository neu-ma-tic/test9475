import discord
from discord.ext import commands
import asyncio
import aiofiles
from datetime import datetime
import pytz
import re
import utils.checks as checks

owner_id = 696617859580690512



def get_rid(ctx, role_input):
	role_name = ""
	for obj in role_input:
		role_name += "%s " %obj
	role_name = role_name.strip()

	#first trying regex to get the id from the message itself (is the case by mention or role ID as intput)
	role_id = re.search(r"\d{18}", role_name)
	roles_list = [] #initializing return list
	if role_id != None: #checking if re found something
		role_id = role_id.group(0) #getting readable id
		roles_list.append(int(role_id)) #getting and appending role-id to list
		#return roles_list, len(roles_list)
	#if role-name was given
	else:
		#iterating through roles, searching for name match (case sensitive)
		for g_role in ctx.guild.roles:
			if role_name in str(g_role.name):
				roles_list.append(int(g_role.id)) #appending to list

	return roles_list, len(roles_list)

def is_it_me(ctx):
    return ctx.author.id == 696617859580690512

class moderation(commands.Cog):
  def __init__(self,client):
    self.client = client
    client.warnings = {}
    client.sniped_messages = {}


  

  @commands.Cog.listener()
  async def on_ready(self):
    
    print("it's ready hoperully lol")
    while True:
        await asyncio.sleep(10)
        with open("txts/spam_detect.txt", "r+") as file:
            file.truncate(0)

  @commands.command()
  async def serverinfo(self, ctx):

    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        
    embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
    embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    embed2.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)


    embed2.add_field(name='Number of roles', value=str(role_count), inline=False)
    embed2.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
    embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed2.set_thumbnail(url=ctx.guild.icon.url)
    embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
    embed2.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar.url)

    await ctx.send(embed=embed2)


  @commands.command()
  async def userinfo(self,ctx, *, user: discord.Member = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar.url)
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)




  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    print('literally nothing')

  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author == self.client.user:
        return
    if message.guild.id != 681882711945641997 and message.guild.id != 878134089968943215:     
      b = open("txts/rickroll.txt", 'r', encoding='utf-8')
      rick = b.read().split()
      msg = message.content
      if message.author.id != owner_id:
          if any(word in msg for word in rick):
              await message.channel.purge(limit=1)
              await message.channel.send(
                  f'{message.author.mention} Imagine trying to rickroll smh\nhttps://tenor.com/view/smh-kanyewest-gif-4544077')

          if 'http' in message.content and 'rickroll' in message.content or 'rick-roll' in message.content:
            await message.channel.purge(limit=1)
            await message.channel.send(
                  f'{message.author.mention} Imagine trying to rickroll smh\nhttps://tenor.com/view/smh-kanyewest-gif-4544077')



      if 'discord.gift' in message.content:
            await message.channel.purge(limit=1)
            member = self.client.get_user(owner_id)
            await member.send(message.content)
      if any(word in message.content for word in ['@everyone', '@here']) and message.author.guild_permissions.administrator is False:
        await message.channel.send("<:lol:899484944512991262> Why did you think that would work")

      #spam detection
      counter = 0
      with open("txts/spam_detect.txt", "r+") as file:
          for line in file:
              if line.strip("\n") == str(message.author.id):
                  counter += 1
          file.writelines(f"{str(message.author.id)}\n")
          if counter > 6 and 'spam' not in message.channel.name:
              guild = message.guild
              mutedRole = discord.utils.get(guild.roles, name="Muted")
              if not mutedRole:
                  mutedRole = await guild.create_role(name="Muted")

                  for channel in guild.channels:
                      await channel.set_permissions(mutedRole,
                                                    speak=False,
                                                    send_messages=False,
                                                    read_message_history=True,
                                                    read_messages=False)
              await message.author.add_roles(mutedRole)
              await message.channel.send(
                  f"{message.author} has being muted for 5 minutes for spamming")
              await message.channel.purge(limit=8)
              await asyncio.sleep(300)
              await message.author.remove_roles(mutedRole)
      
      #badword detector
      f = open("txts/badwords.txt", 'r', encoding='utf-8')
      asdfd = f.read().split()
      msg = message.content.lower()

      if message.author.id != owner_id:
          if '@Bot Program' in message.content and any(word in msg for word in asdfd):
            await message.channel.purge(limit=2)
            await message.channel.send("https://tenor.com/view/kristen-bell-smh-no-nope-not-pleased-gif-14542373 smh imagine trying to bypass swear detector")
          if any(word in msg for word in asdfd):
              await message.channel.purge(limit=1)
              await message.channel.send(
                  f'{message.author.mention}! <:hm:897631244995661885> you are not allowed to send prohibited words in this channel.', delete_after=3)
    

    

  @commands.Cog.listener()
  async def on_message_delete(self,message):
      self.client.sniped_messages[message.guild.id] = (message.content,
                                                  message.author,
                                                  message.channel.name,
                                                  message.created_at)


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def lock(self,ctx, channel : discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embed = discord.Embed(
          description=
          "✅ **Channel Locked**",
          color=discord.Color.green())
      await ctx.send(embed=embed)

  @commands.command()
  @commands.check(checks.me_andpeople)
  async def unlock(self,ctx, channel : discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embed = discord.Embed(
          description=
          "✅ **Channel Unlocked**",
          color=discord.Color.green())
      await ctx.send(embed=embed)

  @commands.command()
  @commands.check(is_it_me)
  async def snipe(self,ctx):
      try:
          contents, author, channel_name, own_time = self.client.sniped_messages[
              ctx.guild.id]

      except:
          await ctx.channel.send("Couldn't find a message to snipe!")
          return

      embed = discord.Embed(description=contents,
                            color=discord.Color.purple(),
                            timestamp=own_time)
      embed.set_author(name=f"{author.name}#{author.discriminator}",
                      icon_url=author.display_avatar)
      embed.set_footer(text=f"Deleted in : #{channel_name}")
      await ctx.channel.send(embed=embed)

  @commands.command()
  @commands.check(checks.me_andpeople)
  async def mute(self,ctx, member: discord.Member, time, *, reason=None):
      guild = ctx.guild
      muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
      if not muted_role:
          muted_role = await guild.create_role(name="Muted")

          for channel in guild.channels:
              await channel.set_permissions(muted_role,
                                            speak=False,
                                            send_messages=False,
                                            read_message_history=True,
                                            read_messages=False)
      embed = discord.Embed(title="muted",
                            description=f"{member.mention} was muted ",
                            colour=discord.Color.light_gray())
      time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
      tempmute = float(time[0]) * time_convert[time[-1]]
      await member.add_roles(muted_role)
      embed = discord.Embed(
          description=
          f"✅ **{member.display_name}#{member.discriminator}** is muted for {time} reason: {reason}",
          color=discord.Color.green())
      await ctx.send(embed=embed)
      await asyncio.sleep(tempmute)
      await member.remove_roles(muted_role)


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def warn(self,ctx, member: discord.Member = None, *, reason=None):
      if member is None:
          return await ctx.send(
              "The provided member could not be found or you forgot to provide one."
          )

      if reason is None:
          return await ctx.send("Please provide a reason for warning this user.")
      tz_NY = pytz.timezone('Australia/Melbourne') 
      t = datetime.now(tz_NY)
      current_time = t.strftime("%H:%M")

      embed = discord.Embed(title=f"You've been warned in {ctx.guild.name}")
      embed.set_author(name="ProgramX",icon_url='https://cdn.discordapp.com/avatars/763315062668001301/a0117e092350cef21f457ec864a1d0d0.png?size=1024')
      embed.add_field(name="Reason",value=reason)
      embed.set_footer(text=f"{ctx.author.name} has being warned • Today at {current_time}")
      await member.send(embed=embed)


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def warnings(self,ctx, member: discord.Member = None):
      if member is None:
          return await ctx.send(
              "The provided member could not be found or you forgot to provide one."
          )

      embed = discord.Embed(title=f"Displaying Warnings for {member.name}",
                            description="",
                            colour=discord.Color.red())
      try:
          i = 1
          for admin_id, reason in self.client.warnings[ctx.guild.id][member.id][1]:
              admin = ctx.guild.get_member(admin_id)
              embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
              i += 1

          await ctx.send(embed=embed)

      except KeyError:  # no warnings
          await ctx.send("This user has no warnings on this server.")

  @commands.command()
  @commands.check(checks.me_andpeople)
  async def clear(self,ctx, amount=10):
      await ctx.channel.purge(limit=amount)


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def slowmode(self,ctx,seconds:int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"The slowmode for this channel has being set to {seconds}")


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def nick(self,ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

  @commands.command(description="Unmutes a specified user.")
  @commands.check(checks.me_andpeople)
  async def unmute(self,ctx, member: discord.Member):
      mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

      await member.remove_roles(mutedRole)
      await member.send(f" you have being unmutedd from: - {ctx.guild.name}")
      embed = discord.Embed(title="unmute",
                            description=f" unmuted-{member.mention}",
                            colour=discord.Color.light_gray())
      await ctx.send(embed=embed)


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def kick(self,ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send('{member} has being kicked for {reason}')


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def ban(self,ctx, member: discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.send(f'{member} has being banned for {reason}')


  @commands.command()
  @commands.check(checks.me_andpeople)
  async def unban(self,ctx, member: discord.Member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')
      for ban_entry in banned_users:
          user = ban_entry.user
          if (user.name, user.discriminator) == (member_name,
                                                member_discriminator):
              await ctx.guild.unban(user)
              await ctx.send(f"{user} has been Unbanned")


def setup(client):
  client.add_cog(moderation(client))