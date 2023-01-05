 #https://discordpy.readthedocs.io/en/latest/api.html
 #https://uptimerobot.com/dashboard#783008384
 #https://repl.it/talk/learn/How-to-use-and-setup-UptimeRobot/9003
donsonid=231259532863602698
thanos=467016289878147073
import discord
from discord.ext import commands
from discord import Game
import random
from random import randint
import asyncio
import json
import re
import datetime
import pytz
import math
import os
import keep_alive
import pip
from replit import db
import requests
import textwrap
import requests
from discord import Webhook, RequestsWebhookAdapter
from discord_buttons_plugin import *

"""
password_provided = str(os.getenv("PASS"))
password = password_provided.encode()
salt = bytes(str(os.getenv("SALT")), encoding = 'utf-8')
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
opkey = Fernet(key)

with open("tt_terms.txt", 'rb') as f:
  data = f.read()
terms = opkey.decrypt(data).decode("utf-8").split("\n")

terms_only=[]
for term in terms:
  if len(term) == 1:
    continue
  line = term.split(": ")
  terms_only.append(line[0])
terms_only.sort()"""

"""async def pong_run(channel_id,c,edit_message):
  if pong[channel_id][3]==5:
    del gamemode[channel_id]
    pong_channels.remove(channel_id)
    del pong[channel_id]
    await c.send('You lost!')
    pong_game=False
  else:
    pong[channel_id]=update_pong(pong[channel_id])
    await edit_message.edit(content=render_pong(pong[channel_id]))
    await asyncio.sleep(1)"""

def doc(link):
  index="0"
  bypass = False
  if not bypass and link.endswith("zip"):
    return "ERROR, no downloads"
  try: res = requests.get(link)
  except: 
    return "ERROR: invalid document."
  text = res.content
  text = str(text).split("\\xe2\\x80\\")
  result = "".join(text)
  result = result.replace("\\n", "\n").replace("x99", "'").replace("x9c", "\"").replace("x9d", "\"").replace("\\t", "")
  stuff = result.split("\"s\":\"")
  #'''
  out = []
  for s in stuff:
    s = s.split("\"},")
    for thing in s:
      if "{\"" not in thing and "\"}" not in thing and "{}" not in thing:
        out.append(thing)
  result = "".join(out).replace("\\", "").replace("u0003", "").replace("u003c3", "").replace("xa6", "…").replace("u0027", "'").replace("xf0x9fx85xb1xefxb8x8f", "🅱️").replace("u003d", "=").replace("x98", "'").replace("xe2x85x94", "⅔").replace("xe2x85x93", "⅓")
  #'''
  return result
  # wrapper = textwrap.TextWrapper(width=2000)
  # wordlist = wrapper.wrap(text=result.replace("\n", "║║"))
  # if not index.isdigit() or int(index) < 0 or int(index) > len(wordlist):
  #   return "Invalid index."
  # index = int(index)
  # try: return wordlist[index].replace("║║", "\n").replace("*", "\*").replace("_", "\_").replace("~", "\~").replace("`", "\`")
  # except: return "No content available."

def update_pong(pong_list):
  ball=pong_list[0]
  paddle1=pong_list[1]
  paddle2=pong_list[2]
  direction=pong_list[3]
  user=pong_list[4]
  if direction==1:#top-right
    if 1<=ball<=8:
      direction=3
      ball=ball+11
    elif ball==9:
      direction=4
      ball=ball+9
    elif ball%10==9:
      direction=2
      ball=ball-11
    else:
      ball=ball-9
  elif direction==2:#top-left
    if ball==0:
      direction=3
      ball=ball+11
    elif 1<=ball<=8:
      direction=4
      ball=ball+9
    elif ball%10==0:
      direction=1
      ball=ball-9
    else:
      ball=ball-11
  elif direction==3:#bottom-right
    if 90<=ball<=99:
      direction=5
    elif ball==89 and paddle1==98:
      direction=2
      ball=ball-11
    elif ball==89 and paddle2==98:
      direction=2
      ball=ball-11
    elif ball+11==paddle1 or ball+11==paddle2:
      direction=1
      ball=ball-9
    elif ball+10==paddle1 or ball+10==paddle2:
      direction=1
      ball=ball-9
    elif ball%10==9:
      direction=4
      ball=ball+9
    else:
      ball=ball+11
  elif direction==4:#bottom-left
    if 90<=ball<=99:
      direction=5
    elif ball==80 and paddle1==91:
      direction=1
      ball=ball-9
    elif ball==80 and paddle2==91:
      direction=1
      ball=ball-9
    elif ball+9==paddle1 or ball+9==paddle2:
      direction=2
      ball=ball-11
    elif ball+10==paddle1 or ball+10==paddle2:
      direction=2
      ball=ball-11
    elif ball%10==0:
      direction=3
      ball=ball+11
    else:
      ball=ball+9
  return [ball,paddle1,paddle2,direction,user]

def pong_move_right(pong_list):
  ball=pong_list[0]
  paddle1=pong_list[1]
  paddle2=pong_list[2]
  direction=pong_list[3]
  user=pong_list[4]
  if paddle2==99:
    return pong_list
  else:
    return [ball,paddle1+1,paddle2+1,direction,user]

def pong_move_left(pong_list):
  ball=pong_list[0]
  paddle1=pong_list[1]
  paddle2=pong_list[2]
  direction=pong_list[3]
  user=pong_list[4]
  if paddle1==90:
    return pong_list
  else:
    return [ball,paddle1-1,paddle2-1,direction,user]

def render_pong(pong_list):
  ball=pong_list[0]
  paddle1=pong_list[1]
  paddle2=pong_list[2]
  direction=pong_list[3]
  user=pong_list[4]
  current_pong=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  current_pong[ball]=1
  current_pong[paddle1]=2
  current_pong[paddle2]=2
  pong_board=[]
  for i in current_pong:
    if i==0:
      pong_board.append(':black_large_square:')
    elif i==1:
      pong_board.append(':white_circle:')
    elif i==2:
      pong_board.append(':left_right_arrow:')
  pong_board[9]=pong_board[9]+'\n'
  pong_board[19]=pong_board[19]+'\n'
  pong_board[29]=pong_board[29]+'\n'
  pong_board[39]=pong_board[39]+'\n'
  pong_board[49]=pong_board[49]+'\n'
  pong_board[59]=pong_board[59]+'\n'
  pong_board[69]=pong_board[69]+'\n'
  pong_board[79]=pong_board[79]+'\n'
  pong_board[89]=pong_board[89]+'\n'
  pong_board_message=''.join(pong_board)
  return pong_board_message

def timeconvert(timeToConvert):
  time=str(timeToConvert)[11:19]
  timelist=time.split(':')
  if int(timelist[0])>=8:
    timelist[0]=str(int(timelist[0])-8)
    timefinal2=str(timeToConvert)[0:10]
  else:
    timelist[0]=str(int(timelist[0])+16)
    time2=str(timeToConvert)[0:10]
    timelist2=time2.split('-')
    timelist2[2]=str(int(timelist2[2])-1)
    if timelist2[2]=="0":
      timelist2[1]=str(int(timelist2[1])-1)
      if timelist2[1]=="0":
        timelist2[0]=str(int(timelist2[0])-1)
        timelist2[1]="12"
    if timelist2[1]=="1":
      timelist2[2]="31"
    if timelist2[1]=="2":
      if int(timelist2[0])%4==0:
        timelist2[2]="29"
      else:
        timelist2[2]="28"
    if timelist2[1]=="3":
      timelist2[2]="31"
    if timelist2[1]=="4":
      timelist2[2]="30"
    if timelist2[1]=="5":
      timelist2[2]="31"
    if timelist2[1]=="6":
      timelist2[2]="30"
    if timelist2[1]=="7":
      timelist2[2]="31"
    if timelist2[1]=="8":
      timelist2[2]="31"
    if timelist2[1]=="9":
      timelist2[2]="30"
    if timelist2[1]=="10":
      timelist2[2]="31"
    if timelist2[1]=="11":
      timelist2[2]="30"
    if timelist2[1]=="12":
      timelist2[2]="31"
    if len(timelist2[1])==1:
      timelist2[1]="0"+timelist2[1]
    if len(timelist2[2])==1:
      timelist2[2]="0"+timelist2[2]
    timefinal2="-".join(timelist2)
  # if int(timelist[0])>7:
  #   if int(timelist[0])<20:
  #     timelist[0]=str(int(timelist[0])-7)
  #   else: 
  #     timelist[0]=str(int(timelist[0])-19)
  # else: 
  #   timelist[0]=str(int(timelist[0])+5)
  timefinal1=':'.join(timelist)
  timefinal=timefinal2+' '+timefinal1
  return timefinal

def timezone():
  ttime=datetime.datetime.now()
  pacific = pytz.timezone('Canada/Pacific')
  ttime = ttime.astimezone(pacific)
  return str(ttime)[0:19]

"""
def timezone():
  return str(datetime.datetime.now())[11:19]"""

memelist={
  'HELP': '**__MEME HELP__**\nuse ".meme <word>" to get a certain meme\n**surprised**: surprised pikachu\n**modern**: modern problems require modern solutions\n**joke**: am I a joke to you\n**analysis**: kowalski, analysis\n**excuseme**: excuse me what the frick\n**damage**: that\'s a lotta damage\n**choices**: the hardest choices require the strongest wills\n**balance**: perfectly balanced, as all things should be\n**toll**: this day extracts a heavy toll\n**myself**: fine, I\'ll do it myself\n**disappointing**: reality is often disappointing\n**reality**: now, reality can be whatever I want\n**smile**: this does put a smile on my face\n**endgame**: we\'re in the endgame now\n**illegal**: wait that\'s illegal\n**pointing**: spidermen pointing at each other\n**me**: of course I know him, he\'s me\n**surprise**: a surprise to be sure, but a welcome one\n**free**: it\'s free real estate\n**quantum**: actually, quantum mechanics forbids this\n**greatness**: we were on the verge of greatness, we were this close\n**outstanding**: outstanding move\n**walking**: theresa may walking meme\n**crying**: kid crying\n**yesno**: well yes but actually no\n**happy**: happiness noises\n**rewind**: it\'s rewind time\n**doubt**: press x to doubt\n**history**: this is going down in history\n**die**: I have decided that I want to die\n**honest**: it ain\'t much, but it\'s honest work\n**treasure**: I guide others to a treasure I cannot possess\n**gay**: why are you gay\n**delusional**: are you delusional? do you suffer from mental illness?\n**pretend**: I\'m gonna pretend I didn\'t see that\n**confusion**: visible confusion\n**tom**: unsettled tom meme\n**first**: they had us in the first half, not gonna lie\n**nothing**: wow look, nothing!\n**treason**: it\'s treason then\n**trap**: it\'s a trap!\n**destroy**: you have become the very thing you swore to destroy\n**remember**: I hope they remember you\n**yes**: thor yes',
  'HELP2': '**sneaky**: see, I pulled a sneaky on ya\n**sweating**: guy sweating\n**salute**: guy crying and saluting\n**failure**: you could not live with your own failure\n**high**: I\'ve just never been this high before\n**hurt**: it hurt itself in its confusion\n**yourself**: congratulations, you played yourself\n**speed**: I am speed\n**win**: I see this as an absolute win!\n**no**: no, I don\'t think I will\n**fool**: you fool! you fell victim to one of the classic blunders\n**monkey**: monkey puppet looking scared\n**seen**: hey, I\'ve seen this one!\n**another**: there is another\n**ironic**: prequel ironic meme\n**vectored**: you just got vectored\n**fallen**: in case you haven\'t noticed, you\'ve fallen right into my trap\n**salvation**: a small price to pay for salvation\n**wise**: who are you, who are so wise in the ways of science?\n**joker**: joker dancing on stairs\n**brain**: yeah this is big brain time\n**genius**: sometimes my genius is, its almost frightening\n**sorry**: i\'m sorry little one\n**police**: kirby\'s calling the police',
  'SURPRISED': 'https://cdn.discordapp.com/attachments/442535708599779340/514253993505980416/download.png', 
  'POLICE': 'https://media.discordapp.net/attachments/758908682456137752/778027993423544400/iu.png',
  'GENIUS':
  'https://media.discordapp.net/attachments/526257599612452884/679943372462489600/Screen_Shot_2020-02-19_at_10.51.55_095PM.png',
  'JOKER': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg2.looper.com%2Fimg%2Fgallery%2Fwe-now-know-why-joaquins-joker-dances-so-much%2Fhow-did-joaquin-phoenix-prepare-for-all-that-joker-dancing-1570811447.jpg&f=1&nofb=1',
  'WISE': 'https://media.discordapp.net/attachments/526257599612452884/679939269879660564/Screen_Shot_2020-02-19_at_10.35.43_834PM.png',
  'BRAIN':
  'https://media.discordapp.net/attachments/526257599612452884/679938600066088960/Screen_Shot_2020-02-19_at_10.png',
  'SALVATION':
  'https://i.kym-cdn.com/entries/icons/original/000/029/766/salvation.jpg',
  'FALLEN':
  'https://media.discordapp.net/attachments/526257599612452884/666134855263977489/Screen_Shot_2020-01-12_at_8.21.47_413PM.png?width=400&height=169',
  'VECTORED':
  'https://media.discordapp.net/attachments/511797229913243649/657459938334998528/1576250209693.png?width=400&height=226',
  'IRONIC':
  'https://media.discordapp.net/attachments/526257599612452884/652994910869258262/Screen_Shot_2019-12-07_at_2.08.18_584PM.png?width=401&height=250',
  'SORRY':
  'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgur.com%2FvAwg7t1.jpg&f=1&nofb=1',
  'ANOTHER':
  'https://media.discordapp.net/attachments/526257599612452884/631966047452397589/Screen_Shot_2019-10-10_at_2.26.30_466PM.png?width=400&height=247',
  'SEEN' : 'https://media.discordapp.net/attachments/526257599612452884/625450594899066881/Screen_Shot_2019-09-22_at_2.57.05_870PM.png?width=400&height=208',
  'MONKEY': 'https://media.discordapp.net/attachments/526257599612452884/598386883419963435/Screen_Shot_2019-07-09_at_10.27.32_419PM.png?width=400&height=241',
  'NO': 'https://media.discordapp.net/attachments/572274707684917261/583526726936690688/Screen_Shot_2019-05-29_at_10.26.36_878PM.png?width=400&height=231',
  'YOURSELF': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FJkWkkQgwAxc%2Fhqdefault.jpg&f=1',
  'SPEED': 'https://media.discordapp.net/attachments/437047996203401216/577621281026080805/Screen_Shot_2019-05-13_at_3.19.36_456PM.png',
  'WIN': 'https://media.discordapp.net/attachments/526257599612452884/578079399501365278/Screen_Shot_2019-05-14_at_9.40.49_942PM.png?width=383&height=301',
  'HURT': 'https://media.discordapp.net/attachments/508155749030166546/564991869553999902/iu.png',
  'HIGH': 'https://media.discordapp.net/attachments/493948606294786049/562510826356080692/885845e01d4590b077e3f786214b7890.png',
  'FAILURE': 'https://media.discordapp.net/attachments/508155749030166546/562811149985382411/failure.png?width=400&height=260',
  'SALUTE': 'https://media.discordapp.net/attachments/562474519072210945/562503436818448384/Screen_Shot_2019-04-01_at_10.07.16_635PM.png?width=265&height=301',
  'SWEATING': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.giphy.com%2Fmedia%2FcZHNk21INIlKo%2Fgiphy-facebook_s.jpg&f=1',
  'DESTROY': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.mememaker.net%2Fapi%2Fbucket%3Fpath%3Dstatic%2Fimg%2Fmemes%2Ffull%2F2017%2FJan%2F5%2F3%2Fyou-have-become-the-very-thing-you-swore-to-destroy38.jpg&f=1',
  'NOTHING': 'https://media.discordapp.net/attachments/526257599612452884/559929124551000067/Screen_Shot_2019-03-25_at_7.36.55_057PM.png?width=400&height=224',
  'CONFUSION': 'https://media.discordapp.net/attachments/771772792031019028/782003373100630086/Screen_Shot_2020-11-27_at_2.02.09_PM.png',
  'TOM': 'https://media.discordapp.net/attachments/526257599612452884/558882107485847592/Screen_Shot_2019-03-22_at_10.17.21_907PM.png?width=380&height=300',
  'MODERN': 'https://media.discordapp.net/attachments/526257599612452884/542130684152774686/Screen_Shot_2019-02-04_at_3.53.33_875PM.png?width=399&height=300',
  'JOKE': 'https://media.discordapp.net/attachments/526257599612452884/542133321488924683/Screen_Shot_2019-02-04_at_4.03.52_651PM.png?width=400&height=262',
  'ANALYSIS': 'https://media.discordapp.net/attachments/526257599612452884/542134165420900354/Screen_Shot_2019-02-04_at_4.05.51_054PM.png?width=400&height=225', 
  'EXCUSEME': 'https://media.discordapp.net/attachments/526257599612452884/542135919206072340/Screen_Shot_2019-02-04_at_4.14.08_264PM.png?width=400&height=237', 
  'DAMAGE': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2Fnyz7c9k0dia01.jpg&f=1',
  'CHOICES': 'https://media.discordapp.net/attachments/526257599612452884/542136762466828289/Screen_Shot_2019-02-04_at_4.17.43_076PM.png?width=400&height=275', 
  'BALANCE': 'https://media.discordapp.net/attachments/526257599612452884/598390531688497172/Screen_Shot_2019-07-09_at_10.49.57_692PM.png?width=400&height=168', 
  'TOLL': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.mPj-RXzGeysPoOL26ICcmQHaHa%26pid%3D15.1&f=1',
  'MYSELF': 'https://media.discordapp.net/attachments/526257599612452884/542139501200277514/Screen_Shot_2019-02-04_at_4.28.39_014PM.png?width=400&height=212', 
  'DISAPPOINTING': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2F3.bp.blogspot.com%2F-46_QBfCjdbM%2FXBoYHVPUeEI%2FAAAAAAAACPs%2Fq9q2p886uYIYiMLQcdQv0TS1vBDmTsMNQCLcBGAs%2Fs1600%2FScreenshot_2018-11-17-01-29-59-765.jpeg&f=1', 
  'REALITY': 'https://i.imgflip.com/2pqmmt.jpg',
  'FIRST': 'https://media.discordapp.net/attachments/508155749030166546/559573265933402114/Z.png',
  'SMILE': 'https://media.discordapp.net/attachments/526257599612452884/542547500662521878/Screen_Shot_2019-02-05_at_7.29.36_654PM.png?width=400&height=183',
  'ENDGAME': 'https://media.discordapp.net/attachments/526257599612452884/543982391300194304/Screen_Shot_2019-02-09_at_6.31.19_380PM.png?width=400&height=184',
  'ILLEGAL': 'https://media.discordapp.net/attachments/526257599612452884/544050527349243905/pdall9ervof21.png?width=400&height=187', 
  'POINTING': 'https://media.discordapp.net/attachments/437047996203401216/545055950239956992/C-658VsXoAo3ovC.png?width=400&height=225', 
  'ME': 'https://media.discordapp.net/attachments/526257599612452884/545137608301215774/Screen_Shot_2019-02-12_at_11.01.31_077PM.png?width=400&height=213',
  'SURPRISE': 'https://media.discordapp.net/attachments/526257599612452884/545282740031979531/Screen_Shot_2019-02-13_at_8.38.37_483AM.png?width=400&height=246',
  'FREE': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FGXskBQ32tlc%2Fmaxresdefault.jpg&f=1',
  'QUANTUM': 'https://media.discordapp.net/attachments/511797229913243649/545489075923320850/1f969d7__01__01__01.jpg?width=400&height=221',
  'GREATNESS': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2Fthumb_we-were-on-the-verge-of-greatness-we-were-this-49902990.png&f=1',
  'OUTSTANDING': 'https://media.discordapp.net/attachments/526257599612452884/546548529196171267/Screen_Shot_2019-02-16_at_8.28.07_205PM.png?width=400&height=217',
  'WALKING': 'https://media.discordapp.net/attachments/437047996203401216/547168178405507093/iu.png?width=400&height=219',
  'CRYING': 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fstatic.elmundo.sv%2Fwp-content%2Fuploads%2F2018%2F04%2Fmeme-ni%25C3%25B1o-llorando.jpg&f=1',
  'YESNO': 'https://media.discordapp.net/attachments/526257599612452884/547995482182647860/Screen_Shot_2019-02-20_at_8.18.04_717PM.png?width=400&height=232',
  'HAPPY': 'https://media.discordapp.net/attachments/526257599612452884/548369627852439552/Screen_Shot_2019-02-21_at_9.04.50_052PM.png?width=400&height=264',
  'REWIND': 'https://media.discordapp.net/attachments/526257599612452884/549070965943042058/Screen_Shot_2019-02-23_at_7.31.41_647PM.png?width=400&height=211',
  'DOUBT': 'https://cdn.discordapp.com/attachments/442535708599779340/519738267738963968/download.png',
  'HISTORY': 'https://media.discordapp.net/attachments/526257599612452884/549105199294316564/Screen_Shot_2019-02-23_at_9.47.47_316PM.png?width=400&height=221',
  'DIE': 'https://media.discordapp.net/attachments/526257599612452884/551986187884036116/Screen_Shot_2019-03-03_at_8.35.24_102PM.png?width=400&height=207',
  'HONEST': 'https://media.discordapp.net/attachments/511797688979816478/552454007184949249/work.png?width=400&height=225',
  'TREASURE': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2F1.bp.blogspot.com%2F-4TsHuEydG7Q%2FW6XxnLmDwLI%2FAAAAAAAACIA%2Fb7FWlaUIOUgyAWeP_4hiMUv1ZQDqpTUnQCLcBGAs%2Fs1600%2FScreenshot_2018-09-20-22-19-09-049.jpeg&f=1',
  'GAY': 'https://media.discordapp.net/attachments/526257599612452884/553827165263757312/Screen_Shot_2019-03-08_at_10.31.01_460PM.png?width=400&height=276',
  'DELUSIONAL': 'https://media.discordapp.net/attachments/526257599612452884/553827943810334725/Screen_Shot_2019-03-08_at_10.34.16_739PM.png?width=400&height=222',
  'PRETEND': 'https://media.discordapp.net/attachments/526257599612452884/560295575531028480/Screen_Shot_2019-03-26_at_7.54.04_679PM.png?width=315&height=300',
  'TREASON': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2F9nvprof2ybl01.jpg&f=1',
  'TRAP': 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.htxt.co.za%2Fwp-content%2Fuploads%2F2017%2F01%2Fits-a-trap.jpg&f=1',
  'REMEMBER': 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Xdl0w4xBi0krtw-3lUP16wHaHT%26pid%3DApi&f=1',
  'YES': 'https://media.discordapp.net/attachments/526257599612452884/561412953921028097/Screen_Shot_2019-03-29_at_9.54.09_344PM.png?width=400&height=169',
  'SNEAKY': 'https://media.discordapp.net/attachments/526257599612452884/562108651997888513/Screen_Shot_2019-03-31_at_7.58.49_056PM.png?width=400&height=226',
  'FOOL':
  'https://media.discordapp.net/attachments/511797229913243649/595337531458060308/Screen_Shot_2019-07-01_at_12.38.31_830PM.png?width=363&height=300'
  }

