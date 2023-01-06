import discord
from discord.ext import commands 
from core.classes import Cog_Extension
import random,json,bs4,requests


class Bug(Cog_Extension):
  async def get_news(self,ctx):
    text2=''
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',}
    url='https://news.pts.org.tw/'
    htmlfile=requests.get(url,headers=header)
    htmlfile.raise_for_status()
    objsoup=bs4.BeautifulSoup(htmlfile.text,'html.parser')
    if htmlfile.status_code == requests.codes.ok:
        print("成功偽裝取得網頁內容")
        print("網頁內容大小 = ",len(htmlfile.text))
        objTag=objsoup.find_all('div','form-row')
        for context in objTag:
        #    context=context.find('div','')
        #    print(context)
          context1=context.find('a','d-block')
          context=str(context1)
          context=context.lstrip("<a class=\"d-block\" href=\"").rstrip("</a>").replace('>','\n')
          link="https://news.pts.org.tw"+context[0:15]
          #print(link) 
          context=context[16:]
          text=context+'\n'+link
          await ctx.send(text)
    else:
          await ctx.send("無法取得網頁內容")

def setup(bot):
  bot.add_cog(Bug(bot))