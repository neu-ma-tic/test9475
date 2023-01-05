import discord
from discord.ext import commands
import json
import random
import asyncio
from datetime import datetime, timedelta

import time
import sched

slowdown = ['Woal now, slow down','Take a chill pill','Dude stop rushing','Hold your horses...','Heeeyoo lets slow it down','Woal nelly, slow it down','Spam isnt cool fam']
r_slowdown = random.choice(slowdown)

async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 500
        users[str(user.id)]["bank"] = 0
    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in main_shop:
        da_name = item['name'].lower()
        name = item["name"].lower().split(str("> "), 1)[1]
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == da_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return
    except:
      return [False,3]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in main_shop:
        da_name = item['name'].lower()
        name = item["name"].lower().split(str("> "), 1)[1]
        if name == item_name:
            name_ = name
            price = item["price"]
            description = item["description"]
            type = item["type"]
            break
    if name_ == None:
        return [False, 1]
    cost = price * amount
    users = await get_bank_data()
    bal = await update_bank(user)
    if bal[0] < cost:
        return [False, 2]
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == da_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {
                "item": da_name,
                "amount": amount,
                "type": type,
                "description": description
            }
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {
            "item": da_name,
            "amount": amount,
            "type": type,
            "description": description
        }
        users[str(user.id)]["bag"] = [obj]
    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    await update_bank(user, cost * -1, "wallet")
    return [True, "Worked"]


main_shop = [{
    "name": "<:fishingrod:883533465608405043> Fishing Rod",
    "price": 1000,
    "description": "It's a fishing rod.. what do you expect?",
    "dt_description":"A fishing rod is a long, flexible rod used by fishermen to catch fish. At its simplest, a fishing rod is a simple stick or pole attached to a line ending in a hook (formerly known as an angle, hence the term angling).",
    "type": "tool"
}, {
    "name": "<:sniper:883505620458807356> Sniper",
    "price": 5000,
    "description": "You can shoot stuff with it.. (including people)",
    "dt_description": "A sniper is a military/paramilitary marksman who engages targets from positions of concealment or at distances exceeding the target's detection capabilities.[1] Snipers generally have specialized training and are equipped with high-precision rifles and high-magnification optics, and often also serve as scouts/observers feeding tactical information back to their units or command headquarters.",
    "type": "weapon"
}, {
    "name": "<:pickaxe:884354233367949312> Pickaxe",
    "price": 6000,
    "description": "Mine stuff exchange for moneyyy",
    "dt_description":"a tool for breaking hard surfaces, with a long wooden handle and a curved metal bar with a sharp point and u can mine it to exchange money",
    "type": "tool"
}]

var = []
just_a_list = []
original = []
percentlist = []

random_list = []
random_intone = 0




