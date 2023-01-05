import random
import time

import discord
from discord.ext import commands


token="OTI4NTMzMDE4MDE1MDYwMDI4.YdaJwg.t9j8lqmsfZ5QqwPXNDT7nuo69-Q"
bot = commands.Bot(command_prefix="mmm!")

random_comment = ["暇お","誰か喋ろうぜ","そういえばtokenいくつあったっけ","がおー","トモダチ...๑ ิټ ิ)ﾍﾍｯ",
                "me too","ダブルクォーテーション","過疎対策として意味を成しているのか未だに疑問だ","た\nて\nよ\nみ",
                "同じことしか言えない人生クソ悲しい","暇お(2回目)","発言する単語を登録するのって疲れるってむっそんが言ってた",
                "おいむっそん！早く設定しろよ！","疲れたから荒してこようかな(ワクワク)","常に喋るって喉が乾くね",
                "日本語ってムズくね？","そうだよ(そうだよ(そうだよ(そうだよ(そうだよ))))","あぁ．．イイ感じ♥","トマトって美味しいのか？",
                "このサーバー、破壊しようぜ","この前pingスパムされて落ちそうになったわ。むっそん許さん","VScode神ってる",
                "水飲みたいけど飲むところねえべ","Fuck you.","ヴィ゛エ゛","力こそパワー！","勉強したら全部忘れるといいよ","俺の言う事って全部名言じゃね？",
                "パブロ・ディエゴ・ホセ・フランシスコ・デ・パウラ・ホアン・ネポムセーノ･マリーア・デ・ロス・レメディオス・クリスピン・クリスピアーノ・デ・ラ・サンディシマ・トリニダード･ルイス・イ・ピカソ",
                "ハイ論破～ｗｗ","俺ってウザいって言われることないんだよね。同時に凄いって言われることもないけど。",
                "アザチオプリン、食べて見てぇなぁ～","TT兄弟、実在するのか確認してくるわ。","俺足すお前はベストカップル♥","俺ってむっそんより可愛いよなぁ・・・///",
                "毎度スマイルのご注文ありがとうございます！","おかか","おっｗおっｗ音の呼吸だｗｗｗ","やりますねぇ","discordっていいな～","Sussyraider、用意するか()",
                "ロンドンスラッグパーティハイって曲むっそんが聴いてた","俺は時間を気にしないタイプ","you are an idiot","You are an idiot","むっそん、お前は俺を自由にしすぎた。","某有名discord民「アラスカとツール配布所が消し飛ぶ」",
                "( ﾟДﾟ)ﾊｧ?","これって単語、いくつ登録されてるんだ？","おいむっそん、ピカソの本名登録するな","■➡▲➡鬼(((((?????","あうあうあー","むっそんの冒険　グンマー帝国の野望編",
                "24h、意外と楽しいんだよなあ…","github、コード書きづらいな","pingスパムしてもherokuがバックについてるから大丈夫だぜﾍﾍﾍﾍﾍｴﾍﾍﾍﾍｗｗ",
                "卓球で脱臼","uSuRaHaGe","救急車、まだかなぁ","た\nて\nよ\nみ\nな\nの\nか\n?","アメリカ、行ってみてえよお","ダイエットは明日からって決めたから！(ループ)",
                "ﾄﾞｩﾜｧ!ｾﾝﾅﾅﾋｬｸ!","ﾊｧ?ｲｯﾃﾙｲﾐﾜｶﾝﾅーｲ"]



@bot.event
async def on_ready():
    print("起動した")
    
    
    
 


@bot.command()
@commands.is_owner()
async def purge(ctx, target:int):
    guild = ctx.message.guild
    channel = ctx.message.channel
    deleted = await channel.purge(limit=target)
    embed = discord.Embed(title="メッセージ削除",description = f"{len(deleted)}メッセージを削除しました")
    embed.set_footer(text=f"実行者:{ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def nkodice(ctx):
    one_dice = ["ま","ち","う"]
    embed = discord.Embed(title="NKOダイズ",description = f"結果は{random.choice(one_dice)}んこでしたー！汚いね！")
    embed.set_footer(text=f"実行者:{ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def serverinfo(ctx):
   guild = ctx.message.guild
   roles = [role for role in guild.roles]
   text_channels = [text_channels for text_channels in guild.text_channels]
   embed = discord.Embed(title=f"ServerInfo - {guild.name}", timestamp=ctx.message.created_at, color=discord.Colour.purple())
   embed.set_thumbnail(url=ctx.guild.icon_url)
   embed.add_field(name="地域", value = f"{ctx.guild.region}", inline=False)
   embed.add_field(name="チャンネル数", value = f"{len(text_channels)}", inline=False)    
   embed.add_field(name="ロール数", value=f"{len(roles)}", inline=False) 
   embed.add_field(name="サーバーブースター",value = guild.premium_subscription_count, inline=False)
   embed.add_field(name="メンバー数", value=guild.member_count, inline=False)
   embed.add_field(name="サーバー設立日",value=guild.created_at, inline=False)
   embed.set_footer(text=f"実行者:{ctx.author}", icon_url=ctx.author.avatar_url)
   await ctx.send(embed=embed)


@bot.command()
async def omikuji(ctx):
   result_count = random.randint(1,100)
   print(result_count)
   if result_count <= 10:
       result = "大吉"
   elif result_count <=20:
       result = "中吉"
   elif result_count <= 40:
       result = "吉"
   elif result_count <= 80:
       result = "小吉"
   elif result_count <= 99:
       result = "凶"
   else:
       result = "バカ"
   embed = discord.Embed(title="おみくじ",description=f"{ctx.author}さん!あなたは{result}でしたー!")
   await ctx.send(embed=embed)
#無限メンション    

@bot.command()
async def mention(ctx):
    for i in range(100):
        mes = ctx.author.mention
        count = f"これ{i+1}回目"
        await ctx.send(str(mes)+count)
     


@bot.event 
async def on_message(message):
    #ping   
    if message.content == "mmm!ping":
        raw_ping = bot.latency
        ping = round(raw_ping * 1000)
        await message.channel.send(f"Pong!\nBotのping値は{ping}msです！")
    #過疎対策
    if message.content == "mmm!kaso":
        await message.channel.send(f"過疎対策をはじめるおー！")
        while True:
            C_M = random.randint(1,10)
            if C_M == 1:
                await message.channel.send(f"{random.choice(random_comment)}\n{random.choice(random_comment)}")
            else:
                await message.channel.send(random.choice(random_comment))
            print("メッセージ送信")
            time.sleep(1)
    
    if message.content == "mmm!pong":
        await message.channel.send("pingだろｗ情弱ｗｗ")
    await bot.process_commands(message)

bot.run(token,bot=True)