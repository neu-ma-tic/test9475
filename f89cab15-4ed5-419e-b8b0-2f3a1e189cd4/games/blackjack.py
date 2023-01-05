import random

import discord
from core import CogInit, readFile
from discord.ext import commands

is_started = False
in_game = False
initiator = ""  # 莊家
participants = {}
channel = ""  # 遊玩的頻道
turn = 0
cards = []
players = []
point = readFile("cards")["point"]
player_num = 0
Round = 1
t_round = 0
message = 0


def draw(player):  # 抽牌
    global cards
    global point
    global participants
    random.shuffle(cards)
    card = cards.pop()  # 考慮以random產生index
    participants[player].append(card)
    return card


def point_check(player):
    global participants
    global point
    total_p = 0
    p = []
    ace_count = 0
    for card in participants[player]:
        if card[1] == "A":
            ace_count += 1
        else:
            total_p += point[card[1]]
    if ace_count == 0:  # 無Ace
        return [total_p]
    else:
        for i in range(1, ace_count + 1):
            temp = total_p + i + 11 * (ace_count - i)
            if temp < 21 and temp not in p:
                p.append(temp)

            temp = total_p + 11 * i + (ace_count - i)
            if temp < 21 and temp not in p:
                p.append(temp)

            if (total_p + i + 11 * (ace_count - i)) == 21 or (total_p + 11 * i + (ace_count - i)) == 21:
                p = [21]
                break
            if p == []:  # 不符合前面任何條件(爆牌)
                p = [total_p + i + 11 * (ace_count - i)]
            else:
                break
        return p


