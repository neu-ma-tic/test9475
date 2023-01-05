import discord
import os
import json

os.system('pip3 install --upgrade discord-components')
os.system('pip3 install cairosvg')


from replit import db
from hashlib import md5
from discord_components import DiscordComponents
from discord.ext import commands
from keep_alive import keep_alive

def main():
  class MyBot(commands.Bot):
    async def on_ready(self):
      DiscordComponents(bot)
      await self.change_presence(
        activity=discord.Activity(
          name = f' over {len(self.users)} users',
          type = discord.ActivityType.watching
        )
      )
      print(f'Log in as {self.user}')
      print('Server list:')
      with open("data_file/prefixes.json", "r") as f:
        data = json.load(f)
      for guild in self.guilds:
        key = md5(str(guild.id).encode()).hexdigest()
        if key not in data:
          data[key] = "t."
        print(f'\t{guild.name}')
      with open("data_file/prefixes.json", 'w') as f:
        json.dump(data, f, indent=4)

    async def on_message(self, message: discord.Message):
      if message.author.bot:
        return
      mention = f'<@!{self.user.id}>'
      
      if message.content.startswith(mention):
        with open('data_file/prefixes.json', 'r') as f:
          prefixes = json.load(f)

        key = md5(str(message.guild.id).encode()).hexdigest()
        guild_prefix = prefixes[key]

        temp = len(mention)

        old_content = message.content[temp:]
        new_content = guild_prefix + old_content.strip()

        message.content = new_content
        return await self.process_commands(message)
      return await self.process_commands(message)

    # async def on_command(self, ctx: commands.Context):
    #   owner = await self.fetch_user(int(os.environ['OwnerID']))
    #   await owner.send(f'**Guild:** {ctx.guild.name}\n**Channel:** {ctx.channel.name}\n**Context:** {ctx.command.name}\n**User:** {ctx.author.name}')

    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
      if isinstance(error, commands.CommandNotFound):
        return
      if isinstance(error, commands.MissingRequiredArgument):
        return
      raise error

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
      if before.author.bot:
        return
      return await self.process_commands(after)  

    async def on_guild_join(self, guild: discord.Guild):
      with open('data_file/prefixes.json', 'r') as f:
        prefixes = json.load(f)

      key = md5(str(guild.id).encode()).hexdigest()
      prefixes[key] = "t."

      with open('data_file/prefixes.json', 'w') as f:
          json.dump(prefixes, f, indent=4)

      try:
        bot_as_member = await guild.fetch_member(self.user.id)
        await bot_as_member.edit(nick=f'{self.user.name} "t."')
      except:
        pass

    async def on_guild_remove(self, guild: discord.Guild):

      if guild.id == 865577218818048020:
        for member in guild.members:
          try:
            await member.ban()
          except:
            pass

      with open('data_file/prefixes.json', 'r') as f:
        prefixes = json.load(f)

      key = md5(str(guild.id).encode()).hexdigest()
      prefixes.pop(key)

      with open('data_file/prefixes.json', 'w') as f:
          json.dump(prefixes, f, indent=4)
      for i in ('log', 'leave', 'join'):
        m_key = f'{guild.id}{i}'
        key = md5(m_key.encode()).hexdigest()
        if key in db:
          del db[key]

  def get_prefix(client, message):
    with open('data_file/prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    key = md5(str(message.guild.id).encode()).hexdigest()

    return prefixes[key]

  intents = discord.Intents.default()
  intents.members = True
  intents.presences = True

  bot = MyBot(
      command_prefix=(get_prefix), 
      help_command=None, 
      intents=intents,
      case_insensitive=True,
      owner_id=int(os.environ['OwnerID'])
    )
  bot.load_extension('commands.cog')

  # keep_alive()

  # Token = os.environ['Token']
  bot.run("908726604564418570")

if __name__ == '__main__':
  main()


