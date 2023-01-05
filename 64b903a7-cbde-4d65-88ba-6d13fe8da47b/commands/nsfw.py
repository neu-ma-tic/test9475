import discord, requests, json, os, asyncio

from io import BytesIO
from discord.ext import commands
from discord_components import Button
from NHentai.nhentai_async import NHentaiAsync
from random import choice
from pysaucenao import SauceNao, PixivSource, VideoSource, AnimeSource

class NSFW(commands.Cog, description='lewd stuffs'):
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.command(description='Randomize rule34.xxx stuffs with a tag', help='r34 <tag>\nEg: r34 yourmom\nr34 skadi_(arknights)')
    async def r34(self, ctx: commands.Context, tag: str):
      url = f'https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}&json=1'
      try:
        r = requests.get(url)
        json_data = json.loads(r.content)
        the_choice = choice(json_data)
        return await ctx.send(the_choice['file_url'])
      except requests.HTTPError:
        return await ctx.send('Nothing found')
      except requests.TooManyRedirects:
        return await ctx.send('Request exceeds the configured number of maximum redirections')
      except requests.Timeout:
        return await ctx.send('Request times out')
      except requests.ConnectTimeout:
        return await ctx.send('Connection times out')
      except requests.ConnectionError:
        return await ctx.send('Connection error')
      except:
        return await ctx.send('Nothing found')

    @commands.command()
    async def pic(self, ctx: commands.Context, category: str):
      my_choice = None
      if category == 'A2':
        with open('data_file/A/2.txt', 'r') as f:
          my_choice = choice(f.read().split())
      elif category == 'A3':
        with open('data_file/A/3.txt', 'r') as f:
          my_choice = choice(f.read().split())
      elif category == 'N2':
        with open('data_file/N/2.txt', 'r') as f:
          my_choice = choice(f.read().split())
      elif category == 'N3':
        with open('data_file/N/3.txt', 'r') as f:
          my_choice = choice(f.read().split())
      if not my_choice:
        return await ctx.send('Please provide a valid category')
      prefix = os.environ['Coll']
      url = f'{prefix}{my_choice}'
      data = requests.get(url).content
      return await ctx.send(
        file=discord.File(
          fp=BytesIO(data),
          filename='result.png'
        )
      )
      '''embed = discord.Embed(
        title=f'{ctx.author.display_name} requests a {category}',
        description='Please enjoy',
        color=0x7821db
      )
      embed.set_image(url=url)
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      return await ctx.send(embed=embed)'''


      

    
    def list_to_string(self, li: list):
        return ' | '.join([i for i in map(lambda x: f'`{x}`', li)])


    async def read(self, ctx: commands.Context, doujin):
      pages = doujin.images

      page = 0 

      message = await ctx.send(pages[page], components=[
          [
            Button(label='Prev'),
            Button(label='Next')
          ]
        ])

      def check(res):
          return res.channel == ctx.channel and res.message == message

      while True:
          try:
            res = await self.bot.wait_for('button_click', timeout=120.0, check=check)
            if res.component.label == 'Prev':
              page -= 1
            if res.component.label == 'Next':
              page += 1
            if page >= len(pages):
              page = 0
            if page <= -1:
              page = len(pages) - 1
            await res.respond(
              type=7,
              content=pages[page],
              components=[
                [
                  Button(label='Prev'),
                  Button(label='Next')
                ]
              ]
              )
          except asyncio.TimeoutError:
            return await message.edit(components=[])



    @commands.command(description='Randomize a doujin', help='nrandom\nEg: nrandom')
    async def nrandom(self, ctx: commands.Context):
        nhentai = NHentaiAsync()
        doujin = await nhentai.get_random()
        description = f'''
**ID:** `{doujin.id}`
**Tag(s):** {self.list_to_string(doujin.tags)}
**Artist(s):** {self.list_to_string(doujin.artists)}
**Character(s):** {self.list_to_string(doujin.characters)}
**Parodies:** {self.list_to_string(doujin.parodies)}
**Total Pages:** `{doujin.total_pages}`
'''
        embed = discord.Embed(title=doujin.title, description=description, color=0xd970ff)
        embed.set_image(url=doujin.images[0])
        message = await ctx.send(
          embed=embed,
          components = [[
            Button(label='Read here', style=1),
            Button(label='Read on web', style=5, url=f'https://nhentai.net/g/{doujin.id}')
          ]]
        )
        try:
          interaction = await self.bot.wait_for(
            'button_click',
            check=lambda x: x.message == message and x.component.label == 'Read here',
            timeout=120.0
          )
          await interaction.respond(
            type=7,
            embed=embed,
            components=[
              Button(label='Read on web', style=5, url=f'https://nhentai.net/g/{doujin.id}')
            ]
          )
          return await self.read(ctx, doujin)
        except:
          return await message.edit(
            embed=embed,
            components=[
              Button(label='Read on web', style=5, url=f'https://nhentai.net/g/{doujin.id}')
            ]
          )


    @commands.command(description='Search for a doujin with code', help='ncode <code>\nEg: ncode 228922')
    async def ncode(self, ctx: commands.Context, code: str):
        nhentai = NHentaiAsync()
        doujin = await nhentai.get_doujin(id=code)
        description = f'''
**ID:** `{doujin.id}`
**Tag(s):** {self.list_to_string(doujin.tags)}
**Artist(s):** {self.list_to_string(doujin.artists)}
**Character(s):** {self.list_to_string(doujin.characters)}
**Parodies:** {self.list_to_string(doujin.parodies)}
**Total Pages:** `{doujin.total_pages}`
'''
        embed = discord.Embed(title=doujin.title, description=description, color=0xd970ff)
        embed.set_image(url=doujin.images[0])
        message = await ctx.send(
          embed=embed,
          components = [[
            Button(label='Read here', style=4),
            Button(label='Read', style=5, url=f'https://nhentai.net/g/{doujin.id}')
          ]]
        )
        try:
          interaction = await self.bot.wait_for(
            'button_click',
            check=lambda x: x.message == message and x.component.label == 'Read here',
            timeout=120.0
          )
          await interaction.respond(
            type=7,
            embed=embed,
            components=[
              Button(label='Read on web', style=5, url=f'https://nhentai.net/g/{doujin.id}')
            ]
          )
          return await self.read(ctx, doujin)
        except:
          return await message.edit(
            embed=embed,
            components=[
              Button(label='Read on web', style=5, url=f'https://nhentai.net/g/{doujin.id}')
            ]
          )

    @commands.command(description='Search using name', help='nquery [keyword]')
    async def nquery(self, ctx: commands.Context, *, query: str):
      nhentai = NHentaiAsync()
      Search = await nhentai.search(
        query=query,
        sort='popular',
        page=1
      )
      dcount = len(Search.doujins)
      if not dcount:
        return await ctx.send('Nothing found')
      dpos, page = 0, 1
      total_pages = Search.total_results // 25 + 1 if Search.total_results % 25 != 0 else Search.total_results // 25
      embed = discord.Embed(
        title=Search.doujins[dpos].title,
        description=f'''
**ID:** {Search.doujins[dpos].id}
**Language:** {Search.doujins[dpos].lang}
        ''',
        color=0xd970ff
      )
      embed.set_image(url=Search.doujins[dpos].cover)
      embed.set_footer(text=f'{dpos + 1}/{dcount}\nPage {page}/{total_pages}')
      comp = [
          [
            Button(label='Prev Doujin', style=1, id='1'),
            Button(label='Next Doujin', style=1, id='2')
          ],
          [
            Button(label='Prev Page', style=4, id='3'),
            Button(label='Next Page', style=3, id='4')
          ],
          [
            Button(label='Read on web', style=5, url=Search.doujins[dpos].url)
          ]
        ]
      
      message = await ctx.send(
        embed=embed,
        components=comp
      )



      while True:
        try:
          interaction = await self.bot.wait_for(
            'button_click',
            check=lambda x: x.message == message,
            timeout=120.0
          )
          button = interaction.component.id
          if button == '1':
            dpos -= 1
          if button == '2':
            dpos += 1
          if button == '3':
            page = page - 1 if page > 1 else total_pages
            Search = await nhentai.search(
              query=query,
              sort='popular',
              page=page
            )
            dcount = len(Search.doujins)
            dpos = 0
          if button == '4':
            page = page + 1 if page < total_pages else 1
            Search = await nhentai.search(
              query=query,
              sort='popular',
              page=page
            )
            dcount = len(Search.doujins)
            dpos = 0
          if dpos < 0:
            dpos = dcount - 1
          if dpos >= dcount:
            dpos = 0
          embed.title = Search.doujins[dpos].title
          embed.description = f'''
**ID:** {Search.doujins[dpos].id}
**Lang:** {Search.doujins[dpos].lang}
          '''
          embed.set_image(url = Search.doujins[dpos].cover)
          embed.set_footer(text=f'{dpos + 1}/{dcount}\nPage: {page}/{total_pages}')
          await interaction.respond(
            type=7,
            embed=embed,
            components=comp
          )
            
        except asyncio.TimeoutError:
          return await message.edit(
            embed=embed,
            components=[
              Button(label='Read on web', style=5, url=Search.doujins[dpos].url)
            ]
          )

    @commands.command(description='Directly read a doujin', help='nread <code> (page)\nEg: nread 228922')
    async def nread(self, ctx: commands.Context, code: str, start_page: str = '0'):

        nhentai = NHentaiAsync()
        doujin = await nhentai.get_doujin(id=code)
        return await self.read(ctx, doujin)
        
    @commands.command()
    async def sauce(self, ctx: commands.Context, minimum: str = None):
      def check():
        try:
          x = float(minimum)
          if 1 <= x <= 100:
            return True
          return False
        except:
          return False
      if not ctx.message.attachments:
        return await ctx.send('Please attach a file')
      saucenao_key = os.environ['saucenao_api_key']
      _minimum = 50.0 if not check() else float(minimum)
      sauce = SauceNao(
        api_key=saucenao_key,
        min_similarity=_minimum,
      )
      if len(ctx.message.attachments) > 1:
        return await ctx.send('Please attach 1 file at a time')
      file = ctx.message.attachments[0]
      if file.content_type not in {'image/png', 'image/jpeg', 'image/jpg', 'image/gif', 'image/webp'}:
        return await ctx.send('Please attach file that has correct format')
      results = await sauce.from_url(file.proxy_url)
      if not results:
        return await ctx.send('Nothing found')
      result = results[0]
      
      embed = discord.Embed(
          title=result.title,
          description=f'''
Similarity: {result.similarity}% alike
Url: {result.url}
Index: {result.index}
          ''',
          color=0x03eeff
        )
      embed.set_image(url=result.thumbnail)
      return await ctx.send(embed=embed)