def filtered(I):
  filteredmessagelist=[]
  for i in I:
    if i.upper() in alphabet:
      filteredmessagelist.append(i)
  filteredmessage=''.join(filteredmessagelist)
  return filteredmessage

client = commands.Bot(command_prefix = 'ajdfkajdflaksdjflaskfdjalsdfkjasldkfjasldfkasjdlaksdjflasdfkj')
buttons = ButtonsClient(client)

@client.event
async def on_ready():
  print ('Bot is ready.')
  playinglist=['Fortnite', 'Minecraft', 'Half Life', 'with the soul stone', 'with dust', 'with a see saw', 'balance knife on finger', 'with the infinity gauntlet', 'on my chair', 'snap', 'with Gamora', 'rewind time', 'collect the infinity stones', 'with fire', '5050 tickets', 'Among Us', '#RestoreTheSnyderVerse', 'pi runner']
  watchinglist=['my farm grow', 'Nebula\'s memories', 'alternate Nebula\'s memories', 'WandaVision', 'Avengers: Infinity War', 'Avengers: Endgame', 'spoilers', 'half the universe get dusted', 'the sun rise over a grateful universe', 'Gamora die', 'Frozen 2', 'the Snyder Cut', 'the Eternals']
  listeninglist=['Nebula scream', 'the Avengers Theme', 'Star Lord rant', 'Hooked on a Feeling', 'Thanos radio, Thanos radio']
  global keklist
  keklist = []
  kekdatachannel = client.get_channel(kekdata)
  async for kekmessage in kekdatachannel.history(limit = None):
    keklist.append(kekmessage)
  global terms
  terms=[]
  global terms_only
  terms_only=[]
  transterms_channel=client.get_channel(transterms_data)
  async for m in transterms_channel.history(limit=None):
    terms.append(m.embeds[0])
    terms_only.append(m.embeds[0].title)
  terms_only.sort(key = lambda x: x.lower())
  global terms2
  terms2={}
  global terms_only2
  terms_only2=[]
  transdoc=doc('https://docs.google.com/document/d/1VHEL-f2al0r-M7Oy2jowrlbUJpuwefQ71Z4t4pd9dmg/edit')
  transdocsplit=transdoc.split('\n')
  for i in transdocsplit:
    if re.search(": ", i):
      thetermsplit=i.split(": ")
      terms2[thetermsplit[0]]=": ".join(thetermsplit[1:])
      terms_only2.append(thetermsplit[0])
  while True:
    gamechoice=randint(1,len(playinglist)+len(watchinglist)+len(listeninglist))
    if 1<=gamechoice<=len(playinglist):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=random.choice(playinglist)))
    elif len(playinglist)<gamechoice<=len(playinglist)+len(watchinglist):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(watchinglist)))
    elif len(playinglist)+len(watchinglist)<gamechoice<=len(playinglist)+len(watchinglist)+len(listeninglist):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(listeninglist)))
    await asyncio.sleep(300)
  
@client.event
async def on_message_edit(before, after):
  channel=before.channel
  author=before.author
  content=before.content
  if len(before.embeds)==0 and len(after.embeds)==0:
    if str(channel.id) in db['editedmessage'].keys():
      tempdb = db['editedmessage']
      tempdb[str(channel.id)].insert(0, before.content)
      db['editedmessage']=tempdb
      tempdb=db['editednew']
      tempdb[str(channel.id)].insert(0,after.content)
      db['editednew']=tempdb
      tempdb=db['editedauthor']
      tempdb[str(channel.id)].insert(0, str(before.author))
      db['editedauthor']=tempdb
      tempdb=db['editedtime']
      tempdb[str(channel.id)].insert(0,timezone())
      db['editedtime']=tempdb
      if len(db['editedmessage'][str(channel.id)])>snipemax:
        tempdb=db['editedmessage']
        tempdb[str(channel.id)]=tempdb[str(channel.id)][0:snipemax]
        db['editedmessage']=tempdb
        tempdb=db['editednew']
        tempdb[str(channel.id)]=tempdb[str(channel.id)][0:snipemax]
        db['editednew']=tempdb
        tempdb=db['editedauthor']
        tempdb[str(channel.id)]=tempdb[str(channel.id)][0:snipemax]
        db['editedauthor']=tempdb
        tempdb=db['editedtime']
        tempdb[str(channel.id)]=tempdb[str(channel.id)][0:snipemax]
        db['editedtime']=tempdb
    else:
      tempdb=db['editedmessage']
      tempdb[str(channel.id)]=[]
      tempdb[str(channel.id)].append(before.content)
      db['editedmessage']=tempdb
      tempdb=db['editednew']
      tempdb[str(channel.id)]=[]
      tempdb[str(channel.id)].append(after.content)
      db['editednew']=tempdb
      tempdb=db['editedauthor']
      tempdb[str(channel.id)]=[]
      tempdb[str(channel.id)].append(str(before.author))
      db['editedauthor']=tempdb
      tempdb=db['editedtime']
      tempdb[str(channel.id)]=[]
      tempdb[str(channel.id)].append(timezone())
      db['editedtime']=tempdb

@client.event
async def on_bulk_message_delete(messages):
  logging=client.get_channel(dlogging)
  outmessage=""
  for i in messages:
    deletedAttachment = ""
    if len(i.attachments)>0: 
      deletedAttachment = i.attachments[0].url
    if str(i.channel.id) in db['deletedmessage'].keys():
      tempdb=db['deletedmessage']
      tempdb[str(i.channel.id)].insert(0, i.content+'\t'+deletedAttachment)
      db['deletedmessage']=tempdb
      tempdb=db['deletedauthor']
      tempdb[str(i.channel.id)].insert(0,str(i.author))
      db['deletedauthor']=tempdb
      tempdb=db['deletedtime']
      tempdb[str(i.channel.id)].insert(0,timezone())
      db['deletedtime']=tempdb
      tempdb=db['deletedtime2']
      tempdb[str(i.channel.id)].insert(0, (timeconvert(i.created_at))[0:19])
      db['deletedtime2']=tempdb
    else:
      tempdb=db['deletedmessage']
      tempdb[str(i.channel.id)]=[i.content+'\t'+deletedAttachment]
      db['deletedmessage']=tempdb
      tempdb=db['deletedauthor']
      tempdb[str(i.channel.id)]=[str(i.author)]
      db['deletedauthor']=tempdb
      tempdb=db['deletedtime']
      tempdb[str(i.channel.id)]=[timezone()]
      db['deletedtime']=tempdb
      tempdb=db['deletedtime2']
      tempdb[str(i.channel.id)]=[(timeconvert(i.created_at))[0:19]]
      db['deletedtime2']=tempdb
    if deletedAttachment=="":
      outmessage = outmessage +timezone()+': {}, {}, Deleted message from {}: {}: {}\n'.format(i.guild, i.channel, (timeconvert(i.created_at))[0:19], i.author, i.content)
    else:
      outmessage = outmessage +timezone()+': {}, {}, Deleted message from {}: {}: {}'.format(i.guild, i.channel, (timeconvert(i.created_at))[0:19], i.author, i.content)+"https://media.discordapp.net"+(deletedAttachment)[26:]+'\n'
  i=messages[0]
  if len(db['deletedmessage'][str(i.channel.id)])>snipemax:
    tempdb=db['deletedmessage']
    tempdb[str(i.channel.id)]=db['deletedmessage'][str(i.channel.id)][0:snipemax]
    db['deletedmessage']=tempdb
    tempdb=db['deletedauthor']
    tempdb[str(i.channel.id)]=db['deletedauthor'][str(i.channel.id)][0:snipemax]
    db['deletedauthor']=tempdb
    tempdb=db['deletedtime']
    tempdb[str(i.channel.id)]=db['deletedtime'][str(i.channel.id)][0:snipemax]
    db['deletedtime']=tempdb
    tempdb=db['deletedtime2']
    tempdb[str(i.channel.id)]=db['deletedtime2'][str(i.channel.id)][0:snipemax]
    db['deletedtime2']=tempdb
  while len(outmessage) > 2000:
    await logging.send(outmessage[0:2000])
    outmessage=outmessage[2000:]
  await logging.send(outmessage)

@client.event
async def on_message_delete(message):
  author=message.author
  content=message.content
  channel=message.channel
  contents=message.content.split(' ')
  deletedAttachment = ""
  datachannel=client.get_channel(631300490776412160)
  if len(message.attachments)>0: 
    deletedAttachment = message.attachments[0].url
  if str(channel.id) in db['deletedmessage'].keys():
    tempdb=db['deletedmessage']
    tempdb[str(channel.id)].insert(0, content+'\t'+deletedAttachment)
    db['deletedmessage']=tempdb
    tempdb=db['deletedauthor']
    tempdb[str(channel.id)].insert(0,str(author))
    db['deletedauthor']=tempdb
    tempdb=db['deletedtime']
    tempdb[str(channel.id)].insert(0,timezone())
    db['deletedtime']=tempdb
    tempdb=db['deletedtime2']
    tempdb[str(channel.id)].insert(0, (timeconvert(message.created_at))[0:19])
    db['deletedtime2']=tempdb
    if len(db['deletedmessage'][str(channel.id)])>snipemax:
      tempdb=db['deletedmessage']
      tempdb[str(channel.id)]=db['deletedmessage'][str(channel.id)][0:snipemax]
      db['deletedmessage']=tempdb
      tempdb=db['deletedauthor']
      tempdb[str(channel.id)]=db['deletedauthor'][str(channel.id)][0:snipemax]
      db['deletedauthor']=tempdb
      tempdb=db['deletedtime']
      tempdb[str(channel.id)]=db['deletedtime'][str(channel.id)][0:snipemax]
      db['deletedtime']=tempdb
      tempdb=db['deletedtime2']
      tempdb[str(channel.id)]=db['deletedtime2'][str(channel.id)][0:snipemax]
      db['deletedtime2']=tempdb
  else:
    tempdb=db['deletedmessage']
    tempdb[str(channel.id)]=[content+'\t'+deletedAttachment]
    db['deletedmessage']=tempdb
    tempdb=db['deletedauthor']
    tempdb[str(channel.id)]=[str(author)]
    db['deletedauthor']=tempdb
    tempdb=db['deletedtime']
    tempdb[str(channel.id)]=[timezone()]
    db['deletedtime']=tempdb
    tempdb=db['deletedtime2']
    tempdb[str(channel.id)]=[(timeconvert(message.created_at))[0:19]]
    db['deletedtime2']=tempdb
  for word in contents:
    if message.author.bot==True:
      break
    elif channel.id in incogchannel:
      break
    elif channel.id in dirtchannel:
      break
    elif word=='.meme':
      break
    elif content=='1':
      break
    elif content=='2':
      break
    elif content=='3':
      break
    elif content=='4':
      break
    elif content=='5':
      break
    elif content=='6':
      break
    elif content=='7':
      break
    elif content=='8':
      break
    elif content=='9':
      break
    elif content=='0':
      break
    elif content.upper()=='CONFIRM':
      break
    elif content.upper()=='EXIT':
      break
    elif content.upper().startswith('!RELOAD'):
      break
    elif message.channel.id==804810342160007248:
      yesornot = await datachannel.fetch_message(807304206016839741)
      if yesornot.content.upper()=="YES":
        break
  else:
    logging=client.get_channel(dlogging)
    if len(deletedAttachment)>0:
      outmessage = timezone()+': {}, {}, Deleted message from {}: {}: {} {}'.format(message.guild, channel, (timeconvert(message.created_at))[0:19], author, content, "https://media.discordapp.net"+(deletedAttachment)[26:])
    else: 
      outmessage = timezone()+': {}, {}, Deleted message from {}: {}: {}'.format(message.guild, channel, (timeconvert(message.created_at))[0:19], author, content)
    if len(outmessage)>2000:
      await logging.send(outmessage[0:2000])
      await logging.send(outmessage[2000:])
    else:
      await logging.send(outmessage)

