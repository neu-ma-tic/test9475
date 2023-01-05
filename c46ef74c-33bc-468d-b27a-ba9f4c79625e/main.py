import os
import urllib

import discord

import imgkit

from discord.ext import commands

from html2image import Html2Image

PATH = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(PATH, 'images')
hti = Html2Image(output_path=IMAGE_PATH)
print(IMAGE_PATH)


def search_in_google(q):
    name = urllib.parse.urlencode(dict(q=q))
    print(name)
    # imgkit.from_url(f'https://www.google.com/search?q={q}', f'{name}.jpg')
    hti.screenshot(url=f'https://www.google.com/search?q={q}', save_as=f'{name}.png')
    return f'{name}.png'


class Google(commands.Cog):
    @commands.command()
    async def search(self, ctx: commands.Context, *, q):
        pic_name = search_in_google(q)
        print(pic_name)
        await ctx.send('Your search result', file=discord.File(os.path.join(IMAGE_PATH, pic_name)))


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    description='Search in google and return result'
)

bot.add_cog(Google(bot))


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


if __name__ == '__main__':
    bot.run(os.getenv('BOT_TOKEN'))
