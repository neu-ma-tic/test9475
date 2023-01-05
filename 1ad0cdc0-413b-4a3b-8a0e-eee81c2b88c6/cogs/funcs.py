import discord
from discord.ext import commands
import random
import requests
import json
from replit import db


class Funcs(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Funcs Cog loaded')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms ')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
                     "Very doubtful.", "Without a doubt.",
                     "Yes.", "Yes – definitely.", "You may rely on it."]
        await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member: commands.MemberConverter, *, reason='No reason'):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} was kicked for {reason}')

    @commands.command()
    async def ban(self, ctx, member: commands.MemberConverter, *, reason='No reason'):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was banned for {reason}')

    @commands.command()
    async def unban(self, ctx, *, member):
        unbanned = False
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} was unbanned and can come back anytime')
                unbanned = True

        if not unbanned:
            await ctx.send(f'{member} is not part of the banned users list')

    @commands.command(aliases=['me'])
    async def meme(self, ctx):
      content = requests.get("https://meme-api.herokuapp.com/gimme").text
      data = json.loads(content,)
      meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
      await ctx.reply(embed=meme)

    @commands.command()
    async def deon(self, ctx):
        await ctx.send(f'{ctx.author.mention} said Deon is dumb and we all agree', tts=True)

    @commands.command(aliases=['cf'])
    async def CoinFlip(self, ctx, member: discord.Member, member2: discord.Member):
        members = [member, member2]
        em = discord.Embed(title='Coin Flipping', color=discord.Color.blue())
        em.add_field(name='Players', value=f'{member.mention} vs. {member2.mention}', inline=False)
        winner = random.choice(members)
        em.add_field(name='Winner', value=f'{winner.mention}', inline=False)
        em.set_footer(text='Bot created by Eggnogg')
        await ctx.send(embed=em)

    @commands.command(aliases=['cg'])
    async def chooseGame(self, ctx, *, game):
        games = game.split(' ')
        chosen_game = random.choice(games)
        em = discord.Embed(title='Choosing Game:', color=discord.Color.blue())
        em.add_field(name='List of Games:', value=f'{games}', inline=False)
        em.add_field(name='Chosen Game:', value=f'{chosen_game}', inline=False)
        em.set_footer(text='Bot created by Eggnogg')
        await ctx.send(embed=em)

    @commands.command()
    async def luan(self, ctx):
        await ctx.send(f'{ctx.author.mention} said Luan is a simp and we all know it is true', tts=True)

    @commands.command()
    async def spam(self, ctx, member: discord.Member, amount, *, message):
        await ctx.channel.purge(limit=1)
        for i in range(int(amount)):
            await ctx.send(f'{member.mention} {message}')

    # be nice
    @commands.Cog.listener()
    async def on_message(self, msg):
        words = ['fok', 'FOK', 'Fok', 'fuck', 'Fuck', 'fokkit', 'Fokkit', 'FUCK', 'FOKKIT','fag','faggot','bitch','shit','FOk','SHIT','FAG','FAggot','dick','kak','Dick','Kak','KAK','wanker','cunt']
        dm = await msg.author.create_dm() 
        for word in words:
            if word in msg.content:
                message = await dm.send(f'{msg.content} was not a nice thing to say {msg.author.mention}')
                await message.add_reaction('⛔')
            else:
                pass
          
    @commands.command()
    async def penis(self, ctx):
        string = "8"
        r = random.randint(0,20)
        for i in range(0,r):
          string = string + '='
        string+='D'
        await ctx.reply(string)

    @commands.command()
    async def dian(self, ctx):
        await ctx.send('Dian sucks at F1 and we all know it is true.', tts=True)

    @commands.command()
    async def setup(self, ctx):
      channel = discord.utils.get(ctx.guild.text_channels, name='music-commands')
      if channel is None:
        channel = await ctx.guild.create_text_channel('music-commands')

        channel = discord.utils.get(ctx.guild.text_channels, name='music-commands')
        channel_id = channel.id
        print(f'{channel}   {channel_id}')
        em = discord.Embed(title='Music Channel', color=discord.Color.blue())
        em.add_field(name='What does this channel do', value='Type song name or paste song url in channel to play it or add it to queue. React to control the music',inline=False)
        em.add_field(name='Pause:', value='React with ⏸ to pause song',inline=False)
        em.add_field(name='Resume:', value='React with ⏯ to resume song',inline=False)
        em.add_field(name='Skip:', value='React with ⏭ to skip song',inline=False)
        em.add_field(name='Stop:', value='React with ⏹️ to stop song', inline=False)
        em.add_field(name='Shuffle:', value='React with 🔀 to shuffle songs in he current queue', inline=False)
        em.set_footer(text='Bot created by Eggnogg')
        msg = await channel.send(embed=em)

        await msg.add_reaction('⏸')
        await msg.add_reaction('⏯')
        await msg.add_reaction('⏭')
        await msg.add_reaction('🔀')
        await msg.add_reaction('⏹️')
        

        msg_id = msg.id
        db[str(ctx.guild.id)] = msg_id
        
      else:
        await ctx.send('Already exsists')

def setup(client):
  client.add_cog(Funcs(client))