@client.event
async def on_message(message):
  await client.process_commands(message)
  #print (message.content)
  channel=message.channel
  datachannel=client.get_channel(631300490776412160)
  #numberofchannelsmessage=await datachannel.fetch_message(631300525685735425)
  # numberofchannels=int(numberofchannelsmessage.content)
  send_message = ''
    
  if channel.id in memes:
    if len(message.embeds)==0:
      if len(message.attachments)==0:
        try:
          await message.delete()
        except discord.errors.NotFound:
          empty=1
    if len(message.attachments)>0:
      try:
        #await message.add_reaction(':donphan2:533499869315334154')
        await message.add_reaction(':donphan:711428671780421702')
        await message.add_reaction (':nahpnod:711426389219344394')
      except discord.errors.NotFound:
        empty=1
    elif len(message.embeds)>0:
      try: 
        #await message.add_reaction(':donphan2:533499869315334154')
        await message.add_reaction(':donphan:711428671780421702')
        await message.add_reaction (':nahpnod:711426389219344394')
      except discord.errors.NotFound:
        empty=1

  if channel.id in dirtchannel:
    await message.delete()

  if channel.id in gamemode.keys():
    try:
      await message.delete()
    except discord.errors.NotFound:
      empty=1
    # if message.content.upper()=='EXIT':
    #   if gamemode[channel.id]==message.author.id:
    #     pong_game=False
    #     del gamemode[channel.id]
    #     await channel.send('Exited game')

  if channel.id in pong_channels:
    if pong[channel.id][4]==message.author.id:
      # if message.content.upper()=='EXIT':
      #   pong_channels.remove(channel.id)
      #   del pong[channel.id]
      #   pong_game=False
      if message.content.upper()=='1':
        pong[channel.id]=pong_move_left(pong[channel.id])
      if message.content.upper()=='2':
        pong[channel.id]=pong_move_right(pong[channel.id])

  if str(channel).upper().startswith('DIRECT MESSAGE WITH'):
    if message.author.id==thanos:
      empty = 1
    else:
      d=client.get_channel(messaging)
      await d.send(str(channel)+': '+message.content)

  if message.author.bot==False:

    # allchannels1=[]
    # magiccow1=client.get_guild(433856438604136459)
    # for c in magiccow1.channels:
    #   allchannels1.append(c.name)
    # if len(allchannels1)!=numberofchannels:
    #   dchannel=client.get_channel(donsongeneral)
    #   await dchannel.send('# of channels has changed')

    if message.author.id==donsonid:
      if message.content.upper()=='SENDCHANNELS':
        mc_channels=[]
        magiccow1=client.get_guild(mc_server)
        for c in magiccow1.channels: 
          mc_channels.append(c.name)
        print(mc_channels)
        channelslist='\n'.join(mc_channels)
        await channel.send(channelslist)
        await channel.send(len(mc_channels))
      if message.content.upper().startswith('.NICK '):
        thanos_user = message.guild.get_member(thanos)
        await thanos_user.edit(nick=message.content[6:])
        await message.delete()
      if message.content.upper()==".RESETNICK":
        thanos_user = message.guild.get_member(thanos)
        await thanos_user.edit(nick=None)
        await message.delete()
      if message.content.upper()==".RESETDOC":
        terms2.clear()
        for i in terms_only2:
          terms_only2.remove(i)
        transdoc=doc('https://docs.google.com/document/d/1VHEL-f2al0r-M7Oy2jowrlbUJpuwefQ71Z4t4pd9dmg/edit')
        transdocsplit=transdoc.split('\n')
        for i in transdocsplit:
          if re.search(": ", i):
            thetermsplit=i.split(": ")
            terms2[thetermsplit[0]]=": ".join(thetermsplit[1:])
            terms_only2.append(thetermsplit[0])
        await channel.send("doc reset")
      if message.content.upper().startswith("DONPURGE "):
        del_limit = int(message.content[9:])
        async for msg in message.channel.history(limit = del_limit):
          if msg.author.id == donsonid:
            await msg.delete()
      
      if message.content.upper()=="RPS":
        await buttons.send(content = "Choose an option!", channel = channel.id, components = [ActionRow ([Button(label = "Rock", style = ButtonType().Primary, custom_id="button_rock"), Button(label = "Paper", style = ButtonType().Primary, custom_id="button_paper"), Button(label = "Scissors", style = ButtonType().Primary, custom_id="button_scissors")])])

    if message.author.id not in ban:

      if message.content.upper()==('STOPTHANOS'):
        if message.author.id in mod:
          await channel.send('<@!231259532863602698>')
          await client.close()
          print ('Bot stopped')

      if message.content.upper()==('CHANNEL ID'):
          await channel.send(channel.id)

      if message.content.upper()==('SERVER ID'):
          await channel.send(message.guild.id)
        
      if message.content.upper().startswith('PURGE'):
        if message.author.id in mod:
          number=(message.content[6:len(message.content):1])
          Number=True
          for i in number:
            if i not in numberlist:
              await channel.send('You must purge a positive integer!')
              Number=False
              break
          if message.content.upper()=='PURGE':
            Number=False
          if Number==True:
            number=int(number)+1
            if number>10000:
              await channel.send('The max you can purge is 9999')
            else:
              await channel.purge(limit=number)
              """
            elif number<101:
              await channel.purge(limit=number)
            else:
              n=number
              while n>100:
                await channel.purge(limit=100)
                n=n-100
              await channel.purge(limit=n)"""

      if message.content.upper()==('MOUND OF DIRT'):
          try:
            await message.delete()
          except discord.errors.NotFound:
            empty=1
          await channel.send('The channel has been dirted. To undirt, type `undirt`')
          await asyncio.sleep(0.5)
          dirtchannel.add(channel.id)
        
      if message.content.upper()==('UNDIRT'):
        if channel.id in dirtchannel:
          dirtchannel.remove(channel.id)
          await channel.send('The channel has been undirted')
        else:
          await channel.send('The channel was never dirted.')

      if message.content.upper()==('INCOGNITO'):
        await message.delete()
        await channel.send('The channel is in incognito mode. To exit, use `exit incognito`')
        await asyncio.sleep(1)
        incogchannel.add(channel.id)

      if message.content.upper()==('EXIT INCOGNITO'):
        if channel.id in incogchannel:
          incogchannel.remove(channel.id)
          await channel.send('You have exited incognito mode')
        else:
          await channel.send('The channel was never in incognito')

      if message.content.upper().startswith ('CHOOSE '):
        choose=message.content[7:]
        choices=choose.split(' | ')
        send_message = send_message + random.choice(choices)+', I choose you!\n'

      # if message.content.upper() == 'TRIGGER':
      #   thisChannelMembers=channel.members
      #   thisChannelNoBots=[]
      #   await message.delete()
      #   for i in thisChannelMembers:
      #     if i.bot:
      #       empty=1
      #     else:
      #       thisChannelNoBots.append(i)
      #   chosenMember=random.choice(thisChannelNoBots)
      #   await channel.send('<@!'+str(chosenMember.id)+'>')
      
      if message.content.upper().startswith('SAY '):
        if message.author.id in mod:
          new_message=message.content[4:]
          await message.delete()
          await channel.send(new_message)

      if message.content.upper().startswith('QUOTE '):
        print(message.content)
        if (((message.content[6:9]=='<@!') or (message.content[6:8]=='<@')) and (len(message.mentions)>0)):
          hooks = await message.channel.webhooks()
          hasthanos = False
          for i in hooks:
            if i.user.id == thanos:
              hook = i
              hasthanos = True
              break
          if hasthanos == False:
            hook = await message.channel.create_webhook(name = "Thanos", avatar = None)
          hook = Webhook.partial(hook.id, hook.token, adapter=RequestsWebhookAdapter())
          quotemessagesplit = message.content.split(' ')
          quotemessage=' '.join(quotemessagesplit[2:])
          quotee = message.mentions[0]
          #quoteeid = quotemessagesplit[1][3:len(quotemessagesplit[1])-1]
          hook.send(quotemessage, username=quotee.display_name, avatar_url = quotee.avatar_url)
        else:
          hooks = await message.channel.webhooks()
          hasthanos = False
          for i in hooks:
            if i.user.id == thanos:
              hook = i
              hasthanos = True
              break
          if hasthanos == False:
            hook = await message.channel.create_webhook(name = "Thanos", avatar = None)
          hook = Webhook.partial(hook.id, hook.token, adapter=RequestsWebhookAdapter())
          quotemessage = message.content[6:]
          hook.send(quotemessage, username=message.author.display_name, avatar_url = message.author.avatar_url)
      
      if message.content.upper().startswith('HOOK '):
        if message.content.upper().startswith('HOOK HELP'):
          await channel.send('Use the command as follows:\n\nhook --content <message content> --name <message author name> --avatar <message avatar url link>')
        else:
          contentsplit=message.content.split(' --content ')
          if len(contentsplit) < 2:
            await channel.send('Use `hook help` to see correct usage of the command')
            return
          namesplit=' --content '.join(contentsplit[1:]).split(' --name ')
          if len(namesplit) < 2:
            await channel.send('Use `hook help` to see correct usage of the command')
            return
          urlsplit=' --name '.join(namesplit[1:]).split(' --avatar ')
          if len(urlsplit) < 2:
            await channel.send('Use `hook help` to see correct usage of the command')
            return
          content = namesplit[0]
          name = urlsplit[0]
          avatar = urlsplit[1]
          hooks = await message.channel.webhooks()
          hasthanos = False
          for i in hooks:
            if i.user.id == thanos:
              hook = i
              hasthanos = True
              break
          if hasthanos == False:
            hook = await message.channel.create_webhook(name = "Thanos", avatar = None)
          hook = Webhook.partial(hook.id, hook.token, adapter=RequestsWebhookAdapter())
          try:
            hook.send(content, username = name, avatar_url = avatar)
          except discord.errors.HTTPException:
            await channel.send('Invalid avatar url, please try again.')

      if message.content.upper()=='TIME':
        await channel.send(timezone())

      if message.content.upper().startswith('POLL '):
        options=message.content[5:].split(' | ')
        if len(options)>21:
          await channel.send('You can only have 20 options!')
        else:
          title=options[0]
          options=options[1:]
          letterTicker=0
          votingOptions=''
          for i in options:
            votingOptions=votingOptions+':regional_indicator_'+alphabet[letterTicker].lower()+':: ' + i + '\n'
            letterTicker=letterTicker+1
          em = discord.Embed(colour=0x36393F)
          em.add_field(name = title, value = votingOptions, inline = False)
          poll_message = await channel.send(embed=em)
          reactionTicker=0
          while reactionTicker < len(options):
            await poll_message.add_reaction(regionalindicators[reactionTicker])
            reactionTicker=reactionTicker+1
      
      if message.content.upper().startswith('BAN '):
        if message.author.id in mod:
          if len(message.mentions)>0:
            person=message.mentions[0]
            ban.append(person.id)
            await channel.send(str(person) + ' has been banned from Thanos.')

      if message.content.upper().startswith('UNBAN '):
        if message.content.upper()==('UNBAN ALL'):
          if message.author.id in mod:
            while len(ban)>0:
              ban.remove(ban[0])
            await channel.send('Everyone has been unbanned.')
        else:
          if message.author.id in mod:
            if len(message.mentions)>0:
              person=message.mentions[0]
              if person.id in ban:
                while person.id in ban:
                  ban.remove(person.id)
                await channel.send(str(person) + ' has been unbanned from Thanos.')
              else:
                await channel.send(str(person) + ' was never banned.')
      
      if message.content.upper()==('BANLIST'):
        if len(ban)==0:
          await channel.send('Nobody is banned.')
        elif len(set(ban))==1:
          await channel.send(str(client.get_user(ban[0])) + ' is banned.')
        else:
          banned=[]
          for i in set(ban):
            banned.append(str(client.get_user(i)))
          bannedlist=', '.join(banned)
          await channel.send(bannedlist + ' are banned.')

      if re.search("donson", message.content, flags = re.IGNORECASE):
        try: 
          message.guild.id
          if re.search("donson \|", message.content, flags = re.IGNORECASE):
            empty=1
          elif re.search("\| donson", message.content, flags = re.IGNORECASE):
            empty=1
          elif message.guild.id == 375005798914457600:
              empty=1
          elif message.guild.id== 758908682456137750:
            empty=1
          elif message.guild.id== 815669219114876968:
            empty=1
          else:
            send_message = send_message + '<@!231259532863602698>\n'
        except AttributeError:
          empty=1
        

      # swore = False
      # if re.search("fk", message.content, flags = re.IGNORECASE):
      #   if re.search("afk", message.content, flags = re.IGNORECASE):
      #     empty=1
      #   else:
      #     swore = True
      
      # if re.search("fuc", message.content, flags = re.IGNORECASE):
      #   swore = True

      # if re.search("fck", message.content, flags = re.IGNORECASE):
      #   swore = True

      # if re.search("fuk", message.content, flags = re.IGNORECASE):
      #   swore = True

      # fmessage=filtered(message.content)
      # for i in chatFilter: 
      #   if re.search(i, fmessage, flags = re.IGNORECASE):
      #     if not message.author.id in bypass_list:
      #       try:
      #         swore = True
      #       except discord.errors.NotFound:
      #         empty=1

      
      contents0=message.content.split(' ')
      contents = []
      for i in contents0:
        contents = contents + i.split('\n')
      # for word in contents:
      #   fword=filtered(word)
      #   if fword.upper() in chatFilter2:
      #     if not message.author.id in bypass_list:
      #       try:
      #         swore = True
      #       except discord.errors.NotFound:
      #         empty=1

      #   if len(fword)>0:
      #     if fword.upper() not in chatFilterexempt:
      #       if fword[0].upper()=='F':
      #         if fword[len(fword)-1].upper()=='K':
      #           if fword[len(fword)-2].upper()=='C':
      #             if not message.author.id in bypass_list:
      #               try:
      #                 swore = True
      #               except discord.errors.NotFound:
      #                 empty=1

      if message.content.upper().startswith('CONTROLZ'):
        if message.guild.id==815669219114876968:
          return
        if message.content.upper()==('CONTROLZ'):
          if str(channel.id) not in db['editedmessage'].keys():
            await channel.send('There\'s nothing to control-z!')
          else:
            em = discord.Embed(colour=0x36393F)
            if db['editedmessage'][str(channel.id)][0] == '' and db['editednew'][str(channel.id)][0] == '':
              em.add_field(name = 'At '+db['editedtime'][str(channel.id)][0]+', Edited message: '+str(db['editedauthor'][str(channel.id)][0])+' said: ', value = '**before:**\n'+invischar+'\n**after:**\n'+invischar, inline = False)
            elif db['editedmessage'][str(channel.id)][0] == '':
              em.add_field(name = 'At '+db['editedtime'][str(channel.id)][0]+', Edited message: '+str(db['editedauthor'][str(channel.id)][0])+' said: ', value = '**before:**\n'+invischar+'\n**after:**\n'+db['editednew'][str(channel.id)][0], inline = False)
            elif db['editednew'][str(channel.id)][0] == '':
              em.add_field(name = 'At '+db['editedtime'][str(channel.id)][0]+', Edited message: '+str(db['editedauthor'][str(channel.id)][0])+' said: ', value = '**before:**\n'+db['editedmessage'][str(channel.id)][0]+'\n**after:**\n'+invischar, inline = False)
            else: 
              em.add_field(name = 'At '+db['editedtime'][str(channel.id)][0]+', Edited message: '+str(db['editedauthor'][str(channel.id)][0])+' said: ', value = '**before:**\n'+db['editedmessage'][str(channel.id)][0]+'\n**after:**\n'+db['editednew'][str(channel.id)][0], inline = False)
            await channel.send(embed=em)
        else:
          if str(channel.id) not in db['editedmessage'].keys():
            await channel.send('There\'s nothing to control-z!')
          else:
            controlzmessage=message.content.upper()[9:len(message.content)]
            controlz=True
            try:
              int(controlzmessage)
            except ValueError:
              controlz = False
            if controlz==True:
              if int(controlzmessage)>snipemax or int(controlzmessage)<1:
                await channel.send('Can only controlz a number between 1 and ' + str(snipemax))
              else:
                try: 
                  em = discord.Embed(colour=0x36393F)
                  if db['editednew'][str(channel.id)][int(controlzmessage)-1] == '' and db['editedmessage'][str(channel.id)][int(controlzmessage)-1]:
                    em.add_field(name = 'At '+db['editedtime'][str(channel.id)][int(controlzmessage)-1]+', Edited message: '+str(db['editedauthor'][str(channel.id)][int(controlzmessage)-1])+' said: ', value = '**before:**\n'+invischar+'\n**after:**\n'+invischar, inline = False)
                  elif db['editednew'][str(channel.id)][int(controlzmessage)-1] == '':
                    em.add_field(name = 'At '+db['editedtime'][str(channel.id)][int(controlzmessage)-1]+', Edited message: '+str(db['editedauthor'][str(channel.id)][int(controlzmessage)-1])+' said: ', value = '**before:**\n'+db['editedmessage'][str(channel.id)][int(controlzmessage)-1]+'\n**after:**\n'+invischar, inline = False)
                  elif db['editedmessage'][str(channel.id)][int(controlzmessage)-1] == '':
                    em.add_field(name = 'At '+db['editedtime'][str(channel.id)][int(controlzmessage)-1]+', Edited message: '+str(db['editedauthor'][str(channel.id)][int(controlzmessage)-1])+' said: ', value = '**before:**\n'+invischar+'\n**after:**\n'+db['editednew'][str(channel.id)][int(controlzmessage)-1], inline = False)
                  else:
                    em.add_field(name = 'At '+db['editedtime'][str(channel.id)][int(controlzmessage)-1]+', Edited message: '+str(db['editedauthor'][str(channel.id)][int(controlzmessage)-1])+' said: ', value = '**before:**\n'+db['editedmessage'][str(channel.id)][int(controlzmessage)-1]+'\n**after:**\n'+db['editednew'][str(channel.id)][int(controlzmessage)-1], inline = False)
                  await channel.send(embed=em)
                except IndexError:
                  await channel.send('There\'s nothing to conrolz!')
                  print('here')
            else:
              await channel.send('You must controlz an integer between 1 and 25!')

      if message.content.upper().startswith('MEMESNIPE'):
        if message.guild.id==433856438604136459:
          if message.content.upper()=='MEMESNIPE':
            if memes1 not in db['deletedmessage'].keys():
              await channel.send('There\'s nothing to snipe!')
            else:
              em = discord.Embed(colour=0x36393F)
              if db['deletedmessage'][memes1][0] == '':
                em.add_field(name = 'At '+db['deletedtime'][memes1][0]+', Deleted message from ' + db['deletedtime2'][memes1][0] + ': '+str(db['deletedauthor'][memes1][0])+' said ', value = invischar, inline = False)
              else:
                deletedmessagecontents=(db['deletedmessage'][memes1][0]).split('\t')
                try:
                  if len(deletedmessagecontents[1])>0:
                    em.set_image(url="https://media.discordapp.net"+(deletedmessagecontents[1])[26:])
                except IndexError:
                  empty=0
                if deletedmessagecontents[0]=='':
                  em.add_field(name = 'At '+db['deletedtime'][memes1][0]+', Deleted message from ' + db['deletedtime2'][memes1][0] + ': '+str(db['deletedauthor'][memes1][0])+' said ', value = invischar, inline = False)
                else:
                  if len(deletedmessagecontents[0])>1024:
                    em.add_field(name = 'At '+db['deletedtime'][memes1][0]+', Deleted message from ' + db['deletedtime2'][memes1][0] + ': '+str(db['deletedauthor'][memes1][0])+' said ', value = deletedmessagecontents[0][0:1000], inline = False)
                    em.add_field(name = invischar, value = deletedmessagecontents[0][1000:], inline = False)
                  else:
                    em.add_field(name = 'At '+db['deletedtime'][memes1][0]+', Deleted message from ' + db['deletedtime2'][memes1][0] + ': '+str(db['deletedauthor'][memes1][0])+' said ', value = deletedmessagecontents[0], inline = False)
              await channel.send(embed=em)
          else:
            if memes1 not in db['deletedmessage'].keys():
              await channel.send('There\'s nothing to snipe!')
            else:
              snipemessage=message.content.upper()[9:len(message.content)]
              snipe=True
              try:
                int(snipemessage)
              except ValueError:
                snipe = False
              if snipe==True:
                if int(snipemessage)>snipemax or int(snipemessage)<1:
                  await channel.send('Can only snipe a number between 1 and ' + str(snipemax))
                else:
                  try: 
                    em = discord.Embed(colour=0x36393F)
                    if db['deletedmessage'][memes1][int(snipemessage)-1] == '':
                      em.add_field(name = 'At '+db['deletedtime'][memes1][int(snipemessage)-1]+', Deleted message from ' + db['deletedtime2'][memes1][int(snipemessage)-1] + ': '+str(db['deletedauthor'][memes1][int(snipemessage)-1])+' said: ', value = invischar, inline = False)
                    else:
                      deletedmessagecontents=(db['deletedmessage'][memes1][int(snipemessage)-1]).split('\t')
                      try:
                        if len(deletedmessagecontents[1])>0:
                          em.set_image(url="https://media.discordapp.net"+(deletedmessagecontents[1])[26:])
                      except IndexError:
                        empty=0
                      if deletedmessagecontents[0]=='':
                        em.add_field(name = 'At '+db['deletedtime'][memes1][int(snipemessage)-1]+', Deleted message from ' + db['deletedtime2'][memes1][int(snipemessage)-1] + ': '+str(db['deletedauthor'][memes1][int(snipemessage)-1])+' said: ', value = invischar, inline = False)
                      else:
                        if len(deletedmessagecontents[0])>1024:
                          em.add_field(name = 'At ' +db['deletedtime'][memes1][int(snipemessage)-1]+', Deleted message from ' + db['deletedtime2'][memes1][int(snipemessage)-1] + ': '+str(db['deletedauthor'][memes1][int(snipemessage)-1])+' said: ', value = deletedmessagecontents[0][0:1000], inline = False)
                          em.add_field(name = invischar, value = deletedmessagecontents[0][1000:], inline = False)
                        else:
                          em.add_field(name = 'At ' +db['deletedtime'][memes1][int(snipemessage)-1]+', Deleted message from ' + db['deletedtime2'][memes1][int(snipemessage)-1] + ': '+str(db['deletedauthor'][memes1][int(snipemessage)-1])+' said: ', value = deletedmessagecontents[0], inline = False)
                    await channel.send(embed=em)
                  except IndexError:
                    await channel.send('There\'s nothing to snipe!')
              else:
                await channel.send('You must snipe an integer between 1 and 25!')

      if message.content.upper().startswith('SNIPE'):
        if message.guild.id==815669219114876968:
          return
        if message.content.upper()==('SNIPE'):
          if str(channel.id) not in db['deletedmessage'].keys():
            await channel.send('There\'s nothing to snipe!')
          else:
            em = discord.Embed(colour=0x36393F)
            if db['deletedmessage'][str(channel.id)][0] == '':
              em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][0]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][0] + ': '+str(db['deletedauthor'][str(channel.id)][0])+' said ', value = invischar, inline = False)
            else:
              deletedmessagecontents=(db['deletedmessage'][str(channel.id)][0]).split('\t')
              try:
                if len(deletedmessagecontents[1])>0:
                  em.set_image(url="https://media.discordapp.net"+(deletedmessagecontents[1])[26:])
              except IndexError:
                empty=0
              if deletedmessagecontents[0]=='':
                em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][0]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][0] + ': '+str(db['deletedauthor'][str(channel.id)][0])+' said ', value = invischar, inline = False)
              else:
                if len(deletedmessagecontents[0])>1024:
                  em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][0]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][0] + ': '+str(db['deletedauthor'][str(channel.id)][0])+' said ', value = deletedmessagecontents[0][0:1000], inline = False)
                  em.add_field(name = invischar, value = deletedmessagecontents[0][1000:], inline = False)
                else:
                  em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][0]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][0] + ': '+str(db['deletedauthor'][str(channel.id)][0])+' said ', value = deletedmessagecontents[0], inline = False)
            await channel.send(embed=em)
        elif message.content.upper()=="SNIPE ALL":
          if str(channel.id) not in db['deletedmessage'].keys():
            await channel.send('There\'s nothing to snipe!')
          else:
            em = discord.Embed(colour=0x36393F)
            j=0
            for i in db['deletedmessage'][str(channel.id)]:
              if len(i)>240:
                em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][j]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][j] + ': '+str(db['deletedauthor'][str(channel.id)][j])+' said ', value = "This message is too long, please snipe it individually", inline = False)
              elif re.search("^\s*$", i):
                em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][j]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][j] + ': '+str(db['deletedauthor'][str(channel.id)][j])+' said ', value = invischar, inline = False)
              else:
                deletedmessagecontents=i.split('\t')
                try:
                  if len(deletedmessagecontents[1])>0:
                    i=deletedmessagecontents[0]+"\thttps://media.discordapp.net"+deletedmessagecontents[1][26:]
                except IndexError:
                  empty=0
                em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][j]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][j] + ': '+str(db['deletedauthor'][str(channel.id)][j])+' said ', value = i, inline = False)
              j=j+1
            await channel.send(embed=em)
        else:
          if str(channel.id) not in db['deletedmessage'].keys():
            await channel.send('There\'s nothing to snipe!')
          else:
            snipemessage=message.content.upper()[5:len(message.content)]
            snipe=True
            try:
              int(snipemessage)
            except ValueError:
              snipe = False
            if snipe==True:
              if int(snipemessage)>snipemax or int(snipemessage)<1:
                await channel.send('Can only snipe a number between 1 and ' + str(snipemax))
              else:
                try:
                  em = discord.Embed(colour=0x36393F)
                  if db['deletedmessage'][str(channel.id)][int(snipemessage)-1] == '':
                    em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][int(snipemessage)-1]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][int(snipemessage)-1] + ': '+str(db['deletedauthor'][str(channel.id)][int(snipemessage)-1])+' said: ', value = invischar, inline = False)
                  else:
                    deletedmessagecontents=(db['deletedmessage'][str(channel.id)][int(snipemessage)-1]).split('\t')
                    try:
                      if len(deletedmessagecontents[1])>0:
                        em.set_image(url="https://media.discordapp.net"+deletedmessagecontents[1][26:])
                    except IndexError:
                      empty=0
                    if deletedmessagecontents[0]=='':
                      em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][int(snipemessage)-1]+', Deleted message from' + db['deletedtime2'][str(channel.id)][int(snipemessage)-1] + ': '+str(db['deletedauthor'][str(channel.id)][int(snipemessage)-1])+' said: ', value = invischar, inline = False)
                    else:
                      if len(deletedmessagecontents[0])>1024:
                        em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][int(snipemessage)-1]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][int(snipemessage)-1] + ': '+str(db['deletedauthor'][str(channel.id)][int(snipemessage)-1])+' said: ', value = deletedmessagecontents[0][0:1000], inline = False)
                        em.add_field(name = invischar, value = deletedmessagecontents[0][1000:], inline = False)
                      else:
                        em.add_field(name = 'At '+db['deletedtime'][str(channel.id)][int(snipemessage)-1]+', Deleted message from ' + db['deletedtime2'][str(channel.id)][int(snipemessage)-1] + ': '+str(db['deletedauthor'][str(channel.id)][int(snipemessage)-1])+' said: ', value = deletedmessagecontents[0], inline = False)
                  await channel.send(embed=em)
                except IndexError:
                  await channel.send('There\'s nothing to snipe!')
            else:
              await channel.send('You must snipe an integer between 1 and 25!')

      if message.content.upper().startswith('EMBED '):
        if len(message.content)>1024:
          send_message = sendmessage + 'Embed must be shorter than 1024 characters\n'
        else:
          embedmessage=message.content[6:len(message.content)]
          em = discord.Embed(colour=0x36393F)
          em.add_field(name = 'Embed requested by '+str(message.author), value = embedmessage, inline = False)
          await channel.send(embed=em)

      if message.content.upper()==('NUMBER OF PINS'):
        await channel.send(len(await message.channel.pins()))

      spoilsearch=message.content.split("||")
      if len(spoilsearch)>2:
        spoilmessage[channel.id]=message.content
        spoilauthor[channel.id]=message.author
      
      if message.content.upper()==('SPOIL'):
        if channel.id in spoilmessage.keys():
          spoiled=[]
          for i in spoilmessage[channel.id]:
            if i=="|":
              empty=1
            else:
              spoiled.append(i)
          spoilmessage1=''.join(spoiled)
          em = discord.Embed(colour=0x36393F)
          em.add_field(name = 'Spoiled message: ', value = str(spoilauthor[channel.id])+' said \''+spoilmessage1+'\'', inline = False)
          await channel.send(embed=em)
        else:
          send_message = send_message + 'There\'s nothing to spoil!\n'

      if message.content.upper()== ('THANOS QUOTE'):
        quote=['Perfectly balanced, as all things should be.', 'You could not live with your own failure. Where did that bring you? Back to me.', 'The hardest choices require the strongest will.', 'You should\'ve gone for the head.', 'A small price to pay for salvation.', 'I\'m sorry little one.', 'Little one, it\'s a simple calculus. This universe is finite, its resources, finite. If life is left unchecked, life will cease to exist. It needs correcting. I\'m the only one who knows that. At least, I\'m the only one with the will to act on it.', 'Well, if you consider failure experience.', 'Fun isn\'t something one considers when balancing the universe. But this does put a smile on my face.', 'I hope they remember you.', 'I know what it\'s like to lose. To feel so desperately that you\'re right, yet to fail nonetheless. It\'s frightening, turns the legs to jelly. I ask you to what end? Dread it. Run from it. Destiny arrives all the same. And now it\'s here. Or should I say, I am.', 'You\'re strong... but I could snap my fingers... and you\'d all cease to exist.', 'I finally rest, and watch the sun rise on a grateful universe.', 'With all the six stones, I could simply snap my fingers, and they would all cease to exist. I call that... mercy.', 'When I\'m done, half of humanity will still exist.', 'Today I lost more than you could know, but now is no time to mourn. Now, is no time at all.', 'All that for a drop of blood.', 'Hear me and rejoice. You have had the privilege of being saved by the great Thanos. You may think this is suffering, no. It is salvation. The universal scale tips toward balance because of your sacrifice. Smile. For even in death, you have become children of Thanos.', 'You\'re strong. Me. You\'re generous. Me. But I never taught you to lie. That\'s why you\'re so bad at it.', 'This day extracts a heavy toll.', 'It was, and it was beautiful. Titan was like most planets. When we faced extinction, I offered a solution. They called me a mad man.', 'You\'re not the only one cursed with knowledge.', 'I ignored my destiny once. I cannot do that again. Even for you.', 'Your optimism is misplaced, Asgardian.', '*cries*', 'Fine, I\'ll do it myself.', 'Reality is often disappointing', 'Now, reality can be whatever I want', 'I am inevitable', 'You could not live with your own failure. Where did that bring you? Back to me.', 'I don\'t even know who you are', 'In all my years of conquest, violence, slaughter, it was never personal. But I\'ll tell you now, what I\'m about to do to your stubborn, annoying little planet... I\'m gonna enjoy it. Very, very much.', 'The universe required correction. After that, the stones served no purpose beyond temptation.', 'You should be grateful', 'Gone. Reduced to atoms.', 'Impossible.', 'I used the stones to destroy the stones.', 'The work is done. It always will be.', 'As long as there are those that remember what was, there will always be those, that are unable to accept what can be.', 'I\'m thankful. Because now I know what I must do. I will shred this universe down to it\'s last atom and then, with the stones you\'ve collected for me, create a new one. It is not what is lost but only what it is been given... a grateful universe.', 'They\'ll never know. Because you won\'t be alive to tell them.', 'Unruly wretches.', 'Rain fire!', 'I thought by eliminating half of life, the other half would thrive, but you have shown me... that\'s impossible.']
        quote1=randint(0, len(quote)-1)
        await channel.send(quote[quote1])

      if message.content.upper()==('.MEME'):
        await channel.send('Use `.meme help` for more info')
      
      if message.content.upper().startswith('.MEME '):
        mememessage=message.content[6:len(message.content)].upper()
        if mememessage=='HELP':
          await message.author.send(memelist['HELP'])
          await message.author.send(memelist['HELP2'])
        elif mememessage not in memelist.keys():
          send_message = send_message + 'That meme doesn\'t exist! Use `.meme help` for more info.\n'
        else:
          await message.delete()
          em = discord.Embed(colour=0x36393F)
          em.set_image(url=memelist[mememessage])
          await channel.send(embed=em)

      if message.content.upper()==('.TT'):
        tt_choice=randint(0,len(terms)-1)
        term=terms[tt_choice]
        embed = discord.Embed(title=term.title, tt_choicecolour=0x36393F)
        embed.add_field(name="Definition", value=term.fields[0].value)
        await channel.send(embed=embed)
      
      if message.content.upper()==('.TM'):
        if message.guild.id in [758908682456137750, 815669219114876968]:
          tt_choice=randint(0,len(terms_only2)-1)
          term=terms_only2[tt_choice]
          term_def=terms2[term]
          embed = discord.Embed(title=term, tt_choicecolour=0x36393F)
          embed.add_field(name="Definition", value=term_def)
          await channel.send(embed=embed)

      if message.content.upper().startswith('.TT '):
        if message.content.upper()==('.TT HELP'):
          await channel.send('Use `.tt <phrase>` to look up the trans term definition of that phrase.\nUse `.tt terms` to get a list of terms, and navigate through the pages using numbers, e.g. `.tt terms 2`\nUse `feedback` to suggest new terms!')
        elif message.content.upper()==('.TT TERMS'):
          max_page=math.ceil(len(terms)/20)
          embed = discord.Embed(colour = 0x36393F)
          terms_send='\n'.join(terms_only[0:20])
          embed.add_field(name= 'Trans Terms', value=terms_send)
          embed.set_footer(text='Page 1'+'/'+str(max_page))
          await channel.send(embed=embed)
        elif message.content.upper().startswith('.TT TERMS '):
          term_params=message.content.upper().split(' ')
          max_page=math.ceil(len(terms_only)/20)
          terms_pg=term_params[2]
          terms_page_int=True
          try:
            int(terms_pg)
          except ValueError:
            terms_page_int=False
            send_message = send_message + 'Must find terms on positive integer page numbers.\n'
          if terms_page_int==True:
            if int(terms_pg) < 1:
              send_message = send_message + 'Must find terms on positive integer page numbers.\n'
              terms_page_int=False
          if terms_page_int==True:
            if int(terms_pg)>max_page:
              send_message = send_message + 'Page number must be less than '+str(max_page) + '\n'
            else:
              embed=discord.Embed(colour=0x36393F)
              terms_min=int(terms_pg)*20-20
              if int(terms_pg)==max_page:
                terms_max=len(terms_only)
              else:
                terms_max=terms_min+20
              terms_send='\n'.join(terms_only[terms_min:terms_max])
              embed.add_field(name= 'Trans Terms', value=terms_send)
              embed.set_footer(text='Page '+terms_pg + '/'+ str(max_page))
              await channel.send(embed=embed)
        elif message.content.upper().startswith('.TT ADD | '):
          if message.author.id in tt_mod:
            tt_add_content=message.content.split(' | ')
            if len(tt_add_content)==3:
              embed=discord.Embed(title=tt_add_content[1], tt_choicecolour=0x36393F)
              embed.add_field(name="Definition", value=tt_add_content[2])
              transterms_channel=client.get_channel(transterms_data)
              await transterms_channel.send(embed=embed)
              await channel.send("Term added")
        elif message.content.upper().startswith('.TT "'):
          keywords=message.content[5:len(message.content)-1].upper()
          for term in terms:
            if keywords == term.title.upper():
              embed = discord.Embed(title=term.title, tt_choicecolour=0x36393F)
              field_int=0
              for field in term.fields:
                if field_int == 0:
                  embed.add_field(name="Definition", value=term.fields[0].value)
                else:
                  embed.add_field(name='\u200b',value=field.value)
                field_int=field_int+1
              await channel.send(embed=embed)
              return
          send_message = send_message + 'Could not find that term.\n'
        else:
          keywords=message.content[4:].upper()
          for term in terms:
            if keywords in term.title.upper():
              embed = discord.Embed(title=term.title, tt_choicecolour=0x36393F)
              field_int=0
              for field in term.fields:
                if field_int == 0:
                  embed.add_field(name="Definition", value=term.fields[0].value)
                else:
                  embed.add_field(name='\u200b',value=field.value)
                field_int=field_int+1
              await channel.send(embed=embed)
              return
          send_message = send_message + 'Could not find that term.\n'

      if message.content.upper().startswith('.TM '):
        if message.guild.id in [758908682456137750, 815669219114876968]:
          if message.content.upper()==('.TM HELP'):
            await channel.send('Use `.tm <phrase>` to look up the trans meme definition of that phrase.\nUse `.tm terms` to get a list of terms, and navigate through the pages using numbers, e.g. `.tm terms 2`')
          elif message.content.upper()==('.TM TERMS'):
            max_page=math.ceil(len(terms_only2)/20)
            embed = discord.Embed(colour = 0x36393F)
            terms_send='\n'.join(terms_only2[0:20])
            embed.add_field(name= 'Trans Memes', value=terms_send)
            embed.set_footer(text='Page 1'+'/'+str(max_page))
            await channel.send(embed=embed)
          elif message.content.upper().startswith('.TM TERMS '):
            term_params=message.content.upper().split(' ')
            max_page=math.ceil(len(terms_only2)/20)
            terms_pg=term_params[2]
            terms_page_int=True
            try:
              int(terms_pg)
            except ValueError:
              terms_page_int=False
              send_message = send_message + 'Must find terms on positive integer page numbers.\n'
            if terms_page_int==True:
              if int(terms_pg) < 1:
                send_message = send_message + 'Must find terms on positive integer page numbers.\n'
                terms_page_int=False
            if terms_page_int==True:
              if int(terms_pg)>max_page:
                send_message = send_message + 'Page number must be less than '+str(max_page) + '\n'
              else:
                embed=discord.Embed(colour=0x36393F)
                terms_min=int(terms_pg)*20-20
                if int(terms_pg)==max_page:
                  terms_max=len(terms_only2)
                else:
                  terms_max=terms_min+20
                terms_send='\n'.join(terms_only2[terms_min:terms_max])
                embed.add_field(name= 'Trans Memes', value=terms_send)
                embed.set_footer(text='Page '+terms_pg + '/'+ str(max_page))
                await channel.send(embed=embed)
          elif message.content.upper().startswith('.TM "'):
            keywords=message.content[5:len(message.content)-1].upper()
            for term in terms_only2:
              if keywords == term.upper():
                embed = discord.Embed(title=term, tt_choicecolour=0x36393F)
                embed.add_field(name="Definition", value=terms2[term])
                await channel.send(embed=embed)
                return
            send_message = send_message + 'Could not find that term.\n'
          else:
            keywords=message.content[4:].upper()
            for term in terms_only2:
              if keywords in term.upper():
                embed = discord.Embed(title=term, tt_choicecolour=0x36393F)
                embed.add_field(name="Definition", value=terms2[term])
                await channel.send(embed=embed)
                return
            send_message = send_message + 'Could not find that term.\n'

      if message.content.upper().startswith ('KEK '):
        if len(message.content) > 500: 
          send_message = send_message + ('You must kek something shorter!\n')
        else: 
          kekdatachannel = client.get_channel(kekdata)
          if message.content.upper().startswith('KEK ADD | '):
            if message.author.id == 242346507578114058: 
              return
            if re.search("\{mUsername\}", message.content, flags = re.IGNORECASE):
              await kekdatachannel.send(message.content[10:])
              send_message = send_message + 'Your kek message has been added\n'
            else: 
              send_message = send_message + "You must include {mUsername} in your kek message!"
          elif message.content.upper()==('KEK HELP'):
            await channel.send ('Kek someone\nUse \"kek add | `term`\" to add a term\n`{mUsername}` = the thing you are kekking\n`{authorName}` = the person sending the kek')
          else:
            kek=message.content[4:len(message.content):1]
            Username=kek
            Author='<@!'+str(message.author.id)+'>'
            #keklist = [f"{mUsername} got copystriked by Article 13!", f"{mUsername} named the new Disney+ show WandaVision", f"In a sudden turn of events, I **don't** kek {mUsername}", f"Sorry, {authorName}, I don't like kekking people", f"{authorName} Alt+F4'd {mUsername}.exe!", f"{authorName} pressed delete. It deleted {mUsername}", f"{authorName} thicc and collapses {mUsername}'s rib cage", "no u", f"{mUsername} died due to {authorName} being so stupid", f"{mUsername} died from a high salt intake", f"{mUsername} died while trying to find the city of England", f"{mUsername} died. OOF", f"{mUsername} dies due to lack of friends", f"{mUsername} is kekked by their own stupidity", f"{mUsername} is not able to be begoned. Oh, wait, no, {authorName} begones them anyway", f"{mUsername} is so dumb that they choked on oxygen", f"{mUsername} talked back to mods and got destroyed by the ban hammer", f"{mUsername} was charging their Samsung Galaxy Note 7...", f"{mUsername} was stuck to the ground with flex tape. That's a lotta damage!", f"To show the power of flex tape, {mUsername} was ripped in half!", f"Thanos snapped {mUsername} out of existence", f"{mUsername} asked {authorName} out. {authorName} said no. {mUsername}'s heart was broken.", f"{mUsername} took the 33 on a snow day. They were never found again.", f"{mUsername} took the 43 on a snow day. They were never found again.", f"{mUsername} took the 19 on a snow day. They were never found again.", f"{mUsername} took the 41 on a snow day. They were never found again.", f"{mUsername} took the 99 on a snow day. They were never found again.", f"{mUsername} took the 4 on a snow day. They were never found again.", f"{mUsername} took the 14 on a snow day. They were never found again.", f"{mUsername} took the 9 on a snow day. They were never found again.", f"{mUsername} took the 25 on a snow day. They were never found again.", f"{mUsername} took the 44 on a snow day. They were never found again.", f"{mUsername} took the 17 on a snow day. They were never found again.", f"{mUsername} took the 95 on a snow day. They were never found again.", f"{mUsername} took the 145 on a snow day. They were never found again.", f"{mUsername} took the 143 on a snow day. They were never found again.", f"{mUsername} tried to sled down Marine Drive and fell off the viewpoint.", f"{mUsername} got a life sentence in gay baby jail", f"{mUsername} dropped the soap", f"{mUsername} signed up for Gateman Econ", f"{mUsername} got earraped by Yames Ju's *fantastic* violin performance", f"{mUsername} heard Jerry Shao's singing voice", f"{mUsername} ran out of attempts on an unlimited attempts WebWork", f"{mUsername} tried to get from Forestry to Iona in 10 minutes.", f"{mUsername} played at the Winter Social.", f"{mUsername} ate rcik's cookies and died of glucose poisoning", f"{mUsername} listened to earthquek remixes for 10 hours until their ears fell off", f"{mUsername} joined the UBC Anime Club and became degen", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It backfired. Literally.", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It cost them their sanity", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It cost them their physics grade.", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It exploded.", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It damaged the wall", f"{mUsername} realized that kek means lol in league of legends", f"{mUsername} missed the personal profile deadline.", f"{mUsername} looked like {authorName}", f"{mUsername} realized that hm means yes to Donson.", f"{mUsername} did outdoor rec on a snow day. When the snow finally melted, all that was left was a tube scarf and a picture of Donson.", f"{mUsername} got a half used bottle of lube for secret santa.", f"{mUsername} realized that their crush was too young for them", f"{mUsername} joined the Daily Poll.", f"{mUsername} consumed diammonium phosphate before asking what the biscuit ingredients were.", f"{mUsername} became a singularity.", f"{mUsername} read this message and self destructed 5 seconds later.", f"{mUsername}'s name began with \"st\" and ended with \"n\" in 2018", f"{authorName} JV5'd {mUsername} in Smash Flash 2", f"{authorName} set up {mUsername} with Jerry Shao", f"{authorName} infected {mUsername} with a bad case of dissing Terry", f"{authorName} defenestrated {mUsername} off the UTP balcony.", f"{mUsername} had Town Hall.", f"{authorName} tried to hang mistletoe on the roof. {mUsername} spoke too loudly about it and they both died at Town Hall.", f"{mUsername} denied jesyu", f"{authorName} decided to sacrifice {mUsername} to the cult of Gateman", f"{mUsername} walked off the edge of the flat earth", f"Doctor Strange bargained with {mUsername}", f"{mUsername} experienced the Awaddening.", f"{mUsername} ran into the Engineering Band.", f"Snow blocked {mUsername}'s door and they missed their final exam.", f"{mUsername} bomb clipped out of this world", f"{mUsername} BLJ-ed out of this world", f"{mUsername} revealed themselves to be Hipster Pony", f"{mUsername} didn't finish the Newsletter", f"{mUsername} tried to start a Student Council.", f"{mUsername} tried to go to UBC class on December 3, 2018.", f"{mUsername} didn't finish the Cookbook by December 31. Their English mark fell with the idea.", f"{mUsername} tried to go to a 4th year law course on campus day", f"{mUsername} lived, and therefore eventually died", f"{mUsername} connected an LED directly to an Arduino.", f"{mUsername} inhaled ABS fumes from the 3D printer.", f"{mUsername} missed a ComPair deadline.", f"{authorName} slapped {mUsername} with a raw fish", f"{authorName} brought {mUsername} to the forbidden water fountain", f"{mUsername} forgot to add +C when integrating", f"{mUsername} had to do a grad speech with {authorName}.", f"{mUsername} drank from the UBC fountain. Turns out it had soap in it. Turns out the soap was fat and lye soap.", f"{mUsername} didn't tap their Compass Card.", f"{mUsername} got scared by Papa John's", f"{mUsername} played as kirby in Smash. S U C C", f"{mUsername} didn't refill their Compass Card by the new month", f"{mUsername} pulled a Kirby ditto and doublesucced. They tore the universe in half.", f"{mUsername}, I choose you! {mUsername} has fainted.", f"{mUsername} opened a glass door and smashed it against a fire extinguisher.", f"{mUsername} didn't press f and pay respects.", f"{mUsername} didn't trust the Natural Recursion.", f"{mUsername} trusted the generative recursion.", f"{mUsername} didn't comment out the stub.", f"{mUsername} ran out of memory.", f"{mUsername} tried to download RAM from the internet.", f"{mUsername} thought the Yearbook was good.", f"{mUsername} joined Newsletter.", f"{mUsername} forgot their speech lines in Taiwan.", f"{mUsername} thought saying no u all the time was a good idea. (no u)", f"{authorName} hid {mUsername}'s backpack.", f"{mUsername} climbed through the ELI window.", f"{mUsername} forgot to feed the Gateman. Always feed the Gateman.", f"{mUsername} joined ballet.", f"{mUsername} used Canada Post during the strike.", f"{mUsername} plugged power into ground.", f"{mUsername} jumped across the tracks at Commercial-Broadway.", f"{mUsername} joined MAGIC COW", f"{mUsername} questioned the Smart Wise Man", f"{mUsername} wrote a story about their crush. Their crush found out and now {mUsername} is saeyad.", f"{mUsername} took a Sheardown test", f"{mUsername} engaged in social interaction", f"{mUsername} tried to win the Darwin awards. {mUsername} succeeded.", f"{mUsername} stayed at school until 10 pm", f"{mUsername} was a large potato", f"{mUsername} lost the game. {authorName} did too.", f"{authorName} found out {mUsername} was a bot. {mUsername} made sure {authorName} was never seen again.", f"{mUsername} died of `@everyone`", f"{mUsername} got scronched by Shep", f"{mUsername} opened the microwave door before the timer ended.", f"{mUsername} put their food in the microwave before realizing that the bottom was coated with Wony Lee's sticky maple syrup", f"{mUsername} was pinged", f"{mUsername} watched Alex jump off the second floor due to Peiyan's puns", f"{mUsername} broke the UTP stairs.", f"{mUsername} jumped off the balcony", f"{mUsername} microwaved a styrofoam cup and made steamed hams.", f"{mUsername} dropped their marshmallow into the sand.", f"{mUsername} got 4% on their test", f"{mUsername} became a meme.", f"{mUsername} joined Chem 121 and wasn't good at labs", f"{mUsername} fell in love with {authorName}", f"{mUsername} joined MUN and got woken up by the fire alarm at 1am", f"{mUsername} joined DEBATE and didn't like talking", f"{mUsername} joined robotics and never came back", f"{mUsername} was too short", f"{mUsername} was too tall", f"{mUsername} got a piece of paper stuck in a test tube in an attempt to clean it and later got scronched by Wilkie", f"{mUsername} became Gandalf, held up the weird pole from the ELI, and let nobody pass.", f"{mUsername} was a res student and got trolled by false fire alarms", f"{mUsername} died during a final", f"{mUsername} did the Hydrogen Balloon experiment and failed.", f"{mUsername} didn't delete this!", f"{mUsername} heard the Year Ones walking in the halls", f"{mUsername} was rickrolled", f"{mUsername} was rcikrolled", f"{mUsername} clicked on this link: https://www.youtube.com/watch?v=dQw4w9WgXcQ", f"{mUsername} tried to pirate a movie about pirates but it didn't work", f"{mUsername} tried to play ping pong at BCIT", f"{mUsername} got spam called during an exam", f"{mUsername} sent a future email to themselves", f"{mUsername} didn't go to the 2020 Reunion and got tracked down by Daria", f"{mUsername} tasted the rainbow, then fell to their death", f"{mUsername} is too hot for their own good", f"{mUsername} was nominated as the sexiest person alive. {mUsername} was killed by {authorName}, who had to defend their title.", f"{mUsername} traversed the UBC fountain with a robot when it was frozen solid...or was it?", f"{mUsername} sank when walking on a frozen fountain", f"{mUsername} made a speech with Jean at grad", f"{mUsername} said ibac (and therefore is bad)", f"{mUsername} used this command and got triggered at the answers", f"{mUsername} died of death", f"{mUsername} consumed dihydrogen monoxide and will die", f"{mUsername} missed a pair of dots on a Lewis Dot Diagram", f"{mUsername} ..", f"{mUsername} didn't realize that they were being watched.", f"{mUsername} fell for Donson and lost their mind chasing them for years and years.", f"{mUsername} turned into a box", f"{mUsername} became the pentagrove.", f"{mUsername} missed the last bus out of UBC.", f"{mUsername} got the mind stone ripped out of their head", f"{mUsername} was sacrificed for the soul stone", f"{mUsername} didn't see that coming", f"{mUsername} became a part of Kieran's story", f"{mUsername} got rekt when Daria read a story that they were written into", f"{mUsername} floats in air", f"{mUsername} tried to flex tape a boat and use it. They found the Titanic instead.", f"{mUsername} tried using flex tape on their grades.", f"{mUsername} thought ships involved actual boats and ran out of money.", f"{mUsername} noticed it said gullible on the ceiling.", f"{mUsername} noticed that cephalized is an anagram of gullible", f"{mUsername} existed and memers saw free real estate.", f"{mUsername}: GENERAL KENOBI", f"{mUsername} watched the prequels nonstop and died of cringe", f"{mUsername}: YODA", f"{mUsername} didn't realize Vader was Luke's father and died when they found out. Oops I spoiled it for {authorName}. {authorName} died too.", f"{mUsername} was a scam", f"{mUsername} didn't go for the head", f"{mUsername} pulled an all-nighter before an exam and fell asleep during the exam.", f"{mUsername} fell asleep on the bus before getting to UBC and woke up back at their house.", f"{mUsername} tapped their wallet", f"{mUsername} didn't thank the bus driver", f"{mUsername} didn't thank the skytrain driver", f"{mUsername} entered through the back door", f"{mUsername} didn't pay attention to SETH.", f"{mUsername} didn't listen to A TIP TO MAKE YOUR TRANSIT RIDE EVEN MORE AWESOME.", f"{mUsername} didn't-HEY VANCOUVER, IT'S SETH. HERE'S A TIP TO MAKE YOUR TRANSIT RIDE EVEN MORE AWESOME. KEEP IT MOVING TO THE BACK OF THE BUS. A LOT OF NEAT STUFF HAPPENING BACK THERE. THAT'S WHERE ALL THE COOL KIDS HANG OUT ANYWAY. YOU'RE MISSING OUT. THANK YOU", f"{mUsername} didn't KEEP IT MOVING TO THE BACK OF THE BUS.", f"{mUsername} didn't realize that A LOT OF NEAT STUFF HAPPENS BACK THERE in the bus.", f"{mUsername} cannot tie their shoe.", f"{mUsername}'s tie was tied by Jean and died of love ", f"{mUsername} consumed some diammonium phosphate", f"{mUsername} didn't realize THAT'S WHERE ALL THE COOL KIDS HANG OUT.", f"{mUsername} was MISSING OUT.", f"{mUsername} found the soul stone. It ripped out their soul.", f"{mUsername} found the mind stone. It made their mind insane.", f"{mUsername} found the time stone. It turned them into a 2 year old.", f"{mUsername} found the space stone. It transported them to the edge of the universe.", f"{mUsername} found the reality stone. It created a reality where they didn\'t exist.", f"{mUsername} found the power stone. They touched it.", f"{mUsername} gave up the time stone", f"{mUsername} realized that now is no time to mourn, now is no time at all", f"{mUsername} didn't have the strongest wills", f"{mUsername} called Thanos a madman", f"{mUsername} didn't go right when Star Lord told them to", f"{mUsername} punched Thanos in the face when the infinity gauntlet was almost off Thanos", f"{mUsername} was hit by Cupid's arrow", f"{mUsername} broke the law of gravity and was sentenced to a year in jail", f"{mUsername} stood under the mistletoe ", f"{mUsername} found the corner outside trans where there's an old barbecue and random trash", f"{mUsername} found the person who lived under the UTP building", f"{mUsername} is an anti-vaxxer", f"{mUsername} broke the internet.", f"{mUsername} used a dead meme", f"{mUsername} forgot to turn off interyear hangouts notifications", f"{mUsername} walked into the UTP office", f"{mUsername} tried to peel soap", f"{mUsername}: I am Groot", f"{mUsername}.", f"{mUsername} procrastinated on their annotations", f"{mUsername} failed to read the book for English", f"{mUsername} GOT SCAMMED INTO WALKING TO THE BOOKSTORE TWICE FOR AN SD CARD", f"{mUsername} became unbalanced, as all things shouldn't be", f"{mUsername} spoiled Infinity War", f"{mUsername} is obsessed with Infinity War and won't stop talking about it", f"{mUsername} leaked the trailer for Avengers 4", f"{mUsername} spoiled Avengers 4", f"{mUsername} couldn't watch the Avengers 4 trailer", f"{mUsername} put sugar on a bass speaker", f"{mUsername} walked into history drinking apple juice from a ziploc bag", f"{mUsername} didn't leave before thank yous at soup day", f"{mUsername} put duct tape on the UTP walls and left them for 3 weeks", f"{mUsername} became unwise", f"{mUsername} didn't do their homework", f"{mUsername} rebooted the clone wars", f"{mUsername} moved all the Disney stuff on Netflix to Disney+", f"{mUsername} created Disney+", f"{mUsername} rebooted Spiderman", f"{mUsername} rebooted Spiderman again", f"{mUsername} rebooted Spiderman yet another time", f"{mUsername} created the Emoji Movie", f"{mUsername} didn't soundproof the ELI", f"{mUsername} can't run", f"{mUsername} didn't call UNO", f"{mUsername} forgot to change the sign", f"{mUsername} walked up the stairs 2 at a time", f"{mUsername} died. Kowalski, analysis.", f"Doctor Strange: Let me guess, your life?\n{mUsername}: It was, and it was beautiful", f"{mUsername} dressed up as an iClicker for halloween and tried to sit down in class", f"{mUsername} and {authorName} have a snowball fight. {mUsername} got snowed to death.", f"{mUsername} found the aurora borealis, at this time of year, at this time of day, in this part of the country, localized entirely within their kitchen", f"{mUsername} made steamed hams and steamed themselves in the process", f"{mUsername} was thrown off the face of the Earth", f"{mUsername} doesn't feel so good...", f"{mUsername} is in the endgame now", f"{mUsername} knew there was no other way", f"{mUsername} was a flat earther", f"{mUsername} didn't get the time stone back", f"{mUsername} used this statement when it was already used somewhere else. They got nerfed by {authorName}.", f"{mUsername} made a bad joke", f"{mUsername} broke through one of the walls at UTP", f"{mUsername} didn't realize that THIS IS AN OFFICE SPACE", f"{mUsername} made a bad pun", f"{mUsername} divided by zero, and the math gods banished them from existence", f"{mUsername} drilled to the centre of the Earth.", f"{mUsername} said 2 + 2 = 4", f"{mUsername} said 2 + 2 = 5", f"{mUsername} tried to drink water with a spoon", f"{mUsername} tried to drink water with a plastic bag", f"{mUsername} tried to drink water with chopsticks", f"{mUsername} tried to drink water with a fork", f"{mUsername} used locker 11.", f"{mUsername} video called Bamfield when the receiving phone was finessed by Donson.", f"{mUsername} used a paper straw.", f"{mUsername} forgot Newton's Third Law.", f"{mUsername} didn't wear formal clothes at grad.", f"{mUsername} clapped before all the students were announced.", f"{mUsername} joined the PCMASTERRACE", f"{mUsername} joined the MACSTERRACE", f"{mUsername} joined the PCMACSTERRACE", f"{mUsername} tried to understand anything on a UTP discord", f"{mUsername} thought a time was PM instead of AM", f"{mUsername} didn't know it was time to stop.", f"{mUsername} :thinking:ed too hard.", f"{mUsername}.exe has stopped working", f"{mUsername} encountered shrek", f"{mUsername} didn't turn off the lights in the ELI", f"{mUsername} was the cause of the fact that A GUIDEWAY INTRUSION HAS BEEN DETECTED AT THIS STATION. IF YOU HAVE TRESPASSED ONTO THE GUIDEWAY, YOU ARE IN DANGER AND MUST RETURN TO THE PLATFORM IMMEDIATELY. YOU ARE BEING RECORDED ON CCTV.", f"{mUsername} fed a seagull. They disappeared in seconds.", f"{mUsername} went to school on a snow day.", f"{mUsername} tried to paint the engineering cairn.", f"{mUsername} went to an ECON 101 tutorial. Nobody else was there.", f"{mUsername} got kekked by life.", f"{mUsername} didn't wash the ice cream bucket properly.", f"{mUsername} had no life", f"{mUsername} had too many lives", f"{mUsername} had no friends", f"{mUsername} tried to find the meaning of life and found 42 instead.", f"{authorName} was one of the 5 people {mUsername} met in heaven.", f"{mUsername} 3d printed a kek and was kekked by yems", f"{mUsername} supported Communism", f"{mUsername} spilled 12M H2SO4 on themselves.", f"{mUsername} didn't know how to use a 25.00ml volumetric pipet.", f"{mUsername} overshot the volumetric flask", f"{mUsername} overshot the equivalence point", f"{mUsername} screwed up the lab quiz", f"{mUsername}'s data was too far off", f"{mUsername} screwed up. Who's up?", f"{mUsername} built the grad slideshow and got memed in their own creation", f"{mUsername} misplayed the Windows XP startup at grad.", f"{mUsername} transfailed.", f"{mUsername} tried to use the hallway chalkboards and their work got memed instead", f"{mUsername} failed a UTP calc quiz", f"{mUsername} watched a Jeffrey Grossman lecture", f"{mUsername} didn't agree with Gladwell", f"{mUsername} watched a Jerry Shao video", f"{mUsername} watched a DONSON DONG video", f"{mUsername} watched a W O N Y L E E video", f"{mUsername} fell asleep during Town Hall", f"{mUsername} gamed at UTP", f"{mUsername} found a picture of themselves on the RPL Facebook Page", f"{mUsername} photoshipped and was caught", f"{mUsername} died", f"{mUsername} tried to get people to go to the Maker Expo setup day without realizing it was a scam. They were never the same again.", f"{mUsername} went to the Maker Expo setup day.", f"{mUsername} listened to Daria's speech", f"{authorName} existed, so {mUsername} died", f"{mUsername} tried to present at the Maker Expo.", f"{mUsername} didn't know de way.", f"{mUsername} and {authorName} swapped lives without knowing how to swap back.", f"{mUsername} got stuck in a time loop", f"{mUsername} got stuck in a time vortex", f"{mUsername} got stuck in the mirror dimension", f"{mUsername} got stuck in the Quantum Realm", f"{mUsername} shrank for all eternity", f"{mUsername} didn't tie their shoes during rec", f"{mUsername} encountered a wild Donphan", f"{mUsername}. is. sparta.", f"{mUsername} tried to find the Avengers 4 trailer.", f"{mUsername} didn't remember the 21st night of September", f"{mUsername} didn't bring food for their club", f"{mUsername} didn't double space after typing a period.", f"{mUsername} had a good question, but they didn't have a good answer.", f"{mUsername} didn't cite all their sources", f"{mUsername} rode the Thanoscar", f"{mUsername} snoozed their alarm", f"{mUsername} differentiated with respect to x instead of t", f"{mUsername} lost their UBCcard", f"{mUsername} tried to use the tables at Wesbrook 100", f"{mUsername} pushed the door between ICCS X wing and ICCS main wing. The fire alarms destroyed their ears", f"{mUsername} didn't type one of kek, rip or lol in kekriplol", f"{mUsername} tried to (make-gregor \"Gregor Kiczales\" 1994)", f"{mUsername} `@everyone` and was stoned by an angry mob consisting of Ivan and Louis", f"{mUsername} tried to climb a tree. They fell.", f"{mUsername} existed on December 32, 2018.", f"{mUsername} was born tomorrow", f"{mUsername} didn't change their clocks when daylight savings time ended", f"{mUsername} forgot to study for their final", f"{mUsername} asked a question and got \"no u\" for an answer", f"{mUsername} sat on their iPad Pro with $169 stylus", f"{mUsername} bolded their name on their chem lab.", f"{mUsername} invested in Wony's cryptomoney, chodecoin. It got too thicc and crashed", f"{mUsername} thought mining Bitcoin on their home computer was a good idea", f"{mUsername} jumped in a pile of leaves. Unfortunately, that pile of leaves was over an open sewer pipe.", f"{mUsername} tried to dig in their backyard, hoping they would mine some bitcoin. Instead they got dirt.", f"{mUsername} tried to take the 480 on a Sunday", f"{mUsername} ate snowflakes only to realize they were solidified acid rain molecules", f"{mUsername} tried to use a water hose to remove snow on a cold day", f"{mUsername} didn't hold up a mirror to no u", f"{mUsername} was bad at rec and got their report card back", f"{mUsername} thought Derek was Donson", f"{mUsername} thought Donson was Derek", f"{mUsername} didn't get the alternate meaning of a poem in english", f"{mUsername} lost the sun. Where's the sun? Nobody knows. Except maybe the Beatles.", f"{mUsername} looked at the sun.", f"{mUsername} caught a battery while fishing", f"{mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername}", "Hmm...nah.", "Nah tl.", "Tl.", f"{mUsername} thought a sine wave was a cubic function", f"{mUsername} built a rollercoaster. They weren't able to feel anything after that.", f"{mUsername} decided not to wear safety glasses to a robotics competition and got hit in the face with a beam.", f"{mUsername} didn't get gud.", f"{mUsername} played badminton at Osborne Gym. The birdie got stuck on the second floor.", f"{authorName} gave {mUsername} a piece of paper that said No U on it. {mUsername} was nou'd into oblivion.", f"{authorName} gave diammonium phosphate cookies to {mUsername}.", f"{mUsername} didn't lock their locker at UTP. When they came back after an hour, everything including the locker door was gone.", f"{authorName} threw a frisbee at {mUsername}.", f"{authorName} tried to throw {mUsername} off the UBC viewpoint. {authorName} lost their balance and they both fell.", f"{mUsername} threw a chair at the ELI wall and got roasted for being too loud.", f"{mUsername} tried to find the secret UTP server room.", f"{mUsername} ate the forbidden fruit of Tide.", f"{mUsername} plugged a power bar into itself and tried to get infinite energy.", f"{mUsername} cranked the volume up to 11.", f"{mUsername} gained too high of an IQ and the signed integer holding the IQ value underflowed to a negative number.", f"{mUsername} found the real live version of the Dr. Racket cat. It natural recursed itself into infinity, consuming everything around it, including {mUsername}.", f"{mUsername} heard Thomas Kroeker speak", f"{mUsername} deleted their essay after submitting it online. It turns out they submitted the rubric instead.", f"{mUsername}'s computer was encrypted and all their files were locked.", f"{mUsername} tried to make a UTP confessions page.", f"{mUsername} was teleported to a timeline in which they didn't exist", f"{mUsername} shot themselves in the foot. Literally", f"{mUsername} stapled themselves", f"{authorName} destroyed {mUsername}'s sanity with never-ending talking", f"{mUsername} went down, but they took {authorName} with them", f"{mUsername} reflected the nerfing beam and {authorName} got kekked instead.", f"{mUsername} faked being kekked and resurfaced later", f"{mUsername} touched a lightbulb", f"{mUsername} was kekked by Saf for breaking into an ELI", f"{mUsername} did nothing wrong. They got kekked anyway.", f"{mUsername} thought the erasable whiteboard markers were erasable. They thought wrong.", f"{mUsername} became a thot and was promptly begoned.", f"{mUsername}'s mind was erased. Begone, thought!", f"{mUsername}'s mind was blown. None of it remained.", f"{mUsername} tried to fold 1000 paper cranes", f"{mUsername} attempted to put a decoration on top of a christmas tree, but fell and was crushed by the tree", f"{mUsername} car, {mUsername} car", f"{mUsername} tried to do a generative recursion in their mind with no termination argument.", f"{mUsername} tried to find out who the Anonymous Platypus is", f"{mUsername} tried to add alts to a discord server and got nerfed by the owner", f"{mUsername} became a chode", f"{mUsername} tried to slide into {authorName}'s DMs", f"{mUsername} was rejected by {authorName} on Valentines Day. REJECTED! REJECTED! {mUsername} got REJECTED! R-E, J-E, C-T-E-D, REJECTED!", f"{mUsername} 3D printed a donut.", f"{mUsername} was too obese", f"{mUsername} died in a tornado", f"{mUsername} attempted to run Project Euler on a home laptop", f"{mUsername} attempted to run C(7) on their home laptop", f"That's a thicc idea. How bout no.", f"{mUsername} found themselves on the surface of the sun.", f"{authorName} thought {mUsername} was a pokemon and tried to put them in a pokeball", f"{mUsername} set fire to their hair", f"{mUsername} poked a stick at a grizzly bear", f"{mUsername} ate medicine that was out of date", f"{mUsername} used their private parts as piranha bait", f"{mUsername} got their toast out with a fork", f"{mUsername} did their own electrical work", f"{mUsername} taught themselves how to fly", f"{mUsername} ate a two week old unrefrigerated pie", f"{mUsername} invited a psycho killer inside", f"{mUsername} scratched a drug dealer’s brand new ride", f"{mUsername} took their helmet off in outer space", f"{mUsername} used a clothes dryer as a hiding place", f"{mUsername} kept a rattlesnake as a pet", f"{mUsername} sold both their kidneys on the internet", f"{mUsername} ate a tube of superglue", f"{mUsername} wondered what the red button did.", f"{mUsername} dressed up like a moose during hunting season", f"{mUsername} disturbed a nest of wasps for no good reason", f"{mUsername} stood on the edge of a train station platform", f"{mUsername} drove around the boom gates at a level crossing", f"{mUsername} ran across the tracks between the platforms", f"Such {mUsername}. Much person. Many owaow. Very kekked now.", f"{mUsername} realized that oops! This command is on cooldown right now. Please wait **0.00000000000069** seconds before trying again.", f"{mUsername} tried to use the UTP grad lounge printer. They were nerfed by grads.", f"{mUsername} gambled away their life savings", f"{mUsername} didn’t wear a lab coat in the lab", f"{mUsername} got lost in Europe", f"{mUsername} found asbestos in the UTP walls", f"{mUsername} dropped Francium in the fishtank"]
            kek1=randint(0,len(keklist)-1)
            newkekmessage=keklist[kek1].content.format(mUsername=Username,authorName=Author)
            send_message = send_message + newkekmessage + '\n'
      
      if client.get_user(467016289878147073) in message.mentions:
        if not message.content.upper().startswith("QUOTE"):
          send_message = send_message + 'Yes?\n'

      if channel.id in banchannel:
        empty=1
      else:
        if message.content.upper()==('I NEED HELP'):
          # removed commands: \n**hi**\nhello\n**bye**\ngoodbye\n**..**\ntry it\n**no u, nou, no you, no w, no yu, neu**\nnou\n**u, you, ur, you, you\'re**\nmessages that start with the above\n**hm**\nyes indeed\n**scam**\nscam indeed\n**ping, bing**\npings everone in the server\n**friend**\nwhat friends?\n**life**\nwhat life?\n**balance, balanced**\nperfectly balanced, as all things should be\n**hypocrite, black panther**\nthe biggest hypocrite of them all\n**slow**\nToo slow\n**sad**\nThis is so sad\n**doubt**\npress x to doubt\n**doing**\nwhat are you doing?\n**strange**\nThe name\'s Strange, Doctor Strange\n**Martha**\nWHY DID U SAY THAT NAME\n**AAAAA**\naaaaa song\n**remember**\nI hope they remember you\n**sorry, cry, sacrifice, rip**\nI\'m sorry little one.\n**rejected**\nyou just got rejected\n**I\'m**\nPlease state your name\n**Thanos did nothing wrong**\nBecause it\'s true\n**noot**\nnoot noot\n**x**\npress x to doubt\n**trigger**\npings someone in the server randomly\n
          await message.author.send('**THANOS**\n__**LIST OF COMMANDS**__:\n**thanks**\nFor all your thankfulness on Thanksgiving\n**8ball**\nThe most reliable 8ball\n**Thanos quote**\nsends a Thanos quote\n**thanks thanos**\nthank thanos bot\n**snap**\nThanos did nothing wrong\n**Ping Thanos**\nTo mention our great lord and savior\n**choose**\nchoose from a list, split the choices with \"|\"\n**time**\nsends the current time PST\n**hunger games**\nhunger games on whoever you pick, split the choices with \"|\"\n**pong start**\nplay a game of pong\n**poll**\ncreates a poll with up to 20 options, split by \'|\'\n**rate**\nrate something\n**australia**\nsends you message upside down\n**backwards**\nsends your message backwards\n**spacify**\nadd spaces between all characters of your message\n**invisify**\nadd invisible characters between all the characters of your message\n**morse code**\ncode a message in morse\n**morse decode**\ndecode a morse code message\n**dumthanos**\nwhen thanosbot is being dumb\n**banlist**\nshows list of banned people\n**Grades**\ngrades flowchart game\n**kek**\nkek someone\n**.meme**\nsends memes, use .meme help for more info\n**.tt**\nsearch up terms in the trans terms dictionary\n**number of pins**\nshows the number of pins in the channel, max is 50\n**quote**\nquotes someone\n**hook**\nsends a hook with the message content, name, and avatar; use hook help for more information\n**i need help**\nsends list of help commands\n__**MOD ONLY**__\n**say**\nmakes the bot say something\n**stopthanos**\nstops the bot if it\'s being dumb\n**ban/unban**\nbans or unbans user from using the bot\n__**Other uses:**__\nDeleted message logger\nSniper\nControl-z\nSpoiler\nText embedder\nChannel id retriever\nUser id retriever\nServer id retriever\nPurger\nMound of Dirt\nIncognito\nFeedback receiver\n*use \'special commands\' for more info on commands*\n-------------------------------------')

        if message.content.upper()==('SPECIAL COMMANDS'):
          await message.author.send('**Sniper**\nuse \'snipe\' to see the previous deleted messages\n**Control-z**\nuse \'controlz\' to see the previous edited messages\n**Spoil**\nspoils the previous spoiler marked message\n**Text embedder**\nuse \'embed\' to embed text\n**Channel id retriever**\nuse \'channel id\' to retrieve the channel id\n**User id retriever**\nuse \'user id\' to retrieve someone\'s user id\n**Server id retriever**\nuse \'server id\' to retrieve the server id\n**Purger**\nuse \'purge\' to purge x amount of messages in the channel\n**Mound of Dirt**\nStops all messages from being sent in the channel\n**Incognito**\nDeletes all messages in channel 30 seconds after it is sent\n**Feedback receiver**\nuse \'feedback\' to give feedback to the bot\n-------------------------------------')

        #if message.author.id==donsonid:
         # if message.content.upper()==('LINESPAM'):
          #  while True:
           #   await channel.send('***ٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴ***')
              #await asyncio.sleep(1)

        # if message.content.upper().startswith('NO U'):
        #   send_message = send_message + 'no u\n'

        # if message.content.upper().startswith('NEU'):
        #   send_message = send_message + 'no u\n'

        # if message.content.upper().startswith('NO YU'):
        #   send_message = send_message + 'Yes, James Yu\n'

        # if message.content.upper().startswith('NO YOU'):
        #   send_message = send_message + 'no u\n'
      
        # if message.content.upper().startswith('NOU'):
        #   send_message = send_message + 'no u\n'

        # if message.content.upper() == ('NO W'):
        #   send_message = send_message + 'no w\n'

        # if message.content.upper().startswith('.. '):
        #   send_message = send_message + 'no, it\'s ...\n'

        # if message.content.upper() == ('..'):
        #   await channel.send('no, it\'s ...')
      
        # if message.content.upper().startswith('U '):
        #   send_message = send_message + 'no u\n'
      
        # if message.content.upper().startswith('YOU '):
        #   send_message = send_message + 'no u\n'

        # if message.content.upper().startswith('YOUR '):
        #   send_message = send_message + 'no u\n'
      
        # if message.content.upper().startswith('YOU\'RE '):
        #   send_message = send_message + 'no u\n'
      
        # if message.content.upper().startswith('UR '):
        #   send_message = send_message + 'no u\n'
          
        # if message.content.upper().startswith('HM'):
        #   send_message = send_message + 'yes indeed\n'
          
        # if message.content==('.'):
        #   await channel.send('x2')

        # if message.content.upper() == ('PING'):
        #   await channel.send('@everyone')

        # if message.content.upper() == ('BING'):
        #   await channel.send('@everyone')

        # if message.content.upper() == ('🅱️ING'):
        #   await channel.send('@everyone')

        # if message.content.upper() == ('X'):
        #   await channel.send('Doubted')

        if message.content.upper() == ('?GARFIELD JESYU'):
          em = discord.Embed(title='2018-05-26', colour=0x36393F)
          em.set_image(url='https://media.discordapp.net/attachments/512138730182672386/667979283439812608/2018-05-26.gif?width=400&height=119')
          await channel.send(embed=em)

        # if message.content.upper().startswith ('I\'M '):
        #   im=message.content[4:len(message.content):1]
        #   thanoschoice=randint(0, 1)
        #   if len(im)>1900:
        #     empty=1
        #   elif thanoschoice==0:
        #     send_message = send_message + 'Hi '+im+', I\'m Thanos\n'
        #   else:
        #     send_message = send_message + 'Hi '+im+', I\'m inevitable\n'

        # if message.content.upper().startswith ('IM '):
        #   im=message.content[3:len(message.content):1]
        #   thanoschoice=randint(0, 1)
        #   if len(im)>1900:
        #     empty=1
        #   elif thanoschoice==0:
        #     send_message = send_message + 'Hi '+im+', I\'m Thanos\n'
        #   else:
        #     send_message = send_message + 'Hi '+im+', I\'m inevitable\n'

        # if message.content.upper().startswith ('I AM '):
        #   im=message.content[5:len(message.content):1]
        #   thanoschoice=randint(0, 1)
        #   if len(im)>1900:
        #     empty=1
        #   elif thanoschoice==0:
        #     send_message = send_message + 'Hi '+im+', I\'m Thanos\n'
        #   else:
        #     send_message = send_message + 'Hi '+im+', I\'m inevitable\n'

        if message.content.upper().startswith ('RATE '):
          # if message.content.upper()=='RATE JESYU':
          #   await channel.send('Thanos rates '+message.content[5:len(message.content):1]+ ' a 100/100')
          if len(message.content.upper())>505:
            send_message = send_message + 'You must rate something with less than 500 characters!\n'
          else:
            ratemessage=message.content.upper()[5:len(message.content):1]
            ratenumber=0
            n=1
            for i in ratemessage:
              if i in rate.keys():
                ratenumber=ratenumber+rate[i]*n
                n=n+1
              else: 
                ratenumber=ratenumber+69/n
                n=n+1
            ratenumber=int(ratenumber%101)
            send_message = send_message + 'Thanos rates ' + message.content[5:len(message.content):1]+ ' a ' + str(ratenumber) + '/100\n'

        if message.content.upper() == ('THANKS THANOS'):
          await channel.send('You\'re welcome, little one')

        if message.content.upper() == ('THANK YOU THANOS'):
          await channel.send('You\'re welcome, little one')

        if message.content.startswith ('8ball'):
          send_message = send_message + 'Yes, definitely\n'

        if message.content.upper() == ('PONG START'):
          if str(channel).upper().startswith('DIRECT MESSAGE WITH'):
            return
          if channel.id in pong:
            empty=1
          else:
            pong_message = await channel.send('Get ready, pong is about to start! Send `1` to move left and `2` to move right.') # Send `exit` if you wish to leave.
            await asyncio.sleep(0.3)
            pong_channels.append(channel.id)
            pong[channel.id]=[randint(0,89),94,95,1,message.author.id]#ball,p1,p2,direction
            gamemode[channel.id]=message.author.id
            await asyncio.sleep(5)
            try:
              await pong_message.edit(content=render_pong(pong[channel.id]))
              #client.loop.create_task(pong_run(channel.id,channel,pong_message))
              pong_game=True
            except discord.errors.NotFound:
              del gamemode[channel.id]
              pong_channels.remove(channel.id)
              del pong[channel.id]
              pong_game=False
            except IndexError:
              del gamemode[channel.id]
              pong_channels.remove(channel.id)
              del pong[channel.id]
              pong_game=False
            while pong_game==True:
              try:
                if pong[channel.id][3]==5:
                  del gamemode[channel.id]
                  pong_channels.remove(channel.id)
                  del pong[channel.id]
                  await channel.send('You lost!')
                  pong_game=False
                else:
                  try: 
                    pong[channel.id]=update_pong(pong[channel.id])
                    pong[channel.id]=update_pong(pong[channel.id])
                    await pong_message.edit(content=render_pong(pong[channel.id]))
                    await asyncio.sleep(1)
                  except discord.errors.NotFound:
                    pong_game=False
                    del gamemode[channel.id]
                    pong_channels.remove(channel.id)
                    del pong[channel.id]
              except KeyError:
                empty=1
        
        if message.content.upper().startswith ('HUNGER GAMES'):
          if channel.id in hungergames:
            send_message = send_message + 'there is already a game going on!\n'
          else:
            hungergames.append(channel.id)
            if message.content.upper()=='HUNGER GAMES':
              try:
                if message.guild.id in [758908682456137750, 815669219114876968]:
                  peoples="Jonathan | Michael | Kevin | Cora | Shaana | Raymond | Emily | Ayan | Alice | Nora | James | Noah | Sarah | Arran | David | Anna | Vanessa | Sheena | Elliott | Jocelyn | Vivian"
                else:
                  peoples='Aiza | Alex | Alyona | Amy | Caitlin | Eddie | Edward | Elwin | Emily | Floria | Jerry | Jonathan | Katherine | Min | Natalie | Nicole | Noreen | Peiyan | Ricky | Shawn Yee | Amanda | Baapooh | Donson | Daniel | Fannia | Felicia | Grady | Ivan | James | Jean | Jessie | Joey | Johnny | Kieran | Louis | Ray | Sherman | Shawn Lu | Sophia | Veronica | William | Wilson | Wony'
              except AttributeError:
                peoples='Aiza | Alex | Alyona | Amy | Caitlin | Eddie | Edward | Elwin | Emily | Floria | Jerry | Jonathan | Katherine | Min | Natalie | Nicole | Noreen | Peiyan | Ricky | Shawn Yee | Amanda | Baapooh | Donson | Daniel | Fannia | Felicia | Grady | Ivan | James | Jean | Jessie | Joey | Johnny | Kieran | Louis | Ray | Sherman | Shawn Lu | Sophia | Veronica | William | Wilson | Wony'
            else:
              peoples=message.content[13:]
            persons=peoples.split(' | ')
            people=[]
            for i in persons:
              people.append(i)
            while len(people)>1: 
              send_message5 = ''
              choice=randint(0, len(people)-1)
              person=people[choice]
              people.remove(person)
              mUsername=person
              authorName=people[randint(0, len(people)-1)]
              keklist0=[f"In a sudden turn of events, I **don't** kek {mUsername}", f"Sorry, {authorName}, I don't like kekking people", f"{mUsername} faked being kekked and resurfaced later", f"That's a thicc idea. How bout no.", "Hmm...nah.", "Nah tl.", "Tl.", "no u"]
              keklist2=[f"{authorName} tried to hang mistletoe on the roof. {mUsername} spoke too loudly about it and they both died at Town Hall.", f"{mUsername} lost the game. {authorName} did too.", f"{mUsername} didn't realize Vader was Luke's father and died when they found out. Oops I spoiled it for {authorName}. {authorName} died too.", f"{mUsername} and {authorName} swapped lives without knowing how to swap back.", f"{authorName} tried to throw {mUsername} off the UBC viewpoint. {authorName} lost their balance and they both fell.", f"{mUsername} went down, but they took {authorName} with them"]
              keklist1 = [f"{mUsername} named the new Disney+ show WandaVision", f"{mUsername} got copystriked by Article 13!", f"{authorName} Alt+F4'd {mUsername}.exe!", f"{authorName} pressed delete. It deleted {mUsername}", f"{authorName} thicc and collapses {mUsername}'s rib cage", f"{mUsername} died due to {authorName} being so stupid", f"{mUsername} died from a high salt intake", f"{mUsername} died while trying to find the city of England", f"{mUsername} died. OOF", f"{mUsername} dies due to lack of friends", f"{mUsername} is kekked by their own stupidity", f"{mUsername} is not able to be begoned. Oh, wait, no, {authorName} begones them anyway", f"{mUsername} is so dumb that they choked on oxygen", f"{mUsername} talked back to mods and got destroyed by the ban hammer", f"{mUsername} was charging their Samsung Galaxy Note 7...", f"{mUsername} was stuck to the ground with flex tape. That's a lotta damage!", f"To show the power of flex tape, {mUsername} was ripped in half!", f"Thanos snapped {mUsername} out of existence", f"{mUsername} asked {authorName} out. {authorName} said no. {mUsername}'s heart was broken.", f"{mUsername} took the 33 on a snow day. They were never found again.", f"{mUsername} took the 43 on a snow day. They were never found again.", f"{mUsername} took the 19 on a snow day. They were never found again.", f"{mUsername} took the 41 on a snow day. They were never found again.", f"{mUsername} took the 99 on a snow day. They were never found again.", f"{mUsername} took the 4 on a snow day. They were never found again.", f"{mUsername} took the 14 on a snow day. They were never found again.", f"{mUsername} took the 9 on a snow day. They were never found again.", f"{mUsername} took the 25 on a snow day. They were never found again.", f"{mUsername} took the 44 on a snow day. They were never found again.", f"{mUsername} took the 17 on a snow day. They were never found again.", f"{mUsername} took the 95 on a snow day. They were never found again.", f"{mUsername} took the 145 on a snow day. They were never found again.", f"{mUsername} took the 143 on a snow day. They were never found again.", f"{mUsername} tried to sled down Marine Drive and fell off the viewpoint.", f"{mUsername} got a life sentence in gay baby jail", f"{mUsername} dropped the soap", f"{mUsername} signed up for Gateman Econ", f"{mUsername} got earraped by Yames Ju's *fantastic* violin performance", f"{mUsername} heard Jerry Shao's singing voice", f"{mUsername} ran out of attempts on an unlimited attempts WebWork", f"{mUsername} tried to get from Forestry to Iona in 10 minutes.", f"{mUsername} played at the Winter Social.", f"{mUsername} ate rcik's cookies and died of glucose poisoning", f"{mUsername} listened to earthquek remixes for 10 hours until their ears fell off", f"{mUsername} joined the UBC Anime Club and became degen", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It backfired. Literally.", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It cost them their sanity", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It cost them their physics grade.", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It exploded.", f"{mUsername} tried to launch a baking soda cannon at the Physics Olympics. It damaged the wall", f"{mUsername} realized that kek means lol in league of legends", f"{mUsername} missed the personal profile deadline.", f"{mUsername} looked like {authorName}", f"{mUsername} realized that hm means yes to Donson.", f"{mUsername} did outdoor rec on a snow day. When the snow finally melted, all that was left was a tube scarf and a picture of Donson.", f"{mUsername} got a half used bottle of lube for secret santa.", f"{mUsername} realized that their crush was too young for them", f"{mUsername} joined the Daily Poll.", f"{mUsername} consumed diammonium phosphate before asking what the biscuit ingredients were.", f"{mUsername} became a singularity.", f"{mUsername} read this message and self destructed 5 seconds later.", f"{mUsername}'s name began with \"st\" and ended with \"n\" in 2018", f"{authorName} JV5'd {mUsername} in Smash Flash 2", f"{authorName} set up {mUsername} with Jerry Shao", f"{authorName} infected {mUsername} with a bad case of dissing Terry", f"{authorName} defenestrated {mUsername} off the UTP balcony.", f"{mUsername} had Town Hall.", f"{mUsername} denied jesyu", f"{authorName} decided to sacrifice {mUsername} to the cult of Gateman", f"{mUsername} walked off the edge of the flat earth", f"Doctor Strange bargained with {mUsername}", f"{mUsername} experienced the Awaddening.", f"{mUsername} ran into the Engineering Band.", f"Snow blocked {mUsername}'s door and they missed their final exam.", f"{mUsername} bomb clipped out of this world", f"{mUsername} BLJ-ed out of this world", f"{mUsername} revealed themselves to be Hipster Pony", f"{mUsername} didn't finish the Newsletter", f"{mUsername} tried to start a Student Council.", f"{mUsername} tried to go to UBC class on December 3, 2018.", f"{mUsername} didn't finish the Cookbook by December 31. Their English mark fell with the idea.", f"{mUsername} tried to go to a 4th year law course on campus day", f"{mUsername} lived, and therefore eventually died", f"{mUsername} connected an LED directly to an Arduino.", f"{mUsername} inhaled ABS fumes from the 3D printer.", f"{mUsername} missed a ComPair deadline.", f"{authorName} slapped {mUsername} with a raw fish", f"{authorName} brought {mUsername} to the forbidden water fountain", f"{mUsername} forgot to add +C when integrating", f"{mUsername} had to do a grad speech with {authorName}.", f"{mUsername} drank from the UBC fountain. Turns out it had soap in it. Turns out the soap was fat and lye soap.", f"{mUsername} didn't tap their Compass Card.", f"{mUsername} got scared by Papa John's", f"{mUsername} played as kirby in Smash. S U C C", f"{mUsername} didn't refill their Compass Card by the new month", f"{mUsername} pulled a Kirby ditto and doublesucced. They tore the universe in half.", f"{mUsername}, I choose you! {mUsername} has fainted.", f"{mUsername} opened a glass door and smashed it against a fire extinguisher.", f"{mUsername} didn't press f and pay respects.", f"{mUsername} didn't trust the Natural Recursion.", f"{mUsername} trusted the generative recursion.", f"{mUsername} didn't comment out the stub.", f"{mUsername} ran out of memory.", f"{mUsername} tried to download RAM from the internet.", f"{mUsername} thought the Yearbook was good.", f"{mUsername} joined Newsletter.", f"{mUsername} forgot their speech lines in Taiwan.", f"{mUsername} thought saying no u all the time was a good idea. (no u)", f"{authorName} hid {mUsername}'s backpack.", f"{mUsername} climbed through the ELI window.", f"{mUsername} forgot to feed the Gateman. Always feed the Gateman.", f"{mUsername} joined ballet.", f"{mUsername} used Canada Post during the strike.", f"{mUsername} plugged power into ground.", f"{mUsername} jumped across the tracks at Commercial-Broadway.", f"{mUsername} joined MAGIC COW", f"{mUsername} questioned the Smart Wise Man", f"{mUsername} wrote a story about their crush. Their crush found out and now {mUsername} is saeyad.", f"{mUsername} took a Sheardown test", f"{mUsername} engaged in social interaction", f"{mUsername} tried to win the Darwin awards. {mUsername} succeeded.", f"{mUsername} stayed at school until 10 pm", f"{mUsername} was a large potato", f"{mUsername} found out {authorName} was a bot. {authorName} made sure {mUsername} was never seen again.", f"{mUsername} died of `@everyone`", f"{mUsername} got scronched by Shep", f"{mUsername} opened the microwave door before the timer ended.", f"{mUsername} put their food in the microwave before realizing that the bottom was coated with Wony Lee's sticky maple syrup", f"{mUsername} was pinged", f"{mUsername} watched Alex jump off the second floor due to Peiyan's puns", f"{mUsername} broke the UTP stairs.", f"{mUsername} jumped off the balcony", f"{mUsername} microwaved a styrofoam cup and made steamed hams.", f"{mUsername} dropped their marshmallow into the sand.", f"{mUsername} got 4% on their test", f"{mUsername} became a meme.", f"{mUsername} joined Chem 121 and wasn't good at labs", f"{mUsername} fell in love with {authorName}", f"{mUsername} joined MUN and got woken up by the fire alarm at 1am", f"{mUsername} joined DEBATE and didn't like talking", f"{mUsername} joined robotics and never came back", f"{mUsername} was too short", f"{mUsername} was too tall", f"{mUsername} got a piece of paper stuck in a test tube in an attempt to clean it and later got scronched by Wilkie", f"{mUsername} became Gandalf, held up the weird pole from the ELI, and let nobody pass.", f"{mUsername} was a res student and got trolled by false fire alarms", f"{mUsername} died during a final", f"{mUsername} did the Hydrogen Balloon experiment and failed.", f"{mUsername} didn't delete this!", f"{mUsername} heard the Year Ones walking in the halls", f"{mUsername} was rickrolled", f"{mUsername} was rcikrolled", f"{mUsername} clicked on this link: https://www.youtube.com/watch?v=dQw4w9WgXcQ", f"{mUsername} tried to pirate a movie about pirates but it didn't work", f"{mUsername} tried to play ping pong at BCIT", f"{mUsername} got spam called during an exam", f"{mUsername} sent a future email to themselves", f"{mUsername} didn't go to the 2020 Reunion and got tracked down by Daria", f"{mUsername} tasted the rainbow, then fell to their death", f"{mUsername} is too hot for their own good", f"{mUsername} was nominated as the sexiest person alive. {mUsername} was killed by {authorName}, who had to defend their title.", f"{mUsername} traversed the UBC fountain with a robot when it was frozen solid...or was it?", f"{mUsername} sank when walking on a frozen fountain", f"{mUsername} made a speech with Jean at grad", f"{mUsername} said ibac (and therefore is bad)", f"{mUsername} used this command and got triggered at the answers", f"{mUsername} died of death", f"{mUsername} consumed dihydrogen monoxide and will die", f"{mUsername} missed a pair of dots on a Lewis Dot Diagram", f"{mUsername} ..", f"{mUsername} didn't realize that they were being watched.", f"{mUsername} fell for Donson and lost their mind chasing them for years and years.", f"{mUsername} turned into a box", f"{mUsername} became the pentagrove.", f"{mUsername} missed the last bus out of UBC.", f"{mUsername} got the mind stone ripped out of their head", f"{mUsername} was sacrificed for the soul stone by {authorName}", f"{mUsername} didn't see that coming", f"{mUsername} became a part of Kieran's story", f"{mUsername} got rekt when Daria read a story that they were written into", f"{mUsername} floats in air", f"{mUsername} tried to flex tape a boat and use it. They found the Titanic instead.", f"{mUsername} tried using flex tape on their grades.", f"{mUsername} thought ships involved actual boats and ran out of money.", f"{mUsername} noticed it said gullible on the ceiling.", f"{mUsername} noticed that cephalized is an anagram of gullible", f"{mUsername} existed and memers saw free real estate.", f"{mUsername}: GENERAL KENOBI", f"{mUsername} watched the prequels nonstop and died of cringe", f"{mUsername}: YODA", f"{mUsername} was a scam", f"{mUsername} didn't go for the head", f"{mUsername} pulled an all-nighter before an exam and fell asleep during the exam.", f"{mUsername} fell asleep on the bus before getting to UBC and woke up back at their house.", f"{mUsername} tapped their wallet", f"{mUsername} didn't thank the bus driver", f"{mUsername} didn't thank the skytrain driver", f"{mUsername} entered through the back door", f"{mUsername} didn't pay attention to SETH.", f"{mUsername} didn't listen to A TIP TO MAKE YOUR TRANSIT RIDE EVEN MORE AWESOME.", f"{mUsername} didn't-HEY VANCOUVER, IT'S SETH. HERE'S A TIP TO MAKE YOUR TRANSIT RIDE EVEN MORE AWESOME. KEEP IT MOVING TO THE BACK OF THE BUS. A LOT OF NEAT STUFF HAPPENING BACK THERE. THAT'S WHERE ALL THE COOL KIDS HANG OUT ANYWAY. YOU'RE MISSING OUT. THANK YOU", f"{mUsername} didn't KEEP IT MOVING TO THE BACK OF THE BUS.", f"{mUsername} didn't realize that A LOT OF NEAT STUFF HAPPENS BACK THERE in the bus.", f"{mUsername} cannot tie their shoe.", f"{mUsername}'s tie was tied by Jean and died of love ", f"{mUsername} consumed some diammonium phosphate", f"{mUsername} didn't realize THAT'S WHERE ALL THE COOL KIDS HANG OUT.", f"{mUsername} was MISSING OUT.", f"{mUsername} found the soul stone. It ripped out their soul.", f"{mUsername} found the mind stone. It made their mind insane.", f"{mUsername} found the time stone. It turned them into a 2 year old.", f"{mUsername} found the space stone. It transported them to the edge of the universe.", f"{mUsername} found the reality stone. It created a reality where they didn\'t exist.", f"{mUsername} found the power stone. They touched it.", f"{mUsername} gave up the time stone", f"{mUsername} realized that now is no time to mourn, now is no time at all", f"{mUsername} didn't have the strongest wills", f"{mUsername} called Thanos a madman", f"{mUsername} didn't go right when Star Lord told them to", f"{mUsername} punched Thanos in the face when the infinity gauntlet was almost off Thanos", f"{mUsername} was hit by Cupid's arrow", f"{mUsername} broke the law of gravity and was sentenced to a year in jail", f"{mUsername} stood under the mistletoe ", f"{mUsername} found the corner outside trans where there's an old barbecue and random trash", f"{mUsername} found the person who lived under the UTP building", f"{mUsername} is an anti-vaxxer", f"{mUsername} broke the internet.", f"{mUsername} used a dead meme", f"{mUsername} forgot to turn off interyear hangouts notifications", f"{mUsername} walked into the UTP office", f"{mUsername} tried to peel soap", f"{mUsername}: I am Groot", f"{mUsername}.", f"{mUsername} procrastinated on their annotations", f"{mUsername} failed to read the book for English", f"{mUsername} GOT SCAMMED INTO WALKING TO THE BOOKSTORE TWICE FOR AN SD CARD", f"{mUsername} became unbalanced, as all things shouldn't be", f"{mUsername} spoiled Infinity War", f"{mUsername} is obsessed with Infinity War and won't stop talking about it", f"{mUsername} leaked the trailer for Avengers 4", f"{mUsername} spoiled Avengers 4", f"{mUsername} couldn't watch the Avengers 4 trailer", f"{mUsername} put sugar on a bass speaker", f"{mUsername} walked into history drinking apple juice from a ziploc bag", f"{mUsername} didn't leave before thank yous at soup day", f"{mUsername} put duct tape on the UTP walls and left them for 3 weeks", f"{mUsername} became unwise", f"{mUsername} didn't do their homework", f"{mUsername} rebooted the clone wars", f"{mUsername} moved all the Disney stuff on Netflix to Disney+", f"{mUsername} created Disney+", f"{mUsername} rebooted Spiderman", f"{mUsername} rebooted Spiderman again", f"{mUsername} rebooted Spiderman yet another time", f"{mUsername} created the Emoji Movie", f"{mUsername} didn't soundproof the ELI", f"{mUsername} can't run", f"{mUsername} didn't call UNO", f"{mUsername} forgot to change the sign", f"{mUsername} walked up the stairs 2 at a time", f"{mUsername} died. Kowalski, analysis.", f"Doctor Strange: Let me guess, your life?\n{mUsername}: It was, and it was beautiful", f"{mUsername} dressed up as an iClicker for halloween and tried to sit down in class", f"{mUsername} and {authorName} have a snowball fight. {mUsername} got snowed to death.", f"{mUsername} found the aurora borealis, at this time of year, at this time of day, in this part of the country, localized entirely within their kitchen", f"{mUsername} made steamed hams and steamed themselves in the process", f"{mUsername} was thrown off the face of the Earth", f"{mUsername} doesn't feel so good...", f"{mUsername} is in the endgame now", f"{mUsername} knew there was no other way", f"{mUsername} was a flat earther", f"{mUsername} didn't get the time stone back", f"{mUsername} used this statement when it was already used somewhere else. They got nerfed by {authorName}.", f"{mUsername} made a bad joke", f"{mUsername} broke through one of the walls at UTP", f"{mUsername} didn't realize that THIS IS AN OFFICE SPACE", f"{mUsername} made a bad pun", f"{mUsername} divided by zero, and the math gods banished them from existence", f"{mUsername} drilled to the centre of the Earth.", f"{mUsername} said 2 + 2 = 4", f"{mUsername} said 2 + 2 = 5", f"{mUsername} tried to drink water with a spoon", f"{mUsername} tried to drink water with a plastic bag", f"{mUsername} tried to drink water with chopsticks", f"{mUsername} tried to drink water with a fork", f"{mUsername} used locker 11.", f"{mUsername} video called Bamfield when the receiving phone was finessed by Donson.", f"{mUsername} used a paper straw.", f"{mUsername} forgot Newton's Third Law.", f"{mUsername} didn't wear formal clothes at grad.", f"{mUsername} clapped before all the students were announced.", f"{mUsername} joined the PCMASTERRACE", f"{mUsername} joined the MACSTERRACE", f"{mUsername} joined the PCMACSTERRACE", f"{mUsername} tried to understand anything on a UTP discord", f"{mUsername} thought a time was PM instead of AM", f"{mUsername} didn't know it was time to stop.", f"{mUsername} :thinking:ed too hard.", f"{mUsername}.exe has stopped working", f"{mUsername} encountered shrek", f"{mUsername} didn't turn off the lights in the ELI", f"{mUsername} was the cause of the fact that A GUIDEWAY INTRUSION HAS BEEN DETECTED AT THIS STATION. IF YOU HAVE TRESPASSED ONTO THE GUIDEWAY, YOU ARE IN DANGER AND MUST RETURN TO THE PLATFORM IMMEDIATELY. YOU ARE BEING RECORDED ON CCTV.", f"{mUsername} fed a seagull. They disappeared in seconds.", f"{mUsername} went to school on a snow day.", f"{mUsername} tried to paint the engineering cairn.", f"{mUsername} went to an ECON 101 tutorial. Nobody else was there.", f"{mUsername} got kekked by life.", f"{mUsername} didn't wash the ice cream bucket properly.", f"{mUsername} had no life", f"{mUsername} had too many lives", f"{mUsername} had no friends", f"{mUsername} tried to find the meaning of life and found 42 instead.", f"{authorName} was one of the 5 people {mUsername} met in heaven.", f"{mUsername} 3d printed a kek and was kekked by yems", f"{mUsername} supported Communism", f"{mUsername} spilled 12M H2SO4 on themselves.", f"{mUsername} didn't know how to use a 25.00ml volumetric pipet.", f"{mUsername} overshot the volumetric flask", f"{mUsername} overshot the equivalence point", f"{mUsername} screwed up the lab quiz", f"{mUsername}'s data was too far off", f"{mUsername} screwed up. Who's up?", f"{mUsername} built the grad slideshow and got memed in their own creation", f"{mUsername} misplayed the Windows XP startup at grad.", f"{mUsername} transfailed.", f"{mUsername} tried to use the hallway chalkboards and their work got memed instead", f"{mUsername} failed a UTP calc quiz", f"{mUsername} watched a Jeffrey Grossman lecture", f"{mUsername} didn't agree with Gladwell", f"{mUsername} watched a Jerry Shao video", f"{mUsername} watched a DONSON DONG video", f"{mUsername} watched a W O N Y L E E video", f"{mUsername} fell asleep during Town Hall", f"{mUsername} gamed at UTP", f"{mUsername} found a picture of themselves on the RPL Facebook Page", f"{mUsername} photoshipped and was caught", f"{mUsername} died", f"{mUsername} tried to get people to go to the Maker Expo setup day without realizing it was a scam. They were never the same again.", f"{mUsername} went to the Maker Expo setup day.", f"{mUsername} listened to Daria's speech", f"{authorName} existed, so {mUsername} died", f"{mUsername} tried to present at the Maker Expo.", f"{mUsername} didn't know de way.", f"{mUsername} got stuck in a time loop", f"{mUsername} got stuck in a time vortex", f"{mUsername} got stuck in the mirror dimension", f"{mUsername} got stuck in the Quantum Realm", f"{mUsername} shrank for all eternity", f"{mUsername} didn't tie their shoes during rec", f"{mUsername} encountered a wild Donphan", f"{mUsername}. is. sparta.", f"{mUsername} tried to find the Avengers 4 trailer.", f"{mUsername} didn't remember the 21st night of September", f"{mUsername} didn't bring food for their club", f"{mUsername} didn't double space after typing a period.", f"{mUsername} had a good question, but they didn't have a good answer.", f"{mUsername} didn't cite all their sources", f"{mUsername} rode the Thanoscar", f"{mUsername} snoozed their alarm", f"{mUsername} differentiated with respect to x instead of t", f"{mUsername} lost their UBCcard", f"{mUsername} tried to use the tables at Wesbrook 100", f"{mUsername} pushed the door between ICCS X wing and ICCS main wing. The fire alarms destroyed their ears", f"{mUsername} didn't type one of kek, rip or lol in kekriplol", f"{mUsername} tried to (make-gregor \"Gregor Kiczales\" 1994)", f"{mUsername} `@everyone` and was stoned by an angry mob consisting of Ivan and Louis", f"{mUsername} tried to climb a tree. They fell.", f"{mUsername} existed on December 32, 2018.", f"{mUsername} was born tomorrow", f"{mUsername} didn't change their clocks when daylight savings time ended", f"{mUsername} forgot to study for their final", f"{mUsername} asked a question and got \"no u\" for an answer", f"{mUsername} sat on their iPad Pro with $169 stylus", f"{mUsername} bolded their name on their chem lab.", f"{mUsername} invested in Wony's cryptomoney, chodecoin. It got too thicc and crashed", f"{mUsername} thought mining Bitcoin on their home computer was a good idea", f"{mUsername} jumped in a pile of leaves. Unfortunately, that pile of leaves was over an open sewer pipe.", f"{mUsername} tried to dig in their backyard, hoping they would mine some bitcoin. Instead they got dirt.", f"{mUsername} tried to take the 480 on a Sunday", f"{mUsername} ate snowflakes only to realize they were solidified acid rain molecules", f"{mUsername} tried to use a water hose to remove snow on a cold day", f"{mUsername} didn't hold up a mirror to no u", f"{mUsername} was bad at rec and got their report card back", f"{mUsername} thought Derek was Donson", f"{mUsername} thought Donson was Derek", f"{mUsername} didn't get the alternate meaning of a poem in english", f"{mUsername} lost the sun. Where's the sun? Nobody knows. Except maybe the Beatles.", f"{mUsername} looked at the sun.", f"{mUsername} caught a battery while fishing", f"{mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername} {mUsername}", f"{mUsername} thought a sine wave was a cubic function", f"{mUsername} built a rollercoaster. They weren't able to feel anything after that.", f"{mUsername} decided not to wear safety glasses to a robotics competition and got hit in the face with a beam.", f"{mUsername} didn't get gud.", f"{mUsername} played badminton at Osborne Gym. The birdie got stuck on the second floor.", f"{authorName} gave {mUsername} a piece of paper that said No U on it. {mUsername} was nou'd into oblivion.", f"{authorName} gave diammonium phosphate cookies to {mUsername}.", f"{mUsername} didn't lock their locker at UTP. When they came back after an hour, everything including the locker door was gone.", f"{authorName} threw a frisbee at {mUsername}.", f"{mUsername} threw a chair at the ELI wall and got roasted for being too loud.", f"{mUsername} tried to find the secret UTP server room.", f"{mUsername} ate the forbidden fruit of Tide.", f"{mUsername} plugged a power bar into itself and tried to get infinite energy.", f"{mUsername} cranked the volume up to 11.", f"{mUsername} gained too high of an IQ and the signed integer holding the IQ value underflowed to a negative number.", f"{mUsername} found the real live version of the Dr. Racket cat. It natural recursed itself into infinity, consuming everything around it, including {mUsername}.", f"{mUsername} heard Thomas Kroeker speak", f"{mUsername} deleted their essay after submitting it online. It turns out they submitted the rubric instead.", f"{mUsername}'s computer was encrypted and all their files were locked.", f"{mUsername} tried to make a UTP confessions page.", f"{mUsername} was teleported to a timeline in which they didn't exist", f"{mUsername} shot themselves in the foot. Literally", f"{mUsername} stapled themselves", f"{authorName} destroyed {mUsername}'s sanity with never-ending talking", f"{authorName} reflected the nerfing beam {mUsername} got kekked instead.", f"{mUsername} touched a lightbulb", f"{mUsername} was kekked by Saf for breaking into an ELI", f"{mUsername} did nothing wrong. They got kekked anyway.", f"{mUsername} thought the erasable whiteboard markers were erasable. They thought wrong.", f"{mUsername} became a thot and was promptly begoned.", f"{mUsername}'s mind was erased. Begone, thought!", f"{mUsername}'s mind was blown. None of it remained.", f"{mUsername} tried to fold 1000 paper cranes", f"{mUsername} attempted to put a decoration on top of a christmas tree, but fell and was crushed by the tree", f"{mUsername} car, {mUsername} car", f"{mUsername} tried to do a generative recursion in their mind with no termination argument.", f"{mUsername} tried to find out who the Anonymous Platypus is", f"{mUsername} tried to add alts to a discord server and got nerfed by the owner", f"{mUsername} tried to slide into {authorName}'s DMs", f"{mUsername} was rejected by {authorName} on Valentines Day. REJECTED! REJECTED! {mUsername} got REJECTED! R-E, J-E, C-T-E-D, REJECTED!", f"{mUsername} 3D printed a donut.", f"{mUsername} was too obese", f"{mUsername} died in a tornado", f"{mUsername} attempted to run Project Euler on a home laptop", f"{mUsername} attempted to run C(7) on their home laptop", f"{mUsername} found themselves on the surface of the sun.", f"{authorName} thought {mUsername} was a pokemon and tried to put them in a pokeball", f"{mUsername} set fire to their hair", f"{mUsername} poked a stick at a grizzly bear", f"{mUsername} ate medicine that was out of date", f"{mUsername} used their private parts as piranha bait", f"{mUsername} got their toast out with a fork", f"{mUsername} did their own electrical work", f"{mUsername} taught themselves how to fly", f"{mUsername} ate a two week old unrefrigerated pie", f"{mUsername} invited a psycho killer inside", f"{mUsername} scratched a drug dealer’s brand new ride", f"{mUsername} took their helmet off in outer space", f"{mUsername} used a clothes dryer as a hiding place", f"{mUsername} kept a rattlesnake as a pet", f"{mUsername} sold both their kidneys on the internet", f"{mUsername} ate a tube of superglue", f"{mUsername} wondered what the red button did.", f"{mUsername} dressed up like a moose during hunting season", f"{mUsername} disturbed a nest of wasps for no good reason", f"{mUsername} stood on the edge of a train station platform", f"{mUsername} drove around the boom gates at a level crossing", f"{mUsername} ran across the tracks between the platforms", f"Such {mUsername}. Much person. Many owaow. Very kekked now.", f"{mUsername} realized that oops! This command is on cooldown right now. Please wait **0.00000000000069** seconds before trying again.", f"{mUsername} tried to use the UTP grad lounge printer. They were nerfed by grads.", f"{mUsername} gambled away their life savings", f"{mUsername} didn’t wear a lab coat in the lab", f"{mUsername} got lost in Europe", f"{mUsername} found asbestos in the UTP walls", f"{mUsername} dropped Francium in the fishtank"]
              kek1=randint(1,len(keklist1)+len(keklist0)+len(keklist2))
              if 1<=kek1<=len(keklist1):
                kek=random.choice(keklist1)
                send_message5 = send_message5 + kek + '\n'
              elif len(keklist1)<kek1<=len(keklist1)+len(keklist0):
                kek0=random.choice(keklist0)
                people.append(person)
                send_message5 = send_message5 + kek0 + '\n'
              else:
                kek2=random.choice(keklist2)
                people.remove(authorName)
                send_message5 = send_message5 + kek2 + '\n'
              if send_message5 != (''):
                while len(send_message5) > 2000:
                  await channel.send(send_message5[0:2000])
                  send_message5=send_message5[2000:]
                await channel.send(send_message5)
              x=randint(1, 10)
              await asyncio.sleep(int(x))
            if len(people)==0:
              send_message = send_message + 'Nobody won!\n'
            else: 
              send_message = send_message + people[0] + ' won!\n'
            hungergames.remove(channel.id)