class Money(commands.Cog):
    def __init__(self, client):
        self.client = client

    cooldown_normal = 40

    lightning_sale = ""

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            for item in main_shop:
                name1 = item["name"]
                just_a_list.append(name1)
            percent = random.randint(1, 70)
            percentlist.append(percent)
            bools = False
            x = random.choice(just_a_list)

            var.append(x)

            while True:
                random_int = random.randint(0, 2)
                random_list.append(random_int)
                if main_shop[random_int]["name"] == x:
                    bools = True
                    print("good")
                    print(random_list[-1])
                    break
                else:
                    print('m')
            print('something')
            if bools == True:
                main_shop[random_list[-1]]["price"] = int(
                    '{:.0f}'.format(main_shop[random_list[-1]]["price"] -
                                    (main_shop[random_list[-1]]["price"] *
                                     (percent / 100))))
                print('main_shop lmao')
            else:
                print("fudge")
            global lmao
            the_time = random.randint(500,10000)
            lmao = int('{:.0f}'.format(the_time / 60))
            
            for i in range(lmao):

                await asyncio.sleep(60)

                lmao -= 1

    @commands.command()
    async def shop(self, ctx):
        lightning_sale = var[-1]
        em = discord.Embed(
            title=f"__LIGHTNING SALES__(resets in {lmao}m)",
            description=
            f'**{lightning_sale} - [{main_shop[random_list[-1]]["price"]}](https://www.youtube.com/watch?v=3QikDbiStlE&t)<:owncoin:899484325660196925>[({percentlist[-1]}% off)](https://www.youtube.com/watch?v=3QikDbiStlE&t)**\n*{main_shop[random_list[-1]]["dt_description"]}*',
            color=discord.Color.random())
        em.set_author(name="Shop Items")

        for i in main_shop:
            name = i["name"]
            price = i["price"]
            description = i["description"]
            em.add_field(name=f"{name} - {price}<:owncoin:899484325660196925>",
                         value=f"{description}",
                         inline=False)
        em.set_footer(
            icon_url=
            'https://cdn.discordapp.com/attachments/849560726833987614/883566968496594974/494229933078478858.gif',
            text="just a cool shop lol")
        await ctx.send(embed=em)

    @commands.command()
    async def buy(self, ctx, *, item):
        await open_account(ctx.author)
        amount = 1
        res = await buy_this(ctx.author, item, amount)

        if not res[0]:
            if res[1] == 1:
                await ctx.send("bruh.. that Object doesn't even exist in the shop!")
                return
            if res[1] == 2:
                await ctx.send(
                    f"You don't have enough money in your wallet to buy {amount} {item}"
                )
                return
        await ctx.send(f"You just bought {amount} **{item}**")

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []

        author_avatar = ctx.author.display_avatar
        em = discord.Embed(title="Your Owned Items",
                           description='this is your inventory',
                           color=discord.Color.from_rgb(149, 247, 45))
        em.set_author(name=f"{ctx.author.name}'s inventory",
                      icon_url=author_avatar)
        index = 0

        for item in bag:
            name = item["item"]
            amount = item["amount"]
            type = item["type"]
            description = item["description"]

            if index % 2 == 0 and index != 0:
                em.add_field(name=f"{name} - {amount}",
                             value=f'{description} - {type}',
                             inline=False)
            else:
                em.add_field(name=f"{name} - {amount}",
                             value=f'{description} - {type}',
                             inline=True)

            index += 1

        await ctx.send(embed=em)
    
    


    @commands.command()
    async def work(self,ctx,index = None):
      if index == None:
        print('test for now')
      

    @commands.command()
    async def sell(self,ctx,*,item):
      amount = 1
      await open_account(ctx.author)
      
      for i in main_shop:
        price=float('{:.0f}'.format(random.uniform(0.1,0.9) * i["price"]))
        res = await sell_this(ctx.author,item,amount,price)
      

      if not res[0]:
          if res[1]==1:
              await ctx.send("That Object isn't there!")
              return
          if res[1]==2:
              await ctx.send(f"You don't have {amount} {item} in your bag.")
              return
          if res[1]==3:
              await ctx.send(f"You don't have {item} in your bag.")
              return

      await ctx.send(f"You just sold {amount} **{item}** for {price}<:owncoin:899484325660196925>")
      

    @commands.command(aliases = ["rich"])
    async def richest(self,ctx,x = 5):
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total,reverse=True)    

        em = discord.Embed(title = f"🤑Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
        index = 1
        for amt in total:
          id_ = leader_board[amt]
          member = self.client.get_user(id_)
          if member is None:
              continue
          if member not in ctx.guild.members:
            continue

          name = member.name
          em.add_field(name = f"{index}. {name}" , value = "{:.0f}<:owncoin:899484325660196925>".format(amt),  inline = False)
          if index == x:
                break
          else:
                index += 1
        
        em.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.display_avatar)
        await ctx.send(embed = em)

    @commands.command()
    async def shoot(self,ctx,member:discord.Member = None):
      if member == None:
        await ctx.send("Dude.. who do you want to shoot")

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        await open_account(ctx.author)
        owner_id = 696617859580690512
        if ctx.author.id is owner_id:
            print("bruh")
        users = await get_bank_data()
        wallet_amt = int(users[str(ctx.author.id)]["wallet"])
        bank_amt = int(users[str(ctx.author.id)]["bank"])

        em = discord.Embed(title=f"{ctx.author.name}'s balance",
                           color=discord.Color.red())
        em.add_field(name="Wallet balance", value=f"{wallet_amt}<:owncoin:899484325660196925>",inline=False)
        em.add_field(name="Bank balance", value=f"{bank_amt}<:owncoin:899484325660196925>",inline=False)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self,ctx):
      user = await get_bank_data()
      await open_account(ctx.author)
      user[str(ctx.author.id)]["wallet"]+=25000
      embed=discord.Embed(title="Your daily moni :money_mouth: ",description="you just got 25000 more coins :D\n[patrons](https://www.patreon.com/botprogram) get 100000 daily coins")
      await ctx.send(embed=embed)
      with open("mainbank.json", "w") as f:
                json.dump(user, f)

    @commands.command()
    @commands.cooldown(1, 604800, commands.BucketType.user)
    async def weekly(self,ctx):
      user = await get_bank_data()
      await open_account(ctx.author)
      user[str(ctx.author.id)]["wallet"]+=2500

    @commands.command()
    @commands.cooldown(1, cooldown_normal, commands.BucketType.user)
    async def beg(self, ctx):
        owner_id = 696617859580690512
        await open_account(ctx.author)
        if ctx.author.id == owner_id:
            earnings = random.choice(range(100000, 100000000))
            await ctx.send(
                f"OH MY CREATOR! hello, i'll give you {earnings}<:owncoin:899484325660196925> just beacuse you are my developer"
            )
            users = await get_bank_data()

            users[str(ctx.author.id)]["wallet"] += earnings
            with open("mainbank.json", "w") as f:
                json.dump(users, f)
        else:
            users = await get_bank_data()

            earnings = random.randint(0, 4001)
            earning_responses = [
                "Someone just gave you ", "Oh you little poor beggar here's ",
                "Fine.. I'll give you "
            ]
            random_earning_response = random.choice(earning_responses)

            not_earning_response = [
                "bruh imagine begging:rolling_eyes: ",
                "Sure, here are some invisible money", "Stop begging omg",
                "Get lost you beggar"
            ]
            random_ner = random.choice(not_earning_response)

            all_of_them_inalist = [random_earning_response, random_ner]

            actual_random_beg = random.choice(all_of_them_inalist)

            if actual_random_beg in earning_responses:  # wait
                await ctx.send(
                    f"{actual_random_beg}{earnings}<:owncoin:899484325660196925> "
                )
                users[str(ctx.author.id)]["wallet"] += earnings
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)
            else:
                await ctx.send(actual_random_beg)
    @beg.error
    async def beg_error(self,ctx,error):
      if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title=r_slowdown,description="Stop begging so much bruh<:bruh:887896562972389446>\nYou can run this command in **{:.2f} second**\nThe default cooldown is `3s` but [subscribers](https://www.youtube.com/channel/UC6kZd-2yKyXXE0UR5sDvy0A?sub_confirmation=1) only need to wait `1s`!".format(
                error.retry_after))
        await ctx.send(embed=embed)

    @commands.command(aliases=['with', 'wd'])
    async def withdraw(self, ctx, amount=None):
        await open_account(ctx.author)
        users = await get_bank_data()
        await open_account(ctx.author)
        if amount == 'all':
          await update_bank(ctx.author, users[str(ctx.author.id)]["bank"], "wallet")
          await update_bank(ctx.author,-1 *users[str(ctx.author.id)]["bank"],"bank")
          
          await ctx.send("You withdrew all of your coins<:owncoin:899484325660196925>")
        if amount == None:
            await ctx.send('Please enter the amount')
            return

        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("You don't have that much money!")
            return
        if amount < 0:
            await ctx.send("Amount must be positive!")
            return

        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1 * amount, "bank")
        await ctx.send(f"You withdrew {amount}<:owncoin:899484325660196925>")

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, amount=None):
        users = await get_bank_data()
        await open_account(ctx.author)
        if amount == 'all':
          await update_bank(ctx.author,-1*users[str(ctx.author.id)]["wallet"])
          await update_bank(ctx.author, users[str(ctx.author.id)]["wallet"], "bank")
          await ctx.send("You deposited all of your coins<:owncoin:899484325660196925>")
        if amount == None:
            await ctx.send('Please enter the amount')
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("You don't have that much money!")
            return
        if amount < 0:
            await ctx.send("Amount must be positive!")
            return

        await update_bank(ctx.author, -1 * amount)
        await update_bank(ctx.author, amount, "bank")
        await ctx.send(f"You deposited {amount}<:owncoin:899484325660196925>")

    @commands.command()
    async def send(self, ctx, member: discord.Member, amount=None):
        await open_account(ctx.author)
        await open_account(member)
        if amount == None:
            await ctx.send('Please enter the amount')
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("You don't have that much money!")
            return
        if amount < 0:
            await ctx.send("Amount must be positive!")
            return
        await update_bank(member, amount, "wallet")
        await update_bank(ctx.author, -1 * amount, "wallet")
        await ctx.send(
            f"You gave {member} {amount}<:owncoin:899484325660196925>")


def setup(client):
    client.add_cog(Money(client))
