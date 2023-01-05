import discord, json, random, os, asyncio
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

class drawcard(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, message):

        if (message.content == '佑樹10連抽' or message.content == '佑樹十連抽'):
            arr = ['3star', '2star', '1star']
            rate = [25, 180, 795]
            rate2 = [25, 975]

            pcr_3star='<:pcr_r:827880901026381826>'
            pcr_2star='<:pcr_g:827880901337546752>'
            pcr_1star='<:pcr_s:827880901332828190>'
            pcr_stone='<:pcr_stone:827916404577665084>'
            space = '\n'
            card = [None]*11
            for i in range(5):
                prob_card=arr[random_index(rate)]
                
                if prob_card == '3star':
                    card[i]=pcr_3star
                elif prob_card == '2star':
                    card[i]=pcr_2star
                elif prob_card == '1star':
                    card[i]=pcr_1star
                else:
                    card[i]=pcr_1star
            card[5] = space

            for i in range(6,10):
                prob_card=arr[random_index(rate)]
                
                if prob_card == '3star':
                    card[i]=pcr_3star
                elif prob_card == '2star':
                    card[i]=pcr_2star
                elif prob_card == '1star':
                    card[i]=pcr_1star
                else:
                    card[i]=pcr_1star

            prob_card = arr[random_index(rate2)]
            if prob_card == '3star':
                card[10]=pcr_3star
            elif prob_card == '2star':
                card[10]=pcr_2star
            else:
                card[10]=pcr_2star

            stone = card.count(pcr_1star) * 1 + card.count(pcr_2star)*10 + card.count(pcr_3star)*50

            lol="".join('%s' %id for id in card)
            await message.channel.send(str(message.author.name)+f'抽到了'+ str(stone) + str(pcr_stone))
            await message.channel.send(str(lol))
            msg=''
            if card.count(pcr_1star)==9 and card.count(pcr_2star)==1:#保底嘲諷
                msg='<:gura:822436625623547937>'
                await message.channel.send(str(msg))

        elif (message.content == '狼師10連抽' or message.content == '狼師十連抽'):
            arr = ['3star', '2star', '1star']
            rate = [25, 180, 795]
            rate2 = [25, 975]

            ba_3star='<:ba_r:827845640562016286>'
            ba_2star='<:ba_g:827845640498315315>'
            ba_1star='<:ba_s:827845640595308575>'
            ba_stone='<:ba_stone:827845640330936331>'
            space = '\n'
            card = [None]*11
            for i in range(5):
                prob_card=arr[random_index(rate)]
                
                if prob_card == '3star':
                    card[i]=ba_3star
                elif prob_card == '2star':
                    card[i]=ba_2star
                elif prob_card == '1star':
                    card[i]=ba_1star
                else:
                    card[i]=ba_1star
            card[5] = space

            for i in range(6,10):
                prob_card=arr[random_index(rate)]
                
                if prob_card == '3star':
                    card[i]=ba_3star
                elif prob_card == '2star':
                    card[i]=ba_2star
                elif prob_card == '1star':
                    card[i]=ba_1star
                else:
                    card[i]=ba_1star

            prob_card = arr[random_index(rate2)]
            if prob_card == '3star':
                card[10]=ba_3star
            elif prob_card == '2star':
                card[10]=ba_2star
            else:
                card[10]=ba_2star

            stone = card.count(ba_1star) * 1 + card.count(ba_2star)*10 + card.count(ba_3star)*50

            lol="".join('%s' %id for id in card)
            await message.channel.send(str(message.author.name)+f'抽到了'+ str(stone) + str(ba_stone))
            await message.channel.send(str(lol))
            msg=''
            if card.count(ba_1star)==9 and card.count(ba_2star)==1:#保底嘲諷
                msg='<:gura:822436625623547937>'
                await message.channel.send(str(msg))
        elif (message.content == '狼師抽pu' or message.content == '狼師抽PU'):
            arr = ['pickup', '3star', '2star', '1star']
            rate = [7, 18, 180, 795]
            rate2 = [7, 18, 975]
            stone = 0
            total_3stat = 0
            total_2stat = 0
            total_1stat = 0
            total_pickup = 0
            ba_pickup='4'
            ba_3star='<:ba_r:827845640562016286>'
            ba_2star='<:ba_g:827845640498315315>'
            ba_1star='<:ba_s:827845640595308575>'
            ba_stone='<:ba_stone:827845640330936331>'

            card = [None]*10

            for i in range (20):
                for i in range(5):
                    prob_card=arr[random_index(rate)]
                    
                    if prob_card == '3star':
                        card[i]=ba_3star
                    elif prob_card == '2star':
                        card[i]=ba_2star
                    elif prob_card == '1star':
                        card[i]=ba_1star
                    elif prob_card == 'pickup':
                        card[i]=ba_pickup
                    else:
                        card[i]=ba_1star

                for i in range(5,9):
                    prob_card=arr[random_index(rate)]
                    
                    if prob_card == '3star':
                        card[i]=ba_3star
                    elif prob_card == '2star':
                        card[i]=ba_2star
                    elif prob_card == '1star':
                        card[i]=ba_1star
                    elif prob_card == 'pickup':
                        card[i]=ba_pickup
                    else:
                        card[i]=ba_1star

                prob_card = arr[random_index(rate2)]
                if prob_card == '3star':
                    card[9]=ba_3star
                elif prob_card == '2star':
                    card[9]=ba_2star
                elif prob_card == 'pickup':
                    card[i]=ba_pickup
                else:
                    card[9]=ba_2star

                stone += card.count(ba_1star) * 1 + card.count(ba_2star)*10 + card.count(ba_3star)*50 + card.count(ba_pickup)*50
                total_3stat += card.count(ba_3star) + card.count(ba_pickup)
                total_2stat += card.count(ba_2star)
                total_1stat += card.count(ba_1star)
                total_pickup += card.count(ba_pickup)

                if card.count(ba_pickup) != 0:
                    break

            total = total_3stat + total_2stat + total_1stat

            await message.channel.send(str(message.author.name) + f'一共抽了' + str(total) + f'抽，'+ f'抽到了'+ str(stone) + str(ba_stone) + str('\n') +\
                                    str(ba_3star) + str(total_3stat) + f'張，其中' + str(total_pickup) + f'張PU' + str('\n') +\
                                    str(ba_2star) + str(total_2stat) + f'張' + str('\n') +\
                                    str(ba_1star)+str(total_1stat)+f'張')
            msg=''
            if total_pickup==0:#保底嘲諷
                msg='<:gura:822436625623547937>'
                await message.channel.send(str(msg))
        elif (message.content == '佑樹抽pu' or message.content == '佑樹抽PU'):
            arr = ['pickup', '3star', '2star', '1star']
            rate = [7, 18, 180, 795]
            rate2 = [7, 18, 975]
            stone = 0
            total_3stat = 0
            total_2stat = 0
            total_1stat = 0
            total_pickup = 0
            pcr_pickup='4'
            pcr_3star='<:pcr_r:827880901026381826>'
            pcr_2star='<:pcr_g:827880901337546752>'
            pcr_1star='<:pcr_s:827880901332828190>'
            pcr_stone='<:pcr_stone:827916404577665084>'

            card = [None]*10

            for i in range (20):
                for i in range(5):
                    prob_card=arr[random_index(rate)]
                    
                    if prob_card == '3star':
                        card[i]=pcr_3star
                    elif prob_card == '2star':
                        card[i]=pcr_2star
                    elif prob_card == '1star':
                        card[i]=pcr_1star
                    elif prob_card == 'pickup':
                        card[i]=pcr_pickup
                    else:
                        card[i]=pcr_1star

                for i in range(5,9):
                    prob_card=arr[random_index(rate)]
                    
                    if prob_card == '3star':
                        card[i]=pcr_3star
                    elif prob_card == '2star':
                        card[i]=pcr_2star
                    elif prob_card == '1star':
                        card[i]=pcr_1star
                    elif prob_card == 'pickup':
                        card[i]=pcr_pickup
                    else:
                        card[i]=pcr_1star

                prob_card = arr[random_index(rate2)]
                if prob_card == '3star':
                    card[9]=pcr_3star
                elif prob_card == '2star':
                    card[9]=pcr_2star
                elif prob_card == 'pickup':
                    card[i]=pcr_pickup
                else:
                    card[9]=pcr_2star

                stone += card.count(pcr_1star) * 1 + card.count(pcr_2star)*10 + card.count(pcr_3star)*50 + card.count(pcr_pickup)*50
                total_3stat += card.count(pcr_3star) + card.count(pcr_pickup)
                total_2stat += card.count(pcr_2star)
                total_1stat += card.count(pcr_1star)
                total_pickup += card.count(pcr_pickup)

                if card.count(pcr_pickup) != 0:
                    break

            total = total_3stat + total_2stat + total_1stat

            await message.channel.send(str(message.author.name) + f'一共抽了' + str(total) + f'抽，'+ f'抽到了'+ str(stone) + str(pcr_stone) + str('\n') +\
                                    str(pcr_3star) + str(total_3stat) + f'張，其中' + str(total_pickup) + f'張PU' + str('\n') +\
                                    str(pcr_2star) + str(total_2stat) + f'張' + str('\n') +\
                                    str(pcr_1star)+str(total_1stat)+f'張')
            msg=''
            if total_pickup==0:#保底嘲諷
                msg='<:gura:822436625623547937>'
                await message.channel.send(str(msg))

        elif ('<:Stanley_cry:833662627045310464>' in message.content or '哭阿' in message.content or '哭啊' in message.content):

            if (message.author.name == 'Juice'):
              pass

            else:
              member = message.author

              role = discord.utils.get(message.guild.roles, name="mute")
              role2 = discord.utils.get(message.guild.roles, name="1")
              role3 = discord.utils.get(message.guild.roles, name="888朋友")
              role3_count = 0

              await member.add_roles(role)
              await member.remove_roles(role2)
              if (role3 in member.roles):
                await member.remove_roles(role3)
                role3_count += 1
              else:
                mute_time = random.randint(1, 600)
              await message.channel.send(f'你已被管理員relaxing234禁言'+ str(mute_time) + f'秒')

              await asyncio.sleep(mute_time)

              await member.remove_roles(role)
              await member.add_roles(role2)
              if (role3_count != 0):
                await member.add_roles(role3)
                role3_count == 0

        elif (message.content == '今早跟誰睡' or message.content == '今午跟誰睡' or message.content == '今晚跟誰睡' or message.content == '凌晨跟誰睡' or message.content.endswith ('跟誰睡')):
            random_sleep = random.choice(jdata['sleep'])
            await message.channel.send(f'{random_sleep}')

        elif ('好油喔' in message.content):
            await message.add_reaction('<:peko_hehe:811625013341847582>')
            await message.add_reaction('<:peko_p:831891624615346187>')
            await message.add_reaction('<:peko_e:831891624833187890>')
            await message.add_reaction('<:peko_k:831891624903835678>')
            await message.add_reaction('<:peko_o:831891624962949211>')


def setup(bot):
    bot.add_cog(drawcard(bot))