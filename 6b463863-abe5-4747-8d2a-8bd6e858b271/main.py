import discord
#import time
import random
#import json
import keep_alive
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print('目前登入身份：',client.user)
    #game = discord.Game('張霈承不要再睡了')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    #await client.change_presence(status=discord.Status.dnd, activity=game)
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Boys'))
    await client.change_presence(activity=discord.Streaming(name=' ', url='https://www.youtube.com/watch?v=tLrnWxXsyho&t=3223s'))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=''))
    print("==============================")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the Bot")


@client.event
#當有訊息時
async def on_message(message):

    keyword = ['道歉']

    #Happy New Year
    HNY = ['＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊\n.\xa0\xa0\xa0\xa0\xa0        \xa0\xa0\xa0\xa0\xa0\xa0 ◢◣\u3000\u3000 \u3000◢◣\u3000\n\u3000\u3000◢◤\u3000◥◣◢◤\u3000◥◣\u3000\n\u3000◢◤\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000◥◣\n\u3000█\u3000︵\u3000\u3000\u3000\u3000\u3000\u3000︵ \u3000█\n\u3000█\u3000〃\u3000\u3000 ┬┬\u3000\u3000〃 \u3000█\n\u3000◥◣\u3000\u3000\u3000 ╰╯ \u3000\u3000\u3000◢◤\n\u3000\u3000◥█▅▃▃\u3000▃▃▅█◤\n\u3000\u3000\u3000\u3000◢◤\u3000\u3000\u3000◥◣\u3000\n\u3000\u3000\u3000\u3000█\u3000\u3000\u3000\u3000\u3000█\n\u3000\u3000\u3000◢◤▕\u3000 ×\u3000▎◥◣\xa0\xa0\xa0\xa0\n\u3000\u3000▕▃◣◢▅▅▅◣◢▃\u3000\n╭☆ ╭╧╮╭╧╮╭╧╮╭╧╮╭☆\n╰╮ ║新│║年│║快│║樂│╰╮\n☆╰ ╘∞╛╘∞╛╘∞╛╘∞╛☆╮\n＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊'
    ,'.°”˜˜”°•.¸☆ ★ ☆¸.•°”˜˜”°•.¸☆\n.╔╗╔╦══╦═╦═╦╗╔╗ ★ ★ ★\n.║╚╝║══║═║═║╚╝║ ☆¸.•°”˜˜”°•.¸☆\n.║╔╗║╔╗║╔╣╔╩╗╔╝ ★ NEW YEAR ☆\n.╚╝╚╩╝╚╩╝╚╝═╚╝ ♥￥☆★☆★☆￥♥ ★☆❤♫❤♫❤\n..•¨•..¸☼ ¸.•¨*•.♫❤♫❤♫❤'
    ]
    #Happy New Year

    #Good Morning
    GoodMorning = ['⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⢳⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠋⠀⢰⠎⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢆⣤⡞⠃⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢠⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⣀⣾⢳⠀⠀⠀⠀⢸⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣀⡤⠴⠊⠉⠀⠀⠈⠳⡀⠀⠀⠘⢎⠢⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀\n⠳⣄⠀⠀⡠⡤⡀⠀⠘⣇⡀⠀⠀⠀⠉⠓⠒⠺⠭⢵⣦⡀⠀⠀⠀\n⠀⢹⡆⠀⢷⡇⠁⠀⠀⣸⠇⠀⠀⠀⠀⠀⢠⢤⠀⠀⠘⢷⣆⡀⠀\n⠀⠀⠘⠒⢤⡄⠖⢾⣭⣤⣄⠀⡔⢢⠀⡀⠎⣸⠀⠀⠀⠀⠹⣿⡀\n⠀⠀⢀⡤⠜⠃⠀⠀⠘⠛⣿⢸⠀⡼⢠⠃⣤⡟⠀⠀⠀⠀⠀⣿⡇\n⠀⠀⠸⠶⠖⢏⠀⠀⢀⡤⠤⠇⣴⠏⡾⢱⡏⠁⠀⠀⠀⠀⢠⣿⠃\n⠀⠀⠀⠀⠀⠈⣇⡀⠿⠀⠀⠀⡽⣰⢶⡼⠇⠀⠀⠀⠀⣠⣿⠟⠀\n⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⡶⠤⣷⣅⡀⠀⠀⠀⣀⡠⢔⠕⠁⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠫⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀',
    '⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀\n⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀\n⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀\n⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜\n⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇\n⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀\n⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀\n⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋',
    '⡿⠿⠛⠋⠉⠁⠀⠀⣀⣀⣀⠀⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⢀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡉⠙⠻⢿⣿⣿⣿⣿⣿⢿⣦⠈⢻⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡆⠀⠀⢻⣿⣿⣿⣿⡆⠈⢳⡄⠹⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠈⢿⣿⣿⣿⣷⠖⠀⠀⣿⣿⣿⣿⣿⣄⠀⣿⡄⠘⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣇⠀⢄⡙⠋⠻⡄⠀⣼⣿⣿⣿⣩⠟⠟⠀⣼⣿⡄⠹⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣭⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣦⣴⣿⣿⣷⠀⠛⠻⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⢰⣶⣄⠈\n⣏⣉⣛⣛⣛⣛⣥⣶⣾⣿⣿⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⠟⠀\n⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠈⠁⢀⣼\n⡇⠀⠹⣿⣿⣿⡿⠿⠛⣋⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⣾⣿⣿']
    #Good Morning

    #temp
    temppicture = [
    '⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕\n⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕\n⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕\n⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕\n⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑\n⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐\n⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐\n⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔\n⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕\n⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕\n⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕\n⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕\n⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁\n⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿']
    #temp

    #Good Night
    GoodNight =['＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊\n　　　∧∧　                    -------------------\n　　 (　･･)                    |   Good night  !     |\n 　 ＿|　⊃／(＿＿          -------------------\n／　└-(＿＿＿／\n\nzZzZ...\n　＜⌒／ヽ-､＿\n／＜_/＿＿＿＿／\n￣￣￣￣￣￣￣\n＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊']
    #Good Night

    #Song
    song = ['瘋狂世界','擁抱','愛情的模樣','I Love You 無望','終結孤單','愛情萬歲','一顆蘋果','相信','純真','人生海海','而我知道','恆星的恆心','九號球','時光機','生命有一種絕對','倔強','孫悟空','讓我照顧你','回來吧','聽不到','超人','聖誕夜驚魂','天使','香水','最重要的小事','忘詞','寵上天','突然好想你','你不是真正的快樂','我心中尚未崩壞的地方','如煙','後青春期的詩','笑忘歌','倉頡','洗衣機','乾杯','我不願讓你一個人','星空','OAOA','第二人生','諾亞方舟','有些事現在不做 一輩子都不會做了','T 121 3121','如果我們不曾相遇','成名在望','好好','後來的我們','頑固','派對動物','最好的一天','終於結束的起點','任意門','轉眼','你說那C和弦就是Do Mi So','龍捲風','一半人生','隱形的紀念','因為你 所以我','什麼歌','青空未來','刻在我心底的名字','說好不哭','玫瑰少年','盛夏光年']
    #['垃圾車','少年他的奇幻漂流']
    #Song

    #舉牌小人
    talk = ['|￣￣￣￣￣￣￣￣￣￣￣|\n','|＿＿＿＿＿＿＿＿＿＿＿|\n','                \ (•◡•) / \n','                   \      / \n','                      ---\n','                      |   |\n']
    #舉牌小人

    #喜哩工傻
    saywhat = ['⠄⠰⠛⠋⢉⣡⣤⣄⡉⠓⢦⣀⠙⠉⠡⠔⠒⠛⠛⠛⠶⢶⣄⠘⢿⣷⣤⡈⠻⣧\n⢀⡔⠄⠄⠄⠙⣿⣿⣿⣷⣤⠉⠁⡀⠐⠒⢿⣿⣿⣿⣶⣄⡈⠳⢄⣹⣿⣿⣾⣿\n⣼⠁⢠⡄⠄⠄⣿⣿⣿⣿⡟⠄⡐⠁⡀⠄⠈⣿⣿⣿⣿⣿⣷⣤⡈⠻⣿⣿⣿⣿\n⢻⡀⠈⠄⠄⣀⣿⣿⣿⡿⠃⠄⡇⠈⠛⠄⠄⣿⣿⣿⣿⣿⣿⠟⠋⣠⣶⣿⣿⣿\n⠄⢉⡓⠚⠛⠛⠋⣉⣩⣤⣤⣀⠑⠤⣤⣤⣾⣿⣿⣿⡿⠛⢁⣤⣾⣿⣿⣿⣿⣿\n⠄⠈⠙⠛⠋⣭⣭⣶⣾⣿⣿⣿⣷⣦⢠⡍⠉⠉⢠⣤⣴⠚⢩⣴⣿⣿⣿⣿⣿⣿\n⠄⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣭⣭⣭⣥⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠄⣴⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⣮⣭⣝⣛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠄⠙⣿⡄⠄⠄⢀⡤⠬⢭⣝⣒⢂⠭⣉⠻⠿⣷⣶⣦⣭⡛⣿⣿⣿⣿⣿⣿⣿⣿\n⠄⠄⠸⣿⡇⠄⠸⣎⣁⣾⠿⠉⢀⠇⣸⣿⣿⢆⡉⠹⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿\n⠄⠄⠄⣿⡇⠄⢀⡶⠶⠶⠾⠿⠮⠭⠭⢭⣥⣿⣿⣷⢸⣿⢸⣿⣿⣿⣿⣿⣿⣿\n⠄⠄⠄⣿⡇⠄⠈⣷⠄⠄⠄⣭⣙⣹⢙⣰⡎⣿⢏⣡⣾⢏⣾⣿⣿⣿⣿⣿⣿⣿\n⠄⠄⢰⣿⡇⠄⠄⢿⠄⠄⠈⣿⠉⠉⣻⣿⡷⣰⣿⡿⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠄⠄⢸⣿⡇⠄⠄⠘⠿⠤⠤⠿⠿⠿⢤⣤⣤⡿⣃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠄⠄⠘⢿⣷⣤⣄⣀⣀⣀⣀⣀⣠⣴⣾⡿⢋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋']
    #喜哩工傻

    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return

  #  if message.content == '短球':
  #              await message.channel.send('學長你知道什麼是短球嗎？')
  
    if '桌遊網址' in message.content:
      await message.channel.send('https://zh.boardgamearena.com/')
  
    if '短球' in message.content:
      await message.channel.send('學長你知道什麼是短球嗎？')
    
    if '道歉' in message.content:
      await message.channel.send('學長對不起。')

    if '邏輯' in message.content:
      await message.channel.send('若P則Q => 非P則非Q')

    if '新年快樂' in message.content and '！！！' not in message.content:
      a = random.randint(0,1)
      await message.channel.send(HNY[a])

    if '早安' in message.content:
      b = random.randint(0,len(GoodMorning)-1)
      await message.channel.send('早安\n'+GoodMorning[b])

    if '晚安' in message.content:
      await message.channel.send(GoodNight[0])

    if '供三小' in message.content:
      await message.channel.send(saywhat[0])

    if '給我一首歌' in message.content:
      c = random.randint(0,len(song)-1)
      await message.channel.send(song[c])

    if '給我三首歌' in message.content:
      d = random.sample(song,3)
      await message.channel.send(d)

    
    if '給我' and '首歌' in message.content:
      tmp1 = message.content.split('給我',2)
      tmp2=str(tmp1[1])
      tmp3 = tmp2.split('首歌')
      #tmp2=list(tmp2)
      print(tmp3[0])
      tmp = int(tmp3[0])
      tmp4 = str(len(song))
      if tmp <= len(song):
        e = random.sample(song,tmp)
        await message.channel.send(e)
      else:
        await message.channel.send('沒有這麼多歌啦，歌單只有'+tmp4+'首')
  #    e = random.sample(song,tmp)
  #    await message.channel.send(e)

    if '點歌測試' in message.content:
      await message.channel.send('&p 因為你所以我')




    #if '隨便點一首' in message.content:
    #  d = random.randint(0,len(song)-1)
    #  await message.channel.send('!play '+song[d])



   # if message.content in keyword : 
   #             await message.channel.send('學長對不起。')

    
    #如果以「say」開頭
    if message.content.startswith('say'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼？")
      else:
        await message.channel.send(tmp[1])

    #舉牌小人
    if message.content.startswith('!message'):
      #分割訊息成兩份
      print(len(talk[0]))
      tmp = message.content.split(" ",4)
      #long = int((14-len(tmp[1]))/2)
      #if len(tmp[1]) < 14:
      #  print(long)
      #  tmp[1]=tmp[1].ljust(long,' ')
      #  tmp[1]=tmp[1].rjust(long,' ')
      #await message.channel.send(talk[0]+tmp[1].rjust(long)+'\n'+tmp[2]+'\n'+tmp[3]+'\n'+talk[1]+talk[2]+talk[3]+talk[4]+talk[5])
      await message.channel.send('{0}{1:^45}\n{2:^45}\n{3:^45}\n{4}{5}{6}{7}{8}'.format(talk[0],tmp[1],tmp[2],tmp[3],talk[1],talk[2],talk[3],talk[4],talk[5]))
      #如果分割後串列長度只有1
      #if len(tmp) == 1:

     # else:
     #   await message.channel.send(tmp[1])
    if message.content.startswith('!指令'):
      await message.channel.send('============================\nkeywords = 道歉 / 短球 / 桌遊網址 / 邏輯 / 新年快樂 / 早安 / 晚安 / 供三小 / 給我一首歌\n指令：(前綴 = "井字號"）\nhelp / say / join / leave /!message\n=============================')

    #await client.process_commands(message)
    await client.process_commands(message)

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("我進來囉")
    else:
        await ctx.send("你不在語音頻道內，請先進入語音頻道")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.author.voice):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("我出去囉")
    else:
        await ctx.send("我不在語音頻道裡面阿，要出去哪")


keep_alive.keep_alive()

#client.run('OTM4MzU1NTI0MTEyNjQyMDY5.YfpFrg.1rtvz0KQWCklsJ4z-cssQgIQBRs')  #Testbot
client.run('OTM4MzY0NzA4ODI4ODg0OTky.YfpOPA.P6Yo655otExe7NreeMCnY-kS-8M')   #數學系大一