#        if message.content.upper().startswith ('P'):
 #         try:
  #          await message.add_reaction('🇯')
   #         await message.add_reaction('🇪')
    #        await message.add_reaction('🇸')
     #       await message.add_reaction('🇾')
      #      await message.add_reaction('🇺')
       #   except discord.errors.NotFound:
        #    empty=1

#        if message.content.upper().startswith ('N'):
 #         try:
  #          await message.add_reaction('🇯')
   #         await message.add_reaction('🇪')
    #        await message.add_reaction('🇸')
     #       await message.add_reaction('🇾')
      #      await message.add_reaction('🇺')
       #   except discord.errors.NotFound:
        #      empty=1

        if message.content.upper().startswith ('THANKS '):
          thanks=message.content[7:len(message.content):1]
          send_message = send_message + str(message.author) + ' is thankful for '+str(thanks) + '\n'

        if message.content.upper()==('FEEDBACK'):
          send_message = send_message + 'You want to send an empty feedback?\n'

        if message.content.upper().startswith ('FEEDBACK '):
          feedback=message.content[9:len(message.content):1]
          messaging1=client.get_channel(messaging)
          newMessage = []
          for i in feedback:
            if i!='@':
              newMessage.append(i)
          finalMessage = ''.join(newMessage)
          await messaging1.send('feedback from '+str(message.author)+': '+finalMessage)
          send_message = send_message + 'Thank you. Your feedback has been received\n'

        if message.content.upper().startswith ('MORSE CODE '):
          morsemessage=[]
          morse=message.content.upper()[11:]
          for i in morse:
            if i in morsecode:
              morsemessage.append(morsecode[i])
            else:
              morsemessage.append(i)
          morsefinal='  '.join(morsemessage)
          send_message = send_message + morsefinal + '\n'

        if message.content.upper().startswith ('MORSE DECODE'):
          decodemessage=[]
          decode=message.content[13:]
          words=decode.split(' ')
          for i in words:
            if i in morsedecode:
              decodemessage.append(morsedecode[i])
            else:
              decodemessage.append(i)
          decodefinal=''.join(decodemessage)
          send_message = send_message + decodefinal.lower() + '\n'

        if message.content.upper()==('USER ID'):
          await channel.send(message.author.id)
        elif message.content.upper().startswith('USER ID'):
          person_id=[]
          for i in message.content:
            if i in numbers:
              person_id.append(i)
          personid=''.join(person_id)
          await channel.send(personid)

        if message.content.upper()==('GRADES'):
          if message.author in flowchart:
            await channel.send('You are already playing a game!')
          else:
            flowchart[message.author]=118
            flowchartchannel[message.author]=channel.id
            currentindex=flowchart[message.author]
            options=['**Dealing With Bad Grades**', List[currentindex]]
            for x in Destinations[currentindex]:
              options.append(f"{Destinations[currentindex].index(x)}: {List[x]}")
            options.append('What now?')
            optionsmsg="\n".join(options)
            await channel.send(optionsmsg)

        if message.content.upper() != 'GRADES':
          if message.author in flowchart:
            if channel.id==flowchartchannel[message.author]:
              if message.content.upper()=='EXIT':
                await channel.send('Game ended')
                del flowchart[message.author]
                del flowchartchannel[message.author]
                return
              check = True
              y=message.content
              try:
                int(y)
              except ValueError:
                check = False
              if check == True:
                if int(y) < len(Destinations[flowchart[message.author]]):
                  flowchart[message.author]=Destinations[flowchart[message.author]][int(y)]
                  currentindex=flowchart[message.author]
                  options=[List[currentindex]]
                  for x in Destinations[currentindex]:
                    options.append(f"{Destinations[currentindex].index(x)}: {List[x]}")
                  options.append('What now?')
                  optionsmsg="\n".join(options)
                  await channel.send(optionsmsg)
                else:
                  await channel.send("Number out of range\nWhat now?")
              else:
                await channel.send("Invalid Response\nWhat now?")

        channelid=client.get_channel(messaging)
        if channel==channelid:
          if message.content.upper().startswith ('SAYDONSON'):
            donson=client.get_user(231259532863602698)
            await donson.send(message.content[10:len(message.content):1])
          elif message.content.upper().startswith ('SAYJAMES'):
            james=client.get_user(375445489627299851)
            await james.send(message.content[9:len(message.content):1])
          elif message.content.upper().startswith ('SAYSHAWN'):
            shawn=client.get_user(226588531772882945)
            await shawn.send(message.content[9:len(message.content):1])
          elif message.content.upper().startswith ('SAYWILLIAM'):
            william=client.get_user(226878658013298690)
            await william.send(message.content[11:len(message.content):1])
          elif message.content.upper().startswith ('SAYKAT'):
            kat=client.get_user(416776113872699394)
            await kat.send(message.content[7:len(message.content):1])
          elif message.content.upper().startswith ('SAYKIERAN'):
            kieran=client.get_user(242346507578114058)
            await kieran.send(message.content[10:len(message.content):1])
          elif message.content.upper().startswith('SAYJEAN'):
            jean=client.get_user(242403180653182978)
            await jean.send(message.content[8:len(message.content):1])
          elif message.content.upper().startswith('SAYPERSON '):
            dm_message=message.content.split(' ')
            person = client.get_user(int(dm_message[1]))
            dm_message2=' '.join(dm_message[2:])
            await person.send(dm_message2)
          else:
            c=client.get_channel(magiccow)
            await c.send(message.content)

        if message.content.upper().startswith ('AUSTRALIA'):
          australia1=message.content.upper()[len(message.content):9:-1]
          australia=[]
          for i in australia1:
            if i=='A':
              australia.append('ɐ')
            elif i=='B':
              australia.append('q')
            elif i=='C':
              australia.append('ɔ')
            elif i=='D':
              australia.append('p')
            elif i=='E':
              australia.append('ǝ')
            elif i=='F':
              australia.append('ɟ')
            elif i=='G':
              australia.append('ƃ')
            elif i=='H':
              australia.append('ɥ')
            elif i=='I':
              australia.append('ᴉ')
            elif i=='J':
              australia.append('ɾ')
            elif i=='K':
              australia.append('ʞ')
            elif i=='L':
              australia.append('l')
            elif i=='M':
              australia.append('ɯ')
            elif i=='N':
              australia.append('u')
            elif i=='O':
              australia.append('o')
            elif i=='P':
              australia.append('d')
            elif i=='Q':
              australia.append('b')
            elif i=='R':
              australia.append('ɹ')
            elif i=='S':
              australia.append('s')
            elif i=='T':
              australia.append('ʇ')
            elif i=='U':
              australia.append('n')
            elif i=='V':
              australia.append('ʌ')
            elif i=='W':
              australia.append('ʍ')
            elif i=='X':
              australia.append('x')
            elif i=='Y':
              australia.append('ʎ')
            elif i=='Z':
              australia.append('z')
            elif i==' ':
              australia.append(' ')
            elif i=='1':
              australia.append('Ɩ')
            elif i=='2':
              australia.append('ᄅ')
            elif i=='3':
              australia.append('Ɛ')
            elif i=='4':
              australia.append('ᔭ')
            elif i=='5':
              australia.append('ϛ')
            elif i=='6':
              australia.append('9')
            elif i=='7':
              australia.append('ㄥ')
            elif i=='8':
              australia.append('8')
            elif i=='9':
              australia.append('6')
            elif i=='0':
              australia.append('0')
            elif i=='.':
              australia.append('˙')
            elif i==',':
              australia.append('\'')
            elif i=='!':
              australia.append('¡')
            elif i=='&':
              australia.append('⅋')
            elif i=='(':
              australia.append(')')
            elif i==')':
              australia.append('(')
            elif i=='<':
              australia.append('>')
            elif i=='>':
              australia.append('<')
            elif i=='`':
              australia.append(',')
            elif i=='"':
              australia.append(',,')
            elif i=='?':
              australia.append('¿')
            elif i=='[':
              australia.append(']')
            elif i==']':
              australia.append('[')
            elif i=='{':
              australia.append('}')
            elif i=='}':
              australia.append('{')
            elif i=='/':
              australia.append('\\')
            elif i=='\\':
              australia.append('/')
            else:
              australia.append(i)
          australia3=str(australia)
          australia2="".join(australia)
          send_message = send_message + australia2 + '\n'

        if message.content.upper().startswith ('SPACIFY '):
          spacify1=message.content[8:len(message.content):]
          spacify=[]
          for i in spacify1:
            if i != ' ':
              spacify.append(i)
              spacify.append(' ')
          spacify3=str(spacify)
          spacify2=spacify3[2::5]
          send_message = send_message + spacify2 + '\n'

        if message.content.upper().startswith ('INVISIFY '):
          invisify1 = message.content[9:len(message.content):]
          invisify=[]
          invisify.append(invischar)
          for i in invisify1:
            invisify.append(i)
            invisify.append(invischar)
          invisify2=''.join(invisify)
          send_message = send_message + invisify2 + '\n'
            
        if message.content=='please spam':
          await message.delete()
          n=0
          while n<30:
            await channel.send('jesyu')
            n=n+1
          
        if message.content.upper().startswith ('BACKWARDS'):
          if message.content.upper()==('BACKWARDS JAMES YU'):
            send_message = send_message + 'scam\n'
          else:
            backward=message.content[len(message.content):9:-1]
            send_message = send_message + backward + '\n'
        
        # if re.search("scam", message.content, flags = re.IGNORECASE):
        #   send_message = send_message + 'no, ' + str(message.author) + ' is more of a scam\n'

        # if re.search("uwu", message.content, flags = re.IGNORECASE):
        #   await message.delete()
        #   send_message = send_message + 'weeb\n'

        # if re.search("owo", message.content, flags = re.IGNORECASE):
        #   await message.delete()
        #   send_message = send_message + 'weeb\n'

        # if re.search("friend", message.content, flags = re.IGNORECASE):
        #   send_message = send_message + 'What friends?\n'

        # if re.search("reject", message.content, flags = re.IGNORECASE):
        #   send_message = send_message + 'REJECTED! REJECTED! YOU JUST GOT REJECTED! R-E, J-E, C-T-E-D, REJECTED!\n'

        if re.search("dumthanos", message.content, flags = re.IGNORECASE):
          send_message = send_message + 'I\'m sorry little one\n'

        # if re.search("doubt", message.content, flags = re.IGNORECASE):
        #   if message.content.upper()!='.MEME DOUBT':
        #     em = discord.Embed(colour=0x36393F)
        #     em.set_image(url='https://cdn.discordapp.com/attachments/442535708599779340/519738267738963968/download.png')
        #     await channel.send(embed=em)
        #     send_message = send_message + 'x\n'

        # if re.search("life", message.content, flags = re.IGNORECASE):
        #   em = discord.Embed(colour=0x36393F)
        #   em.set_image(url='https://cdn.discordapp.com/attachments/442535708599779340/505224681603858442/Screen_Shot_2018-10-25_at_8.41.56_940PM.png')
        #   await channel.send(embed=em)

        # if re.search("doing ", message.content, flags = re.IGNORECASE):
        #   if message.content.upper().startswith('DOING '):
        #     send_message = send_message + '*who\'s ' + message.content[6:] + '*\n'
        #   else:
        #     doing_message = message.content.lower().split('doing')
        #     del doing_message[0]
        #     doing_message_final = 'doing'.join(doing_message)
        #     send_message = send_message + '*who\'s' + doing_message_final + '*\n'


        if re.search("snap", message.content, flags = re.IGNORECASE):
          if message.content.upper().startswith('SNAP '):
            snap=message.content[5:len(message.content):1]
            snapped=True
            try:
              int(snap)
            except ValueError:
              snapped=False
            if snapped==True:
              if int(snap)>10:
                send_message = send_message + 'The max times you can snap is 10\n'
              else:
                kList = []
                try:
                  if message.guild.id in [758908682456137750, 815669219114876968]:
                    classList = ["Jonathan", "Michael", "Kevin", "Cora", "Shaana", "Raymond", "Emily", "Ayan", "Alice", "Nora", "James", "Noah", "Sarah", "Arran", "David", "Anna", "Vanessa", "Sheena", "Elliott", "Jocelyn", "Vivian"]
                  else: 
                    classList = ["Aiza", "Alex", "Alyona", "Amanda", "Amy", "Baapooh", "Caitlin", "Daniel", "Donson", "Eddie", "Edward", "Elwin", "Emily", "Fannia", "Felicia", "Floria", "Grady", "Ivan", "James", "Janie", "Jean", "Jerry", "Jessie", "Joey", "Johnny", "Jonathan", "Katherine", "Kieran", "Louis", "Min", "Natalie", "Nicole", "Noreen", "Peiyan", "Ray", "Ricky", "Shawn Lu", "Shawn Yee", "Sherman", "Sophia", "Veronica", "William", "Wilson", "Wony"]
                except AttributeError:
                  classList = ["Aiza", "Alex", "Alyona", "Amanda", "Amy", "Baapooh", "Caitlin", "Daniel", "Donson", "Eddie", "Edward", "Elwin", "Emily", "Fannia", "Felicia", "Floria", "Grady", "Ivan", "James", "Janie", "Jean", "Jerry", "Jessie", "Joey", "Johnny", "Jonathan", "Katherine", "Kieran", "Louis", "Min", "Natalie", "Nicole", "Noreen", "Peiyan", "Ray", "Ricky", "Shawn Lu", "Shawn Yee", "Sherman", "Sophia", "Veronica", "William", "Wilson", "Wony"]
                n=1
                while n<=int(snap):
                  a = len(classList)
                  b= math.ceil(len(classList)/2)
                  while a > b: #gives exactly half of the classList
                      x = random.randrange(a)
                      kList.append(classList[x])
                      del classList[x]
                      a -= 1
                  n=n+1
                send_string = ", ".join(kList)
                send_string2=", ".join(classList)
                if int(snap)>5:
                  try:
                    send_message = send_message + send_string+' have been sacrificed to balance the universe\n-----------------------------------\n**'+send_string2+ '** survived the snappening\n'
                  except discord.errors.NotFound:
                    empty=1
                else:
                  try:
                    send_message = send_message + send_string+' have been sacrificed to balance the universe\n-----------------------------------\n**'+send_string2+ '** survived the snappening\n'
                  except discord.errors.NotFound:
                    empty=1
            if snapped==False:
              kList = []
              try:
                if message.guild.id in [758908682456137750, 815669219114876968]:
                  classList = ["Jonathan", "Michael", "Kevin", "Cora", "Shaana", "Raymond", "Emily", "Ayan", "Alice", "Nora", "James", "Noah", "Sarah", "Arran", "David", "Anna", "Vanessa", "Sheena", "Elliott", "Jocelyn", "Vivian"]
                else: 
                  classList = ["Aiza", "Alex", "Alyona", "Amanda", "Amy", "Baapooh", "Caitlin", "Daniel", "Donson", "Eddie", "Edward", "Elwin", "Emily", "Fannia", "Felicia", "Floria", "Grady", "Ivan", "James", "Janie", "Jean", "Jerry", "Jessie", "Joey", "Johnny", "Jonathan", "Katherine", "Kieran", "Louis", "Min", "Natalie", "Nicole", "Noreen", "Peiyan", "Ray", "Ricky", "Shawn Lu", "Shawn Yee", "Sherman", "Sophia", "Veronica", "William", "Wilson", "Wony"]
              except AttributeError:
                classList = ["Aiza", "Alex", "Alyona", "Amanda", "Amy", "Baapooh", "Caitlin", "Daniel", "Donson", "Eddie", "Edward", "Elwin", "Emily", "Fannia", "Felicia", "Floria", "Grady", "Ivan", "James", "Janie", "Jean", "Jerry", "Jessie", "Joey", "Johnny", "Jonathan", "Katherine", "Kieran", "Louis", "Min", "Natalie", "Nicole", "Noreen", "Peiyan", "Ray", "Ricky", "Shawn Lu", "Shawn Yee", "Sherman", "Sophia", "Veronica", "William", "Wilson", "Wony"]
              a = len(classList)
              b= math.ceil(len(classList)/2)
              while a > b: #gives exactly half of the classList
                  x = random.randrange(a)
                  kList.append(classList[x])
                  del classList[x]
                  a -= 1
              send_string = ", ".join(kList)
              send_string2=", ".join(classList)
              try:
                send_message = send_message + send_string+' have been sacrificed to balance the universe\n-----------------------------------\n**'+send_string2+ '** survived the snappening\n'
              except discord.errors.NotFound:
                empty=1
          else:
            kList = []
            try:
              if message.guild.id in [758908682456137750, 815669219114876968]:
                classList = ["Jonathan", "Michael", "Kevin", "Cora", "Shaana", "Raymond", "Emily", "Ayan", "Alice", "Nora", "James", "Noah", "Sarah", "Arran", "David", "Anna", "Vanessa", "Sheena", "Elliott", "Jocelyn", "Vivian"]
              else: 
                classList = ["Aiza", "Alex", "Alyona", "Amanda", "Amy", "Baapooh", "Caitlin", "Daniel", "Donson", "Eddie", "Edward", "Elwin", "Emily", "Fannia", "Felicia", "Floria", "Grady", "Ivan", "James", "Janie", "Jean", "Jerry", "Jessie", "Joey", "Johnny", "Jonathan", "Katherine", "Kieran", "Louis", "Min", "Natalie", "Nicole", "Noreen", "Peiyan", "Ray", "Ricky", "Shawn Lu", "Shawn Yee", "Sherman", "Sophia", "Veronica", "William", "Wilson", "Wony"]
            except AttributeError:
              classList = ["Aiza", "Alex", "Alyona", "Amanda", "Amy", "Baapooh", "Caitlin", "Daniel", "Donson", "Eddie", "Edward", "Elwin", "Emily", "Fannia", "Felicia", "Floria", "Grady", "Ivan", "James", "Janie", "Jean", "Jerry", "Jessie", "Joey", "Johnny", "Jonathan", "Katherine", "Kieran", "Louis", "Min", "Natalie", "Nicole", "Noreen", "Peiyan", "Ray", "Ricky", "Shawn Lu", "Shawn Yee", "Sherman", "Sophia", "Veronica", "William", "Wilson", "Wony"]
            a = len(classList)
            b= math.ceil(len(classList)/2)
            while a > b: #gives exactly half of the classList
                x = random.randrange(a)
                kList.append(classList[x])
                del classList[x]
                a -= 1
            send_string = ", ".join(kList)
            send_string2=", ".join(classList)
            try:
              send_message = send_message + send_string+' have been sacrificed to balance the universe\n-----------------------------------\n**'+send_string2+ '** survived the snappening\n'
            except discord.errors.NotFound:
              empty=1

        # if re.search("remember", message.content, flags = re.IGNORECASE):
        #   send_message = send_message + 'I hope they remember you\n'

        # if re.search("slow", message.content, flags = re.IGNORECASE):
        #   send_message = send_message + '*despacito*\n'

        # if re.search ("sad", message.content, flags=re.IGNORECASE):
        #   send_message = send_message + 'This is so sad\nAlexa, play Despacito\nhttps://www.youtube.com/watch?v=kJQP7kiw5Fk\n'

        if re.search("thanos did nothing wrong", message.content, flags = re.IGNORECASE):
          send_message = send_message + '<@!'+str(message.author.id)+'> '+'You have my respect, '+ str(message.author) + '\n'

        # if re.search("anyway", message.content, flags = re.IGNORECASE):
        #   if message.author.id==375445489627299851:
        #     send_message = send_message + 'said James\n'

        # if re.search ("aaaaa", message.content, flags = re.IGNORECASE):
        #   send_message = send_message + 'https://www.youtube.com/watch?v=yBLdQ1a4-JI\n'

        # if re.search("ibac", message.content, flags = re.IGNORECASE):
        #   send_message = send_message + 'ifront\n'

        # byeMessage = False
        # balanceMessage = False
        # shipMessage = False
        # hiMessage = False
        # nootMessage = False
        # strangeMessage = False
        # marthaMessage = False
        # blackPantherMessage = False
        # sorryMessage = False

        # contents0=message.content.split(' ')
        # contents=[]
        # for i in contents0:
        #   contents = contents + (i.split('\n'))
        # for word in contents:
            
        #   if filtered(word.upper()) in bye:
        #     byeMessage = True

        #   if filtered(word.upper()) in balance:
        #     balanceMessage = True
        
        #   if filtered(word.upper())=='SHIP':
        #     shipMessage = True

        #   if filtered(word.upper()) in hi:
        #     hiMessage = True

        #   if filtered(word.upper()) == 'NOOT':
        #     nootMessage = True

        #   if filtered(word.upper()) == 'STRANGE':
        #     strangeMessage = True

        #   if filtered(word.upper()) == 'MARTHA':
        #     marthaMessage = True

          # if filtered(word.upper()) in bp:
          #   blackPantherMessage = True
          
          # if filtered(word.upper()) in sorry:
          #   if message.content.upper() != '.MEME SORRY':
          #     sorryMessage = True
        
        # if byeMessage:
        #     send_message = send_message + 'Goodbye my child\n'

        # if balanceMessage:
        #   send_message = send_message + 'Perfectly balanced, as all things should be\n'
        
        # if shipMessage:
        #   send_message = send_message + 'iship\n'

        # if hiMessage:
        #   send_message = send_message + 'Hello my child\n'

        # if nootMessage:
        #   send_message = send_message + 'https://www.youtube.com/watch?v=a4VvRWTD3Ok&t=1s\n'

        # if strangeMessage:
        #   send_message = send_message + '*Doctor* Strange\n'

        # if marthaMessage:
        #   send_message = send_message + 'WHY DID U SAY THAT NAME\n'

        # if blackPantherMessage:
        #   em=discord.Embed(colour=0x36393F)
        #   em.set_image(url='https://cdn.discordapp.com/attachments/375448655655862275/492889904066592779/Screen_Shot_2018-09-21_at_7.46.36_825PM.png')
        #   await channel.send(embed=em)
        
        # if sorryMessage:
        #   r=randint(0,1)
        #   if r==0:
        #     send_message = send_message + 'I\'m sorry little one.\n'
        #   else:
        #     send_message = send_message + 'Reality is often disappointing\n'
        
      # if swore:
      #   send_message = send_message + 'https://tenor.com/ELo4.gif\n'
      #   await message.delete()
  
  if channel.id in incogchannel:
    await asyncio.sleep(30)
    try:
      await message.delete()
    except discord.errors.NotFound:
      empty=1

  if send_message != (''):
    while len(send_message) > 2000:
      await channel.send(send_message[0:2000])
      send_message=send_message[2000:]
    await channel.send(send_message)

