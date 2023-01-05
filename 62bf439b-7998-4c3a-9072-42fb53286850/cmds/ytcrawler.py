import discord, json, requests, asyncio, feedparser
from discord.ext import commands
from core.classes import Cog_Extension
from bs4 import BeautifulSoup

with open('cache_yt.json','r', encoding='utf8') as jfile2:
    cache_yt = json.load(jfile2)

with open('yt_url.json','r', encoding='utf8') as jfile3:
    yt_url = json.load(jfile3)


class Ytcrawler(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        print(">> Bot is online <<")

        new_title_yt = []
        new_herf_yt = []
        global dic_yt
        dic_yt = {}
        keys_yt = ['yt_title', 'yt_herf']
        [dic_yt.update({key: []}) for key in keys_yt]

        def yt_get_all_href(url):
            rss = feedparser.parse(url)
            new_title_yt.append(rss.entries[0]['title'])
            new_herf_yt.append(rss.entries[0]['link'])

        for i in range (len(yt_url['yt_url'])):
            dic_yt['yt_title'].append(cache_yt['yt_title'][i])
            dic_yt['yt_herf'].append(cache_yt['yt_herf'][i])

        async def ytcrawler2():
            for i in range (len(yt_url['yt_url'])):
                yt_get_all_href(url = yt_url['yt_url'][i])

        async def ytupdate():
            for i in range (len(dic_yt['yt_title'])):
                if (new_herf_yt[i] not in dic_yt['yt_title']):
                    await self.channel.send(new_title_yt[i] + str('\n') + new_herf_yt[i])
            dic_yt['yt_title'] = new_title_yt.copy()
            dic_yt['yt_herf'] = new_herf_yt.copy()
            with open('cache_yt.json','w', encoding='UTF-8') as f:
                json.dump(dic_yt, f, indent=4, ensure_ascii=False)


        self.channel = self.bot.get_channel(816684011207917640)

        while not self.bot.is_closed():
            try:
                await ytcrawler2()
                await ytupdate()

            except:
                pass

            new_title_yt.clear()
            new_herf_yt.clear()

            await asyncio.sleep(600)
    
    @commands.command()
    async def yt(self, ctx, ch):
        if (ch.startswith('https://www.youtube.com/channel/') or ch.startswith('https://youtube.com/channel/')):
            yt_url['yt_url'].append('https://www.youtube.com/feeds/videos.xml?channel_id=' + ch[-24:])
            with open('yt_url.json','w', encoding='UTF-8') as f:
                json.dump(yt_url, f, indent=4, ensure_ascii=False)
            dic_yt['yt_title'].append('0')
            dic_yt['yt_herf'].append('0')
            with open('cache_yt.json','w', encoding='UTF-8') as f:
                json.dump(dic_yt, f, indent=4, ensure_ascii=False)
            await ctx.send(f'Success')
        else :
            await ctx.send(f'Fail')

    @commands.command()
    async def ytremove(self, ctx, ch):
        if (ch.startswith('https://www.youtube.com/channel/') or ch.startswith('https://youtube.com/channel/')):
            yt_url['yt_url'].remove('https://www.youtube.com/feeds/videos.xml?channel_id=' + ch[-24:])
            with open('yt_url.json','w', encoding='UTF-8') as f:
                json.dump(yt_url, f, indent=4, ensure_ascii=False)
            await ctx.send(f'Success')
        else:
            await ctx.send(f'Fail')
def setup(bot):
    bot.add_cog(Ytcrawler(bot))