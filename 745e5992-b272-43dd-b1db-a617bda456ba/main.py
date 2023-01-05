#導入 Discord.py
import discord
from discord.ext import commands
#client 是我們與 Discord 連結的橋樑
client = discord.Client()
#調用 event 函式庫
@client.event
#當機器人完成啟動時

#前面有async代表協程
async def on_ready():#機器人成功登陸後
    print('目前登入身份：', client.user)

@client.event
#當有訊息時Called when a Message is created and sent.
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        await message.channel.send('pong')
    #async 意指異步執行，而 await 則是用來驅動 async 函式的必須指令。
@client.event
async def on_member_join(member):
  channel=client.get_channel('enT3rp9S')
  await channel.send(f"{member} welcome!")
async def no_member_remove(member):
  channel=client.get_channel('enT3rp9S')
  await channel.send(f"{member} leave!")
async def add(a: int, b: int):
  if a.auther!=client.user:
    await client.channel.send(a + b)
#加入token
client.run('ODcyMTExNjYxOTI5MDc0NzE5.YQlHRw.FmMdBbqtqj_Wp3HYYDHggyyfwmo') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面