import os
import discord
import gspread
import datetime
import jaconv
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import tasks
from server import keep_alive

my_secret = os.environ['TOKEN']
#discordBotのトークン
TOKEN = my_secret  
#投稿するチャンネルのID
TEST_CHANNEL = 973840467420663818
TITAN_CHANNEL = 971707220070899712
CHANNEL_ID = [TEST_CHANNEL,TITAN_CHANNEL]

client = discord.Client()

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

#認証キーの設定
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'spreadsheet-test-349902-f0569c22f9c1.json', scope)

gc = gspread.authorize(credentials)

#スプレッドシートキーの設定
SPREADSHEET_KEY = os.environ['SHEET']
workbook = gc.open_by_key(SPREADSHEET_KEY)


#############################################################
# チャット内容をスプレッドシートに記載する関数
# 引数：シート名, ディスコードID, 日付, 記載内容, 行オフセット
# 戻り値：なし
#############################################################
def write_report(worksheet, userID, date, amount, offset):

    nCell = worksheet.find(str(userID))
    findFlag = 0
    if nCell is None :
      findFlag = 0
    else:
      findFlag = 1
      rows = nCell.row + offset
      nCols = nCell.col
      dCell = worksheet.find(date)
      cols = dCell.col
      base = datetime.time(9, 0, 0)
      base2 = datetime.time(5, 0, 0)
      # 現在時間
      dt_now = datetime.datetime.now() + datetime.timedelta(hours=9)
      hnow = dt_now.time()
      if base > hnow and base2 < hnow:
          cols = cols + 1
      # print( str(cols) + "," + str(rows) +"\n")
  
      worksheet.update_cell(rows, cols, amount)
      worksheet.update_cell(rows, nCols - 1, '完了')
    return findFlag


############################################################
# 記載シートを特定する関数
# 引数：ゲームタイトル
# 戻り値：シート
#############################################################
def titleCheck(title):
    worksheet_list = workbook.worksheets()
    bcgTitle = title
    exist = False
    for current in worksheet_list:
        if current.title == bcgTitle:
            exist = True
    if exist == False:
        return

    return workbook.worksheet(bcgTitle)


#############################################################
# 未報告者のIDを取得して配列に格納する関数
# 引数：ゲームタイトル
# 戻り値：ディスコIDの一次元配列
#############################################################
def noComplite(title):
    user = []
    worksheet = workbook.worksheet(title)
    cell_list = worksheet.findall('未')
    for cell in cell_list:
        rows = cell.row
        col = cell.col + 1
        user.append(int(worksheet.cell(rows, col).value))
        # print(worksheet.cell(rows,col).value)
        # print(user)
    return user


#############################################################
# 報告完了をリセットする関数（0時に起動）
# 引数：ゲームタイトル
# 戻り値：なし
#############################################################
@tasks.loop(seconds=60)
async def reportReset(title, time):
    now = datetime.datetime.now() + datetime.timedelta(hours=9)
    now = now.strftime('%H:%M')
    # print(now)
    # print(time)
    if now == time:
        worksheet = workbook.worksheet(title)
        cell_list = worksheet.findall('完了')
        for cell in cell_list:
            rows = cell.row
            col = cell.col
            worksheet.update_cell(rows, col, '未')


#############################################################
# 未報告者にメンションする数
# 引数：ゲームタイトル, 投稿するテキストチャンネルID
# 戻り値：なし
#############################################################
@tasks.loop(seconds=60)
async def noFinUserSend(title, channel, time):
    now = datetime.datetime.now() + datetime.timedelta(hours=9)
    now = now.strftime('%H:%M')
    # print(now)
    # print(time)
    if now == time:
        inchannel = client.get_channel(channel)
        noFinUser = []
        noFinUser = noComplite(title)
        memberMention = ""

        if not noFinUser:
            return
        else:
            for user in noFinUser:
                memberMention = memberMention + "<@" + str(user) + ">\n"
                print(memberMention)
            await inchannel.send(f"{memberMention} スカラー報告が未完了です。報告お願いします！")


#############################################################
# Bot起動時に動作する関数
# 引数：なし
# 戻り値：なし
#############################################################
@client.event
async def on_ready():
    print("------------Bot起動中------------")
    print(discord.__version__)

    #ループ処理実行
    noFinUserSend.start('test', TITAN_CHANNEL, '23:59')
    reportReset.start('test', '05:00')


#############################################################
# ディスコでメッセージ受け取った際に動作する関数
# 引数：メッセージ
# 戻り値：なし
#############################################################
@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id not in CHANNEL_ID:
        return

    if message.content == "":
        return

    worksheet = titleCheck('test')
    convMessage = jaconv.z2h(message.content, kana=False, digit=True, ascii=True)
    convMessage = convMessage.replace("　"," ")    
    print(convMessage)
    userID = message.author.id
    receipt = convMessage.split(' ')
    print(receipt)
    today = datetime.date.today() + datetime.timedelta(hours=9)
    today = today.strftime('%m/%d')
    print(today)    

    if len(receipt) != 4:
        await message.channel.send(
            'フォーマットが正しくありません。\n 例）耐久 30 TITA 100\nスペースと英数字は半角、全角どちらでも問題ないです。')
        return

    if receipt[0] == '耐久' and receipt[2] == 'TITA':
        tOffset = 2
        ttOffset = 0
        rFlag = write_report(worksheet, userID, today, float(receipt[1]), tOffset)
        write_report(worksheet, userID, today, float(receipt[3]), ttOffset)

        if rFlag == 1:
          await message.channel.send('本日の報告を受け付けました！')
        else:
          await message.channel.send('該当のユーザーが見つかりません')
        return
    else:
        await message.channel.send(
            'フォーマットが正しくありません。\n 例）耐久 30\nスペースと英数字は半角、全角どちらでも問題ないです。')
        return


# ウェブサーバーを起動する
keep_alive()

client.run(TOKEN)
