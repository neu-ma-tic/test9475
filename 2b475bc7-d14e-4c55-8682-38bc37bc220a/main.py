import discord
from riotwatcher import LolWatcher, ApiError
from dotenv import load_dotenv
import datetime
from discord.ext import commands

key = "RGAPI-e1c819dd-e9ae-4e14-9056-4cef17b89cf6"

watcher = LolWatcher(key)

load_dotenv()
TOKEN = "ODczODI0NjQzODE4MDY1OTQw.YQ-CnQ.2MvuWyBDwg3q_f7RkAE-Kq39kaM"

bot = commands.Bot(command_prefix="+")


@bot.command(name="stats")
async def print_stats(ctx, summonerName):
    servidor = "la1"

    summoner = watcher.summoner.by_name(servidor, summonerName)
    stats = watcher.league.by_summoner(servidor, summoner["id"])

    try:
        for queue in stats:
            if queue["queueType"] == 'RANKED_SOLO_5x5':
                tier = queue["tier"]
                rank = queue["rank"]
                lps = queue["leaguePoints"]

                wins = queue["wins"]
                lost = queue["losses"]
                wr = wins / (wins + lost)
                wr = round(100 * wr, 2)

                message = f"{tier} {rank} con {lps} LP's y {wr}% de winrate. {wins} W || {lost} L"

                await ctx.send(message)

    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise

    '''
    except ApiError as err:
        if err.response.status_code == 429:
            await ctx.send('We should retry in {} seconds.'.format(err.headers['Retry-After']))
            await ctx.send('this retry-after is handled by default by the RiotWatcher library')
            await ctx.send('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            await ctx.send('Summoner with that ridiculous name not found.')
        else:
            raise
    '''

@bot.command()
async def info(ctx):
    servidor = "la1"

    participants = ["DancingBlades", "Diego6u9r", "Franco04", "Gsk1ngs", "wik 2020", "Zed Ekkonomista", "GSkings", "DoomBlade18", "Invio1ab1e"]
    lps_tier={"IRON":0, "BRONZE":1, "SILVER":2, "GOLD":3, "PLATINUM":4, "DIAMOND":5, "MASTER":6}
    lps_rank={"IV":0, "III":100, "II":200, "I":300}
    players_stats = []
    for summonerName in participants:
        summoner = watcher.summoner.by_name(servidor, summonerName)
        stats = watcher.league.by_summoner(servidor, summoner["id"])
        for queue in stats:
            if queue["queueType"] == 'RANKED_SOLO_5x5':
                tier = queue["tier"]
                rank = queue["rank"]
                lps = queue["leaguePoints"]

                wins = queue["wins"]
                lost = queue["losses"]
                wr = wins / (wins + lost)
                wr = round(100 * wr, 2)

                total_lps = lps_tier[tier]*400 + lps_rank[rank]+ lps
                players_stats.append({
                    "Name":summonerName,
                    "tier":tier,
                    "rank":rank,
                    "lps":lps,
                    "wins":wins,
                    "loses":lost,
                    "winrate":wr,
                    "TOTAL_LPS":total_lps})
    players_stats.sort(key=lambda player: player["TOTAL_LPS"], reverse=True)

    embed = discord.Embed(title="HierroQ Challenge", description="Estadísticas actuales :0", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())

    await ctx.send(embed=embed)

    for i in range(len(players_stats)):
        tier = players_stats[i]["tier"]
        rank = players_stats[i]["rank"]
        lps = players_stats[i]["lps"]

        wins = players_stats[i]["wins"]
        lost = players_stats[i]["loses"]
        wr = players_stats[i]["winrate"]

        name = players_stats[i]["Name"]
        '''
        embed.add_field(name=f"PUESTO {i+1}: {name}", value=f"{tier} {rank} {lps} LP's\t{wr}% de winrate.\t{wins} W || {lost} L")
        '''

        player_embed = discord.Embed(title=f"PUESTO {i+1}", description=name, color=discord.Color.green())
        player_embed.add_field(name="RANGO ACTUAL:", value=f"{tier} {rank}\t{lps} LP's")
        player_embed.add_field(name="WINRATE:", value=f"{wr}%\t{wins} W\t||\t{lost} L")
        await ctx.send(embed=player_embed)

bot.run(TOKEN)
