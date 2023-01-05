import discord, json, requests, asyncio, feedparser
from discord.ext import commands
from core.classes import Cog_Extension
from bs4 import BeautifulSoup

with open('cache_ptt.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Crawler(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def ptt_crawler():
            await self.bot.wait_until_ready()
            
            ptt_url = 'https://www.ptt.cc/bbs/Lifeismoney/index.html'

            new_title_ptt = []
            new_herf_ptt = []
            dic_ptt = {}
            keys_ptt = ['ptt_money_title', 'ptt_money_herf']
            [dic_ptt.update({key: []}) for key in keys_ptt]
            def ptt_get_all_href(url):
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                results = soup.select("div.title")
                for item in results:
                    a_item = item.select_one("a")
                    title = item.text
                    if title.startswith('\n[情報]'):
                        if a_item:
                            new_title_ptt.append(title.strip())
                            new_herf_ptt.append('https://www.ptt.cc' + a_item.get('href'))
            for i in range (len(jdata['ptt_money_title'])):
                dic_ptt['ptt_money_title'].append(jdata['ptt_money_title'][i])
                dic_ptt['ptt_money_herf'].append(jdata['ptt_money_herf'][i])

            async def update():
                for i in range (len(new_herf_ptt)):
                    if (new_title_ptt[i] not in dic_ptt['ptt_money_title']):
                        await self.channel.send(new_title_ptt[i] + str('\n') + new_herf_ptt[i])
                dic_ptt['ptt_money_title'] = new_title_ptt.copy()
                dic_ptt['ptt_money_herf'] = new_herf_ptt.copy()
                with open('cache_ptt.json','w', encoding='UTF-8') as f:
                    json.dump(dic_ptt, f, indent=4, ensure_ascii=False)

            while not self.bot.is_closed():
                self.channel = self.bot.get_channel(832152942110834758)
                ptt_get_all_href(url = ptt_url)

                try:
                    await update()

                except:
                    pass
                
                new_title_ptt.clear()
                new_herf_ptt.clear()

                await asyncio.sleep(1800)

        self.bg_task = self.bot.loop.create_task(ptt_crawler())


def setup(bot):
    bot.add_cog(Crawler(bot))