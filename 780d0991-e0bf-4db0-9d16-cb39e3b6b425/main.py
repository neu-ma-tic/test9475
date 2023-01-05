import discord
from discord.ext import commands
import requests
import json
import io

with open('config.json','r') as f:
	config = json.load(f)

with open('value.json','r') as f:
	value = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'],help_command=None)
color = discord.Colour(int(config['color'],16))

@bot.event
async def on_ready():
	print(f"Botが正常に起動しました\nBot:{bot.user}")

@bot.command()
async def help(ctx):
  embed=discord.Embed(title="BotHelp",color=color)
  embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
  embed.set_footer(text="Github",icon_url=value['github_icon'])
  embed.add_field(name="コマンド一覧",value="""
	`help` `item` `brnews` `stats` `shop`""",inline=False)
  embed.add_field(name="GitHub",value=f"[Github]({value['github']})",inline=False)
  embed.add_field(name="Botバージョン",value=value['version'],inline=False)
  embed.add_field(name="作成者のBot",value=f"[ここ]({value['creators_bot']})から導入",inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def item(ctx,*,name=None):
  if name == None:
    embed=discord.Embed(title="エラー",description="検索するアイテム名を入力してください",color=color)
    embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
    embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
    await ctx.send(embed=embed)
  else:
    request = requests.get(f"https://fortnite-api.com/v2/cosmetics/br/search/all?name={name}&matchMethod=starts&language=ja&searchLanguage=ja").json()
    if request['status'] == 200:
      for respone in request['data']:
        embed=discord.Embed(title=respone['name'],color=color)
        embed.add_field(name="ID",value=respone['id'],inline=False)
        embed.add_field(name="説明", value=respone['description'],inline=False)
        embed.add_field(name="レアリティ", value=respone['rarity']['displayValue'],inline=False)
        embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
        embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
        if respone['images']['icon'] != None:
          embed.set_thumbnail(url=respone['images']['icon'])
        await ctx.send(embed=embed)
    elif request["status"] == 404:
      embed=discord.Embed(title="エラー",description="アイテムが見つかりませんでした",color=color)
      embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
      embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
      await ctx.send(embed=embed)
    else:
      embed=discord.Embed(title="エラー",description="不明なエラーが発生しました\nAPIがダウンしている可能性があります",color=color)
      embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
      embed.set_footer(text="Github",icon_url=value['github_icon'])
      await ctx.send(embed=embed)				
  
@bot.command()
async def brnews(ctx):	
  request = requests.get("https://fortnite-api.com/v2/news/br?language=ja").json()
  if request['status'] == 200:
    embed=discord.Embed(title="バトルロワイヤルニュース",color=color)
    embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
    embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
    embed.set_image(url=request['data']['image'])
    await ctx.send(embed=embed)
  else:
    embed=discord.Embed(title="エラー",description="ニュースが存在しない場合があります",color=color)
    embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
    embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
    await ctx.send(embed=embed)

@bot.command()
async def stats(ctx,user=None):
  if user == None:
    embed=discord.Embed(title="エラー",description="ユーザーを指定してください",color=color)
    embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
    embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
    await ctx.send(embed=embed)
  else:
    request = requests.get(f"https://fortnite-api.com/v1/stats/br/v2?name={user}&image=all",headers={"Authorization":config['apikey']}).json()
    if request['status'] == 200:
      embed=discord.Embed(title=f"{request['data']['account']['name']}の戦績",color=color)
      embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
      embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
      embed.set_image(url=request['data']['image'])
      await ctx.send(embed=embed)
    elif request['status'] == 403:
      embed=discord.Embed(title="エラー",description="指定したユーザーがキャリアランキング表示をONにしていません",color=color)
      embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
      embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
      await ctx.send(embed=embed)
    elif request['status'] == 404:
      embed=discord.Embed(title="エラー",description="ユーザーが見つかりません",color=color)
      embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
      embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
      await ctx.send(embed=embed)
    elif request['status'] == 401:
      embed=discord.Embed(title="エラー",description="APIKeyが有効でない、または入力されていません",color=color)
      embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
      embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
      await ctx.send(embed=embed)

@bot.command()
async def shop(ctx):
  request = requests.get("https://api.nitestats.com/v1/shop/image")
  if request.status_code == 200:
    embed=discord.Embed(title="デイリーショップ",color=color)
    embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
    embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
    embed.set_image(url="attachment://dailyshop.png")
    await ctx.send(embed=embed,file=discord.File(fp=io.BytesIO(request.content), filename="dailyshop.png"))
  else:
    embed=discord.Embed(title="エラー",description="ショップ画像の取得に失敗しました",color=color)
    embed.set_author(name=bot.user.name,icon_url=bot.user.avatar_url,url=value['github'])
    embed.set_footer(text="p-yttor4869/FortniteBot-For-Discord",icon_url=value['github_icon'])
    await ctx.send(embed=embed)

bot.run(config['token'])
