#import needed for the bot to function 
import discord
import os
import requests
from discord.ext import commands
from riotwatcher import LolWatcher, ApiError
#import pandas as pd
#import matplotlib.pyplot as plt

apiKey = os.getenv('RIOT_API_KEY')

#riotwatcher api wrapper
#Important Note The region is hardcoded to be defined as NA
watcher = LolWatcher(os.getenv('RIOT_API_KEY'))
my_region = 'na1'

#prefix used to signal that the text is for the bot to handle
bot = commands.Bot(command_prefix="!")

#function to calculate KDA Ratio
def kda(kill,death, assists):
  return str((kill+assists) / death)

#function to calculate win rate
def winRate(wins, losses):
  sum = wins+losses
  result = wins / sum
  return str(result)





@bot.event
async def on_ready():
    print(f'{bot.user.name } has connected to Discord!')


@bot.command()
async def noWrapper(name):
    apiCall = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+str(name)+"?api_key=RGAPI-65b14ab9-348d-4032-b4c7-894651dd307b" 
    response = requests.get(apiCall)
    print(response)

#looks up a op.gg link for the Summoner Selected
@bot.command()
async def opGG(ctx, arg1):
    summonerLookUp = "https://na.op.gg/summoner/userName=" + arg1
    requests.get(summonerLookUp)
    if summonerLookUp:
        await ctx.send(summonerLookUp)
    else:
        await ctx.send("failed to find link!")

#gets the entered summoners ranked stats for ranked Solo Queue and Ranked Flex modes
@bot.command()
async def rankedStats(ctx, arg1):
    player = watcher.summoner.by_name(my_region, arg1)
    ranked_stats = watcher.league.by_summoner(my_region, player['id'])
    stats = []
    for row in ranked_stats:
      if row['queueType'] == 'RANKED_SOLO_5x5':
        stats_row = {}
        stats_row['QueueType'] = "Ranked Solo"
        stats_row['Tier'] = row ['tier']
        #print(row['tier'])
        stats_row['Rank'] = row['rank']
        stats_row['LeaguePoints'] =  row['leaguePoints']
        wins = stats_row['Wins'] = row['wins']
        losses = stats_row['Losses'] = row['losses']
        stats_row['winRate'] = winRate(wins,losses)
        stats.append(stats_row)
      elif row['queueType'] == 'RANKED_FLEX_SR':
        stats_row = {}
        stats_row['QueueType'] = "Ranked Flex"
        stats_row['Tier'] = row ['tier']
       # print(row['tier'])
        stats_row['Rank'] = row['rank']
        stats_row['LeaguePoints'] =  row['leaguePoints']
        wins =stats_row['Wins'] = row['wins']
        losses = stats_row['Losses'] = row['losses']
        stats_row['winRate'] = winRate(wins,losses)
        #print(row['rank'])
        stats.append(stats_row)
        #stats_row['SoloQueueRank'] = row[0][2]
    rankStatString = " "
    for d in stats:
      rankStatString += "---------------------------------------------------------\n"
      for k, v in d.items():
        rankStatString += (str(k) + " : " + str(v) + "\n")
    await ctx.send("```css\n"+rankStatString+"```")

    #print(stats)
    #rankStatString = stats['SoloQueueRank']
    #print(ranked_stats)
  #print(rankStatString)

#Gets basic stats about the entered summoners last game.
@bot.command()
async def lastMatch(ctx, arg1):
  me = watcher.summoner.by_name(my_region, arg1)
  my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
    #print(my_matches)

    # fetch last match detail
  last_match = my_matches['matches'][0]
  print(last_match)
    #print(my_matches)
    #print(len(my_matches))
  match_detail = watcher.match.by_id(my_region, last_match['gameId'])
  participant = []
  #print(last_match)
  #print(type(last_match))
  champPlayed = last_match['champion']
   # print(champPlayed)
  for row in match_detail['participants']:
       # participants_row = {}
        #participants_row = {}
        
        if row['championId'] == champPlayed:
          print(row)
          participants_row = {}
          participants_row['champion'] = row['championId']
       
          participants_row['spell1'] = row['spell1Id']
      
          participants_row['spell2'] = row['spell2Id']
          
          participants_row['win'] = row['stats']['win']
          if participants_row['win'] == False:
            participants_row['win'] = "You Lost!"
          else:
            participants_row['win'] = "You Won!"
        
          gameKills = participants_row['kills'] = row['stats']['kills']
       
          gameDeaths = participants_row['deaths'] = row['stats']['deaths']
       
          gameAssists = participants_row['assists'] = row['stats']['assists']
       
          participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        
          participants_row['totalDamageDealtToChampions'] = row['stats']['totalDamageDealtToChampions']

          participants_row['timeCCingOthers'] = row['stats']['timeCCingOthers']
          participants_row['goldEarned'] = row['stats']['goldEarned']
      
          participants_row['champLevel'] = row['stats']['champLevel']
       
          participants_row['totalMinionsKilled'] = row['stats'][
            'totalMinionsKilled']
          participants_row['totalTimeCrowdControlDealt'] = row['stats']['totalTimeCrowdControlDealt']

        
          csStatsPerMinute = row['timeline']['creepsPerMinDeltas']

        

          participants_row['item0'] = row['stats']['item0']
          participants_row['item1'] = row['stats']['item1']
          participant.append(participants_row)

  gameStatString = (participant[0]['win'] + "\n" +
                str(participant[0]['kills']) + " Kills \n"
                + str(participant[0]['deaths']) + " Deaths \n" 
                + str(participant[0]['assists']) + " Assists \n"
                "KDA: " + kda(gameKills,gameDeaths,gameAssists) +"\n" +
                "Total Damage Dealt to Champions " + str(participant[0]['totalDamageDealtToChampions']) +"! \n")
              
                

  await ctx.send("```css\n"+   gameStatString + "```")
  await ctx.send("-- CS per Minute -- ") 
  await ctx.send(csStatsPerMinute)
  #await ctx.send("-- CS per Minute difference vs Opponent -- \n ")  
  # await ctx.send(csStatsPerMinuteVerusOpponent)

bot.run(os.getenv('Discord_Api_Key'))
