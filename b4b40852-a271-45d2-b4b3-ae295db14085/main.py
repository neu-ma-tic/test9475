import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run('ODU2NzAzNDQyODc3MTUzMjkw.YNE5QQ.oMbiBk-Gu16NftUAXzpEdvvqeQg')

@client.evnt
async def on_member_update(before, after):
  games = ['vrchat', 'blender']
  if after.activity and after.activity.name.lower() in games:
    print('Playing a game')
    role = discord.utils.get(after.guild.roles, name=after.activity)
    await after.add_roles(role)
  elif before.activity and before.activity.name.lower() in games and not after.activity:
    print('Stopped playing a game')
    role = discord.utils.get(after.guild.roles, name=after.activity)
    if role in after.roles:
      await after.remove_roles(role)
  