class BLACKJACK(CogInit):
    async def end_game(self):
        global participants
        global channel
        global in_game
        global is_started
        global players
        global Round
        global turn

        def check(msg: discord.Message) -> bool:
            return msg.author.id == 719120395571298336

        # await channel.purge(check=check, before=end_time, after=start_time)
        await channel.purge(check=check, limit=300)
        if len(participants.keys()) == 0:
            await channel.send("所有玩家皆爆牌，此局遊戲無贏家")
        else:
            point = []
            winner = []
            msg = ""
            for player in participants.keys():
                point.append(max(point_check(player)))
            for i, player in enumerate(participants.keys()):
                if point[i] == max(point):
                    winner.append(player)
            if initiator in winner:
                msg += f"回合結束，莊家({initiator.mention})"
            else:
                msg += "回合結束，"
                for player in winner:
                    if player != winner[-1]:
                        msg += f" {player.mention} &"
                    else:
                        msg += f" {player.mention}"
            msg += "贏了，各玩家資訊：\n"
            for player, p in zip(list(participants.items()), point):
                msg += f"{player[0].mention} : `{p}` 點，手牌 :"
                for card in player[1]:
                    if card != player[1][-1]:
                        msg += f"`{card[0]}` `{card[1]}`、"
                    else:
                        msg += f"`{card[0]}` `{card[1]}`\n"
            msg += "** **"
            await channel.send(msg, delete_after=30)

        if Round > t_round:
            await channel.send("遊戲結束", delete_after=30)
            in_game = False
            is_started = False
            participants = {}
            players = []
            Round = 1
        else:
            turn = 0
            participants = {initiator: []}
            players.remove(initiator)
            for player in players:
                participants.setdefault(player, [])
            await self.game()

    async def game(self):
        global in_game
        global is_started
        global players
        global initiator
        global cards
        global participants
        global turn
        global Round
        global message

        await message.delete()
        if not in_game and is_started:
            if len(list(participants.keys())) <= 1:
                await channel.send("遊戲人數不足或發起人離開遊戲，遊戲取消", delete_after=5)
                is_started = False
                participants = {}
            else:
                await channel.send("遊戲開始，由於bot一定時間內只能發5則訊息，若訊息卡住請稍待數秒")
                in_game = True
        if is_started and in_game:
            if turn == 0:  # 回合開始
                cards = readFile("cards")["cards"]  # 初始化牌組
                random.shuffle(players)
                players.append(initiator)
                await channel.send(f"第 {Round} 回合開始，要牌順序及明牌：")
                msg = ""
                for i, player in enumerate(players):  # 發明牌
                    card1 = draw(player)
                    card2 = draw(player)
                    if player != players[-1]:
                        msg += f"{i+1}.{player.mention} : `{card1[0]}` `{card1[1]}`、`{card2[0]}` `{card2[1]}`\n"
                    else:
                        await initiator.send(f"暗牌：`{card1[0]}` `{card1[1]}`")
                        msg += f"莊家：{player.mention} : `暗牌不公開`、`{card2[0]}` `{card2[1]}`"
                await channel.send(msg)
            message = await channel.send(
                f"現在是 {players[turn].mention} 的回合，\N{SQUARED OK}加牌，爆牌/21點/\N{End with Leftwards Arrow Above}結束加牌(遊戲)，\N{BLACK QUESTION MARK ORNAMENT}查詢點數"
            )
            await message.add_reaction("\N{SQUARED OK}")
            await message.add_reaction("\N{End with Leftwards Arrow Above}")
            await message.add_reaction("\N{BLACK QUESTION MARK ORNAMENT}")

    @commands.command(aliases=["BJ"])
    async def blackjack(self, ctx, n: int = 10, r: int = 1):
        global is_started
        global in_game
        global initiator
        global channel
        global participants
        global player_num
        global turn
        global t_round
        global message

        await ctx.message.delete()
        if is_started:
            await ctx.send("已經有人開始遊戲", delete_after=3)
        else:
            if (not 1 < n <= 10) or (not 0 < r <= 5):
                await ctx.send("遊戲人數或局數不合理(1 < 人數 <= 10， 0 < 局數 <= 5)", delete_after=3)
            else:
                turn = 0
                is_started = True
                in_game = False
                initiator = ctx.author
                channel = ctx.channel
                participants.setdefault(initiator, [])
                player_num = n
                t_round = r
                msg = await ctx.send(
                    f"{ctx.author.mention}開始了21點遊戲，預計進行 **{r}** 回合\n選取\N{WHITE HEAVY CHECK MARK}參加遊戲，加入後選取\N{NEGATIVE SQUARED CROSS MARK}可退出，參加人數達到 **{n}** 或遊戲發起人選取\N{Black Right-Pointing Triangle}後開始遊戲"
                )
                message = msg
                await msg.add_reaction("\N{WHITE HEAVY CHECK MARK}")
                await msg.add_reaction("\N{NEGATIVE SQUARED CROSS MARK}")
                await msg.add_reaction("\N{Black Right-Pointing Triangle}")

                def check(reaction, user):
                    return str(reaction.emoji) == "\N{Black Right-Pointing Triangle}" and user == initiator

                try:
                    await self.bot.wait_for("reaction_add", check=check)
                except:
                    pass
                else:
                    await self.game()

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global message
        global participants
        global players
        global channel
        global initiator
        global turn
        global Round
        if is_started and user != self.bot.user and reaction.message.id == message.id:
            try:
                await reaction.remove(user)
            except:
                pass
            if not in_game:
                if str(reaction.emoji) == "\N{WHITE HEAVY CHECK MARK}":
                    if user not in participants.keys():
                        participants.setdefault(user, [])
                        players.append(user)
                        await channel.send(f"{user.mention}參加成功", delete_after=3)
                        if len(participants.keys()) == player_num:
                            await self.game()
                    else:
                        await channel.send(f"{user.mention}你已在遊戲中", delete_after=3)
                elif str(reaction.emoji) == "\N{NEGATIVE SQUARED CROSS MARK}":
                    if user == initiator:
                        participants = {}
                        await self.game()
                    elif user in participants.keys():
                        del participants[user]
                        players.remove(user)
                        await channel.send(f"{user.mention}取消參加成功", delete_after=3)
                    else:
                        await channel.send(f"{user.mention}你沒有在遊戲中", delete_after=3)
                elif str(reaction.emoji) != "\N{Black Right-Pointing Triangle}":
                    await channel.send("無效的操作", delete_after=3)

            elif in_game:
                if str(reaction.emoji) == "\N{SQUARED OK}" and user == players[turn]:  # 抽牌
                    card = draw(players[turn])
                    await channel.send(f"{user.mention} : `{card[0]}` `{card[1]}`")
                    point = point_check(user)

                    if len(point) == 1 and point[0] > 21:  # 爆牌
                        MSG = f"{user.mention} 爆牌了，手牌:"
                        for card in participants[user]:
                            if card != participants[user][-1]:
                                MSG += f"`{card[0]}` `{card[1]}`、"
                            else:
                                MSG += f"`{card[0]}` `{card[1]}`，共 `{point[0]}` 點"
                        await channel.send(MSG)
                        del participants[user]

                        if user == initiator:  # 莊家爆牌
                            Round += 1
                            await self.end_game()
                        else:  # 閒家爆牌
                            turn += 1
                            await self.game()
                    elif point == [21]:  # 21點
                        await channel.send(f"{user.mention} 21點")
                        if user == initiator:  # 莊家
                            Round += 1
                            await self.end_game()
                        else:  # 閒家
                            turn += 1
                            await self.game()
                elif str(reaction.emoji) == "\N{End with Leftwards Arrow Above}" and user == players[turn]:  # next
                    if user == initiator:  # 莊家
                        Round += 1
                        await self.end_game()
                    else:  # 閒家
                        turn += 1
                        await self.game()

                elif str(reaction.emoji) == "\N{BLACK QUESTION MARK ORNAMENT}" and user in participants.keys():  # 查點數
                    point = point_check(user)
                    msg = "你的點數可為： "
                    for p in point:
                        if p != point[-1]:
                            msg += f" `{p}` 、"
                        else:
                            msg += f" `{p}` 點"
                    await user.send(msg)
                # else:
                # await channel.send(f"{user.mention} 你不在遊戲中或現在不是你的回合", delete_after = 5)

    @commands.command()
    async def BJ_e(self, ctx):
        global in_game
        global is_started
        global participants
        global players
        global Round
        if is_started and in_game and ctx.author == initiator:
            await ctx.send("強制結束遊戲成功", delete_after=3)
            in_game = False
            is_started = False
            participants = {}
            players = []
            Round = 1
        else:
            await ctx.send("目前沒有遊戲正在進行或你不是遊戲發起人", delete_after=5)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(BLACKJACK(bot))
