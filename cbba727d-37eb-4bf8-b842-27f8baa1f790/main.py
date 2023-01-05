#導入 Discord.py
import discord
import requests
from bs4 import BeautifulSoup
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user: return
    #如果包含 ping，機器人回傳 pong
    if message.content[0] == '!':
        queryStr = message.content[1:]
        for i in range(len(queryStr)):
            if queryStr[i].isascii():
                queryStr = queryStr[:i] + ' ' + queryStr[i:]
                queryStr = queryStr.split()
                break
        if len(queryStr) == 2:
            try:
                lawDict = {"憲法":"https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=A0000001",
                        "民法":"https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0000001",
                        "民訴":"https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=B0010001",
                        "刑法":"https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=C0000001",
                        "刑訴":"https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=C0010001"
                        }
                url = lawDict[queryStr[0]] + "&flno=" + queryStr[1]
                resp = requests.get(url)
                soup = BeautifulSoup(resp.text, 'lxml')
                art = soup.select('div.law-article')[0].find_all('div')
                for i in art:
                    print(i.text)
                    await message.channel.send(i.text + "\n")
            except:
                pass
#TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
client.run('OTM0ODQ2MDYxNTA2MzM0NzQy.Ye2BPQ.4FRER46JDoSa9V0iyPF1G4dp2oo') 