# chatFilter2=['BS', 'HELL']
# chatFilterexempt=['FIRETRUCK', 'FEEDBACK', 'FUCK']
bypass_list=[467016289878147073]
balance=['BALANCE', 'BALANCED', 'HALF', 'HALVE', 'HALVES', 'HALF!']
sorry=['SORRY', 'CRY', 'CRYING', 'CRIES', '*CRIES*', 'SACRIFICE', 'SACRIFICED', 'SACRIFICING', 'SACRIFICES', 'CRIED', 'RIP']
hi=['HI', 'HELLO', 'HEY']
bye=['BYE', 'BAI', 'GOODBYE']
scam=['SCAM', 'SCAM,']
mod=[231259532863602698, 416776113872699394, 226588531772882945, 231484431532032000]
tt_mod=[375445489627299851, 231259532863602698]
ban=[]
bp=['PANTHER', 'HYPOCRITE', 'HYPOCRITES', 'HYPOCRITE,']
me=[231259532863602698]
magiccow=584455348417593355
mc_server=433856438604136459
messaging=511242877792157717
donsongeneral=739375221299216414
spoilauthor={}
spoilmessage={}
dirtchannel=set([])
incogchannel=set([])
memes=[437047996203401216, 562474519072210945]
banchannel=[437047996203401216, 562474519072210945, 437048678868582401, 584454574748729352, 758908682456137752]
memes1='437047996203401216'
numberlist=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
snipemax=25
hungergames=[]
morsecode={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'}
morsedecode={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '}
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabetwithspace=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
regionalindicators=['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']
Destinations = [[17, 27], [12], [21, 39], [14, 15, 23], [24, 38, 42],[13, 15], [16, 18], [6, 20], [25, 35], [34], [44], [43], [17], [15], [37], [4, 18, 25, 37], [31], [22], [5], [48, 55, 59], [31], [27], [118], [28], [29, 30, 31], [15, 32], [118], [40], [15, 37], [37],[31, 37], [33, 36, 37], [33], [26], [35], [41], [37], [46, 48], [37, 62], [52], [37], [37, 47], [53], [37], [45, 51], [50, 56], [44],[109], [37, 47, 79], [37], [49, 55, 117], [57], [53], [48, 55], [62], [48], [65], [60], [66], [55], [48, 55, 59], [55], [63], [61], [77], [58, 67], [67], [68, 69], [112], [70], [60, 71], [72, 73], [54], [60], [80, 82], [70, 76], [60, 82, 83], [78], [76], [86], [89, 90, 108], [19], [84], [67], [10, 105, 107], [83], [81], [88], [106], [91, 103], [94], [98], [98], [92, 98], [93, 96, 119], [96], [97], [98], [99], [103], [98], [98, 100, 114], [98, 104], [87, 102, 113], [102], [106, 113], [102, 115], [85, 102, 111], [75], [64, 17], [120], [110], [37], [110], [101], [101, 116], [120], [45, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 17, 74], [95], [120]]
List = [
  "Smash face into pillow ", 
  "Go to outside of Trans extracurricular ", 
  "Go to Bons ", 
  "Talk to teacher ",
  "Go to the Nest ", 
  "Go home ", 
  "Stay at Trans ", 
  "Go to band or reach ",
  "Run away ",
  "Attend Soup Day ",
  "Go to Arts ",
  "Find a person with a worse grade ",
  "Get called nerd",
  "Somehow get lost",
  "Bribe",
  "Parents",
  "Get invaded by Sheardown memes",
  "Cry",
  "Bearded dragon overload",
  "Be sad",
  "Get forced to climb through ELI window",
  "Meet some hobo",
  "Win :)",
  "Get scronched",
  "Study",
  "Police",
  "Draw a dinosaur",
  "Uncertain fate",
  "Get recommended a tutor",
  "Fall asleep",
  "Get sidetracked by video games",
  "Fail studying",
  "Get brainwashed",
  "Forget everything on the test",
  "Become full and happy",
  "Get pressured into making thank you speech",
  "Watch youtube instead",
  "DEATH",
  "Drop 2 of the 3 bubble teas you just bought",
  "Get stuck on a snowdrifting bus", 
  "<insert fate here>",
  "Get laughed at",
  "Run into grad",
  "Fail to find one",
  "End up with no job",
  "End up with no money",
  "Fail to get into UBC",
  "Get shamed publicly",
  "Disowned",
  "Freeze to...",
  "End up homeless",
  "Apply for job",
  "Take 5 hours to get home",
  "Be late for dinner",
  "Do a bottle flip",
  "Be useless",
  "Beg for money",
  "Get rejected because age <15",
  "Realize pennies are worthless",
  "Hide in sketchy corner with old barbecue so no one sees you crying",
  "Be sad",
  "Have sticky hands",
  "Watch the contents form a puddle",
  "Watch classmates run inside and come out with a huge roll of toilet paper",
  "Remember the time you got roasted at IEP",
  "Get a few cents",
  "Like you",
  "Go to corner store",
  "Realize you can't pay for any overpriced coke",
  "Buy a 1L coke",
  "Realize you got scammed",
  "Accidentally leave coke in lounge",
  "Miraculously find that it's still there",
  "Come back to find it all gone",
  "Attempt to do homework",
  "Be told there's none",
  "Fail calc test",
  "Get exposed",
  "Spend a week feeling ashamed",
  "Feel marginally better because Mr. Wilkie let you play with Penny",
  "Run out of time",
  "Water plants with hot water",
  "Not care because Dr. MacDonald drops lowest mark",
  "Fail a couple too many tests",
  "Realize that you can't get 100\% anyway",
  "Fail anyway",
  "Suddenly remember that you need to water your plants",
  "Consume diammonium phosphate out of hunger",
  "Learn to make the diammonium phosphate fly",
  "Stay up all night finishing",
  "Assure yourself that you'll do it in the morning",
  "Parents force you to turn off the lights and sleep",
  "65%",
  "Hand it in late",
  "Forget to wake up earlier",
  "Be late for school",
  "Be glad you no longer need to wake up early to play a sport",
  "Think about how fun sports were",
  "Feel depressed",
  "Become a potato",
  "Accept the fact of your failure",
  "Regret them",
  "Become the ultimate zombie",
  "Be non-functional the next day",
  "no u",
  "Go to rec hoping it will boost your average",
  "Expend excessive ATP",
  "Study a little harder",
  "Hope there's a late start",
  "Remember the time you got publicly roasted by your parents at soup day",
  "67% :)",
  "Guess correctly on multiple choice",
  "Drink from UBC fountain instead", 
  "Earn extra bonus marks on the bonus question",
  "Suddenly realize that you're procrastinating by coding a flowchart",
  "Question your life choices",
  "Oh wait what life",
  "Live with newly befriended hobo",
  "66%",
  "Wake up late",
  "Game over. Type `exit` to end the game"
]
flowchart={}
flowchartchannel={}
rate={'A': 52, 'B': 96, 'C': 25, 'D': 57, 'E': 83, 'F': 32, 'G': 10, 'H': 34, 'I': 99, 'J': 21, 'K': 35, 'L': 74, 'M': 13, 'N': 39, 'O': 42, 'P': 94, 'Q': 23, 'R': 49, 'S': 68, 'T': 62, 'U': 100, 'V': 46, 'W': 51, 'X': 62, 'Z': 77, '1': 35, '2': 47, '3': 85, '4': 32, '5': 27, '6': 15, '7': 71, '8': 33, '9': 96, '0': 40, ' ': 53, '.': 42, ',': 86, ':': 75, '-': 50, '+': 36, '&': 29, '/': 66, '\'': 40}
pong={}
pong_channels=[]
gamemode={}
transterms_data=620356122745896980
dlogging=595133816314658819
kekdata=655576473994002472
terms=[]
terms_only=[]
terms2={}
terms_only2=[]
keklist=[]
invischar='឵឵'
rps_list=["Rock", "Paper", "Scissors"]

@buttons.click
async def button_rock(ctx):
  rps_choice = random.choice(rps_list)
  if rps_choice == "Rock":
    await ctx.reply("You chose **Rock**\nThanos chose **Rock**\nYou tied!")
  if rps_choice == "Paper":
    await ctx.reply("You chose **Rock**\nThanos chose **Paper**\nYou lost!")
  if rps_choice == "Scissors":
    await ctx.reply("You chose **Rock**\nThanos chose **Scissors**\nYou won!")
@buttons.click
async def button_paper(ctx):
  rps_choice = random.choice(rps_list)
  if rps_choice == "Rock":
    await ctx.reply("You chose **Paper**\nThanos chose **Rock**\nYou won!")
  if rps_choice == "Paper":
    await ctx.reply("You chose **Paper**\nThanos chose **Paper**\nYou tied!")
  if rps_choice == "Scissors":
    await ctx.reply("You chose **Paper**\nThanos chose **Scissors**\nYou lost!")
@buttons.click
async def button_scissors(ctx):
  rps_choice = random.choice(rps_list)
  if rps_choice == "Rock":
    await ctx.reply("You chose **Scissors**\nThanos chose **Rock**\nYou lost!")
  if rps_choice == "Paper":
    await ctx.reply("You chose **Scissors**\nThanos chose **Paper**\nYou won!")
  if rps_choice == "Scissors":
    await ctx.reply("You chose **Scissors**\nThanos chose **Scissors**\nYou tied!")

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))