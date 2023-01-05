from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument
import discord
from discord.ext import commands
from model import *
import os
from webserver import keep_alive

intents = discord.Intents().all()
Bot = commands.Bot(command_prefix=".", intents=intents)
@Bot.event
async def on_ready():
    print('Giriş yaptım!')
    await Bot.change_presence(activity=discord.Game(name=".yardim"))





@Bot.command()
@commands.guild_only()
async def kod_ayarla(ctx,ark_kod):
    discord_id = ctx.message.author.id
    user = get_user_or_false(discord_id)
    if user:
        await ctx.send(embed=discord.Embed(description="Zaten arkadaşlık kodunuzu ayarladınız.",color=0xe74c3c))
    else:
        code = Code(discord_id, ark_kod).save()
        await ctx.send(embed=discord.Embed(description=f"{ctx.message.author.mention}, arkadaşlık kodunuz {ark_kod} olarak ayarlandı.",color=0xe74c3c))

    db.commit()


@Bot.command()
@commands.guild_only()
async def kod_degis(ctx,ark_kod):
    objects = Code.manager(db)
    code_list = list(objects.all())
    author_id = ctx.message.author.id
    for usercode in objects.all():
        usercode_id = usercode.id
        idcode = objects.get(usercode_id)
        if author_id == idcode.discord_id:
            idcode.ark_kod = ark_kod
            idcode.update()
            await ctx.send(embed=discord.Embed(description=f"{ctx.message.author.mention}, arkadaşlık kodunuz {ark_kod} olarak değiştirildi.",color=0xe74c3c))
    db.commit()

@Bot.command()
@commands.guild_only()
@has_permissions(administrator=True)
async def admin_kod_degis(ctx,user : discord.User, ark_kod):
    objects = Code.manager(db)
    code_list = list(objects.all())
    for usercode in objects.all():
        usercode_id = usercode.id
        idcode = objects.get(usercode_id)
        discordid = user.id
        if int(discordid) == idcode.discord_id:
            idcode.ark_kod = ark_kod
            idcode.update()
            await ctx.send(embed=discord.Embed(description=f"{user} kullanıcısının arkadaşlık kodu, {ctx.message.author.mention} tarafından {ark_kod} olarak değiştirildi.",color=0xe74c3c))
    db.commit()

@Bot.command()
@commands.guild_only()
async def kod_sil(ctx):
    objects = Code.manager(db)
    code_list = list(objects.all())
    author_id = ctx.message.author.id
    for usercode in objects.all():
        usercode_id = usercode.id
        idcode = objects.get(usercode_id)
        if author_id == idcode.discord_id:
            idcode.delete()
            await ctx.send(embed=discord.Embed(description=f"{ctx.message.author.mention}, arkadaşlık kodunuz başarıyla silindi.",color=0xe74c3c))
    
    db.commit()

@Bot.command()
@commands.guild_only()
@has_permissions(administrator=True)
async def admin_kod_sil(ctx,user : discord.User):
    objects = Code.manager(db)
    code_list = list(objects.all())
    for usercode in objects.all():
        usercode_id = usercode.id
        idcode = objects.get(usercode_id)
        discordid = user.id
        if int(discordid) == idcode.discord_id:
            idcode.delete()
            await ctx.send(embed=discord.Embed(description=f"{user} kullanıcısının arkadaşlık kodu {ctx.message.author.mention} tarafından silindi.",color=0xe74c3c))
    
    db.commit()


@Bot.command()
@commands.guild_only()
async def kod(ctx,user : discord.User):
    objects = Code.manager(db)
    code_list = list(objects.all())
    discordid = user.id
    for usercode in objects.all():
        usercode_id = usercode.id
        idcode = objects.get(usercode_id)
        if int(discordid) == idcode.discord_id:
            ark_kod = idcode.ark_kod
            await ctx.send(embed=discord.Embed(description=f"{user} kullanıcısının arkadaşlık kodu: {ark_kod}", color=0xe74c3c))
            return
    await ctx.send(embed=discord.Embed(title="Hata:",description="Kullanıcı henüz arkadaşlık kodunu belirtmedi.",color=0xe74c3c))

@Bot.command()
async def yardim(ctx):
    embed_yardim = discord.Embed(title="Oritris Yardım Menüsüne Hoşgeldin!",description="━━━━━━━━━━━━━━━━━━━━━━",color=0xe74c3c)
    embed_yardim.set_thumbnail(url=Bot.user.avatar_url)
    embed_yardim.set_author(name=Bot.user.display_name,icon_url=Bot.user.avatar_url)
    embed_yardim.add_field(name="• | `.kod_ayarla (kod)` : Avakin arkadaşlık kodunuzu ayarlar.",value="━━━━━━━━━━━━━━━━━━━━━━", inline=False)
    embed_yardim.add_field(name="• | `.kod @kullanıcı` : Etiketlediğiniz kullanıcının kodunu gösterir.",value="━━━━━━━━━━━━━━━━━━━━━━", inline=False)
    embed_yardim.add_field(name="• | `.kod_degis (yeni kod)` : Avakin arkadaşlık kodunuzu değiştirir.",value="━━━━━━━━━━━━━━━━━━━━━━", inline=False)
    embed_yardim.add_field(name="• | `.kod_sil` : Avakin arkadaşlık kodunuzu siler.",value="━━━━━━━━━━━━━━━━━━━━━━", inline=False)
    embed_yardim.add_field(name="Admin komutları:",value="Sadece admin yetkisi olan üyeler kullana bilir.",inline=False)
    embed_yardim.add_field(name="• | `.admin_kod_degis @kullanıcı (kod)` : Etiketlediğiniz kullanıcının kodunu değiştirir.",value="━━━━━━━━━━━━━━━━━━━━━━", inline=False)
    embed_yardim.add_field(name="• | `.admin_kod_sil @kullanıcı` : Etiketlediğiniz kullanıcının kodunu siler.",value="━━━━━━━━━━━━━━━━━━━━━━", inline=False)
    await ctx.send(embed=embed_yardim)
@Bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(title="Hata:",description="Lütfen kullanmış olduğunuz komutun parametrelerini eksiksiz bir şekilde doldurun.",color=0xe74c3c))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Hata:",description="Bu komutu kullanmak için yetkiniz yok.",color=0xe74c3c))

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
my_secret = os.environ['DISCORD_BOT_SECRET']
Bot.run(TOKEN)