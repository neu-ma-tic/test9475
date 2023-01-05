import datetime

import discord
from addict import Dict
from core import CogInit, Config, Emoji, SQL_getData, SQL_inquiry, SQL_modify, read_yaml, write_yaml
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


class ActionCancel(Exception):
    pass


guildID = Config.servers


class DateInvaild(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


tz = datetime.timezone(datetime.timedelta(hours=8))


def get_date() -> datetime.date:
    return datetime.datetime.now(tz).date()


def get_time() -> datetime.datetime:
    return datetime.datetime.now(tz)


def date_valid(date):
    try:
        date = datetime.date.fromisoformat(date)
    except:
        raise DateInvaild("日期格式不合理")
    else:
        if not date <= (get_date()):
            raise DateInvaild("日期不合理")
        else:
            return


class SUBSCRIBE(CogInit):
    def __init__(self, bot):
        super().__init__(bot)
        self.config = Dict(read_yaml("config")).subscribe

    def channelCheck(self, ctx) -> bool:
        return (
            ctx.channel.category_id in self.config.valid_category
            and ctx.channel.id not in self.config.exclude_channel
        )

    def managerCheck(self, ctx) -> bool:
        return self.channelCheck(ctx) and ctx.author.id in Config.managers

    def authorCheck(self, ctx, target) -> bool:
        return (self.channelCheck(ctx) and ctx.author.id == int(target[2:-1])) or self.managerCheck(
            ctx
        )

    async def print_overview(self):
        message = "訂閱總覽(如內容有誤需要更改請告知管理者)\n>>> "
        artists = SQL_inquiry(
            """SELECT artists.artist, artists.subscriber, artists.mark FROM `artists`
               NATURAL JOIN subscribers ORDER BY `subscribers`.addTime, subscriber, `artist`"""
        )
        subscribers = {}
        for artist, subscriber, mark in artists:  # 將資料彙整為dict，{subscriber:[artist, mark]}
            if subscriber not in subscribers.keys():
                subscribers[subscriber] = [[artist, mark]]  # dict中已有該訂閱者
            else:
                subscribers[subscriber].append([artist, mark])

        for subscriber, datas in subscribers.items():  # 將dict轉為文字
            message += f"{subscriber}："
            artists = list(map(lambda x: f"`{x[0]}`{x[1]}", datas))
            message += "、".join(artists) + "\n"

        try:  # 已有總覽
            overview = await self.bot.get_channel(self.config.overview_channel).fetch_message(
                self.config.overview_msg
            )
        except:  # 無總覽，發出總覽訊息
            msg = await self.bot.get_channel(self.config.overview_channel).send(message)
            await msg.pin()
            self.config.overview_msg = msg.id
            write_yaml("config", self.config, "subscribe")
        else:
            await overview.edit(content=message)

    async def changeData(self, ctx, query, message=None, send_msg: bool = True):
        try:
            SQL_modify(query)
        except Exception as e:
            await ctx.send(f"操作失敗, 原因：{e}", delete_after=5)
            await self.bot.get_channel(self.config.log_channel).send(
                f"{ctx.author.mention} 更改資料失敗， {e}"
            )
            return False
        else:
            await self.print_overview()
            if message:
                if send_msg:
                    await ctx.send(message)
                await self.bot.get_channel(self.config.log_channel).send(f"{message}")
            return True

    async def actionCheck(self, msg, author):
        await msg.add_reaction(Emoji.check)
        await msg.add_reaction(Emoji.cancel)

        def check(reaction, user):
            if reaction.message.id == msg.id and user == author:
                if str(reaction.emoji) == Emoji.check:
                    return True
                elif str(reaction.emoji) == Emoji.cancel:
                    raise ActionCancel

        try:
            await self.bot.wait_for("reaction_add", check=check)
        except:
            return False
        else:
            return True
        finally:
            await msg.delete()

    @cog_ext.cog_subcommand(
        base="manage",
        subcommand_group="subscriber",
        name="add",
        description="新增訂閱者，限管理員使用",
        guild_ids=guildID,
        options=[
            create_option(name="subscriber", description="新訂閱者", option_type=6, required=True),
            create_option(name="download_url", description="下載網址", option_type=3, required=True),
            create_option(name="preview_url", description="預覽網址", option_type=3, required=False),
        ],
    )
    async def new_subscriber(self, ctx, subscriber, download_url, preview_url=None):
        if self.managerCheck(ctx):
            await ctx.defer()
            subscriber = subscriber.mention.replace("!", "")
            if SQL_getData("subscribers", "subscriber", subscriber):
                await ctx.send(f"{subscriber} 已在訂閱者名單", hidden=True)
            else:
                download_url = download_url.replace(" ", "\n")
                if "\n" in download_url:
                    download_url = "\n" + download_url
                if preview_url is not None:  # 有預覽網址
                    if "\n" in preview_url:
                        preview_url = "\n" + preview_url
                    preview_url = preview_url.replace(" ", "\n")
                    query = f"""INSERT INTO subscribers(subscriber, preview_url, download_url)
                                VALUES("{subscriber}", "{preview_url}", "{download_url}")"""
                else:  # 無預覽網址
                    query = f"""INSERT INTO subscribers(subscriber, download_url)
                                VALUES("{subscriber}", "{download_url}")"""
                message = f"新訂閱者:{subscriber}(by {ctx.author.mention})"
                await self.changeData(ctx, query, message)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    @cog_ext.cog_subcommand(
        base="manage",
        subcommand_group="subscriber",
        name="delete",
        description="刪除訂閱者及其訂閱的繪師資料，限管理員使用",
        guild_ids=guildID,
        options=[
            create_option(name="subscriber", description="欲刪除的訂閱者", option_type=6, required=True)
        ],
    )
    async def delete_subscriber(self, ctx, subscriber):
        if self.managerCheck(ctx):
            await ctx.defer()
            subscriber = subscriber.mention.replace("!", "")
            if SQL_getData("subscribers", "subscriber", subscriber):
                artists = SQL_getData("artists", "subscriber", subscriber)
                message = f"請確認刪除 {subscriber} 的資料"
                if len(artists) != 0:
                    message += "，***以下繪師資料也將被刪除***："
                    for artist in artists:  # 列出目標訂閱的繪師
                        message += f"`{artist[0]}`"
                        if artist != artists[-1]:
                            message += "、"

                msg = await ctx.send(message)
                if await self.actionCheck(msg, ctx.author):
                    query = f'DELETE FROM `subscribers` WHERE `subscriber`="{subscriber}"'
                    message = f"訂閱紀錄：{ctx.author.mention} 刪除了 {subscriber} 的資料"
                    await self.changeData(ctx, query, message)
                else:
                    await ctx.send("刪除訂閱者資料取消", delete_after=5)

            else:
                await ctx.send(f"{subscriber} 不在訂閱者名單內", hidden=True)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    @cog_ext.cog_subcommand(
        base="manage",
        subcommand_group="artist",
        name="add",
        description="新增訂閱紀錄，限管理員使用",
        guild_ids=guildID,
        options=[
            create_option(name="subscriber", description="訂閱者", option_type=6, required=True),
            create_option(name="artist", description="繪師", option_type=3, required=True),
            create_option(name="mark", description="備註，將顯示於繪師名後方", option_type=3, required=False),
        ],
    )
    async def subscribe(self, ctx, subscriber, artist, mark=""):
        if self.managerCheck(ctx):
            subscriber = subscriber.mention.replace("!", "")
            if SQL_getData("artists", "artist", artist):
                await ctx.send(f"繪師 `{artist}` 已有訂閱紀錄", delete_after=5)  # 已訂閱繪師
            elif not SQL_getData("subscribers", "subscriber", subscriber):
                await ctx.send(f"{subscriber} 不在訂閱者名單內", delete_after=5)
            # 無此訂閱者
            else:
                msg = await ctx.send(f"請確認 {subscriber} 訂閱 `{artist}`")
                if not await self.actionCheck(msg, ctx.author):
                    await ctx.send("新增資料取消", delete_after=5)
                else:
                    lastUpdate = str(get_date())
                    if mark:
                        mark = f"({mark})"
                        query = f"""INSERT INTO `artists`(`artist`, `subscriber`, `lastUpdateTime`, `mark`)
                                    VALUES("{artist}", "{subscriber}", "{lastUpdate}", "{mark}")"""
                    else:
                        query = f'INSERT INTO `artists`(`artist`, `subscriber`, `lastUpdateTime`) VALUES("{artist}", "{subscriber}", "{lastUpdate}")'
                    message = f"訂閱紀錄：{subscriber} 訂閱了 `{artist}`(by{ctx.author.mention})"
                    await self.changeData(ctx, query, message)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    @cog_ext.cog_subcommand(
        base="manage",
        subcommand_group="artist",
        name="delete",
        description="取消訂閱，限管理員使用",
        guild_ids=guildID,
        options=[create_option(name="artist", description="繪師名", option_type=3, required=True)],
    )
    async def unsubscribe(self, ctx, artist):
        if self.managerCheck(ctx):
            artist = SQL_getData("artists", "artist", artist, 1)  # (artist, subscriber, ...)
            if artist:
                msg = await ctx.send(f"請確認 {artist[1]} 取消訂閱 `{artist[0]}`")
                if not await self.actionCheck(msg, ctx.author):
                    await ctx.send("刪除資料取消", delete_after=5)
                else:
                    query = f'DELETE FROM `artists` WHERE `artist`="{artist[0]}"'
                    message = f"訂閱紀錄：{artist[1]} 取消訂閱 `{artist[0]}`(by {ctx.author.mention})"
                    await self.changeData(ctx, query, message)
            else:
                await ctx.send(f"無人訂閱 {artist[0]}", delete_after=5)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    @cog_ext.cog_subcommand(
        base="manage",
        subcommand_group="artist",
        name="change_subscriber",
        description="更改訂閱者，限管理員使用",
        guild_ids=guildID,
        options=[
            create_option(name="artist", description="繪師名", option_type=3, required=True),
            create_option(name="newsubscriber", description="新訂閱者", option_type=6, required=True),
        ],
    )
    async def change_subscriber(self, ctx, artist, newsubscriber):
        if self.managerCheck(ctx):
            newsubscriber = newsubscriber.mention.replace("!", "")
            artist = SQL_getData("artists", "artist", artist, 1)
            if SQL_getData("subscribers", "subscriber", newsubscriber) and artist:
                if artist[1] == newsubscriber:  # 原訂閱者和新訂閱者相同
                    await ctx.send("原訂閱者和新訂閱者相同", delete_after=5)
                else:
                    msg = await ctx.send(f"請確認 `{artist[0]}` 由 {artist[1]} 改為 {newsubscriber} 訂閱")
                    if not await self.actionCheck(msg, ctx.author):
                        await ctx.send("更改訂閱者取消", delete_after=5)
                    else:
                        query = f'UPDATE `artists` SET `subscriber`="{newsubscriber}" WHERE `artist`="{artist[0]}"'
                        message = f"訂閱紀錄：{ctx.author.mention} 將 `{artist[0]}` 由 {artist[1]} 改為 {newsubscriber} 訂閱"
                        await self.changeData(ctx, query, message)
            else:
                await ctx.send("新訂閱者不在訂閱者名單內或繪師尚未被訂閱", delete_after=5)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    @cog_ext.cog_subcommand(
        base="subscribe",
        description="更新常態訂閱的繪師圖包",
        guild_ids=guildID,
        options=[
            create_option(
                name="artists",
                description='要更新的繪師名，可一次更新多個繪師，於繪師名之間加上","即可',
                option_type=3,
                required=True,
            ),
            create_option(
                name="timestamp",
                description="更新日期(mm-dd)，當日更新則不必輸入",
                option_type=3,
                required=False,
            ),
        ],
    )
    async def update(self, ctx, artists, timestamp=None):
        artists = artists.split(",")
        if timestamp is None:
            timestamp = str(get_date())
        else:
            timestamp = f"{get_date().year}-{timestamp}"

        try:
            date_valid(timestamp)
        except Exception as e:
            await ctx.send(e, hidden=True)
        else:
            for artist in artists:
                await ctx.defer()
                data = SQL_inquiry(
                    f'''SELECT `artists`.`artist`, `artists`.`subscriber`,
                        `subscribers`.`preview_url`, `subscribers`.`download_url`
                        FROM `artists` NATURAL JOIN `subscribers`
                        WHERE `artist`="{artist}"''',
                    1,
                )
                if data:  # [artist, subscriber, preview, download]
                    if self.authorCheck(ctx, data[1]):
                        query = f'UPDATE `artists` SET `lastUpdateTime`="{timestamp}", `status`=0 WHERE `artist`="{artist}"'
                        msg = f"{data[1]} 於 `{timestamp}` 更新了 `{artist}`"
                        if await self.changeData(ctx, query, msg, False):
                            await ctx.send(f"{msg} \n>>> 預覽：{data[2]}\n下載：{data[3]}")
                    else:
                        await ctx.send(f"你不是 `{artist}` 的訂閱者或頻道錯誤", delete_after=5)
                        break
                else:
                    await ctx.send(f"無`{artist}`此繪師的訂閱紀錄", delete_after=5)

    @cog_ext.cog_subcommand(
        base="subscribe",
        description="繪師本月無更新圖包",
        guild_ids=guildID,
        options=[
            create_option(
                name="artists",
                description='無更新的繪師名，可一次更新多個繪師，於各繪師名間加上","即可',
                option_type=3,
                required=True,
            )
        ],
    )
    async def noupdate(self, ctx, artists):
        artists = artists.split(",")
        for artist in artists:
            artist_data = SQL_getData("artists", "artist", artist, 1)
            if artist_data:
                if self.authorCheck(ctx, artist_data[1]):
                    query = f'UPDATE `artists` SET `lastUpdateTime`="{str(get_date())}", `status`=2 WHERE `artist`="{artist}"'
                    await self.changeData(ctx, query, f"{artist_data[1]}：`{artist}`本月沒有更新")
                else:
                    await ctx.send("沒有權限或頻道錯誤", hidden=True)
                    break
            else:
                await ctx.send(f"無 `{artist}` 此繪師的訂閱紀錄", delete_after=5)

    @cog_ext.cog_subcommand(
        base="subscribe",
        subcommand_group="url",
        name="edit",
        description="更改網址",
        guild_ids=guildID,
        options=[
            create_option(
                name="item",
                description="要更改的網址項目",
                option_type=3,
                required=True,
                choices=[
                    create_choice("preview_url", "預覽網址"),
                    create_choice("download_url", "下載網址"),
                ],
            ),
            create_option(name="url", description="新網址，空格將自動取代為換行", option_type=3, required=True),
            create_option(
                name="subscriber",
                description="更改網址的訂閱者，限管理員使用",
                option_type=6,
                required=False,
            ),
        ],
    )
    async def edit_url(self, ctx, item, url, subscriber: discord.Member = None):  # item:0->預覽，1->下載
        if subscriber is None:
            subscriber = ctx.author.mention.replace("!", "")
        else:
            subscriber = subscriber.mention.replace("!", "")

        if url == "None":
            url = None  # 刪除網址
        else:
            url = url.split(" ")
            url = "\n".join(url)
            if "\n" in url:
                url = "\n" + url

        if self.authorCheck(ctx, subscriber):
            if not SQL_getData("subscribers", "subscriber", subscriber, 1):
                await ctx.send(f"{subscriber} 不在訂閱者名單內", delete_after=5)
            else:
                query = (
                    f'UPDATE `subscribers` SET `{item}`="{url}" WHERE `subscriber`="{subscriber}"'
                )
                if await self.changeData(ctx, query):
                    await ctx.send("更改成功", hidden=True)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    @cog_ext.cog_subcommand(
        base="subscribe",
        subcommand_group="url",
        name="append",
        description="網址擴展(輸入的網址將加在原有的下一行)",
        guild_ids=guildID,
        options=[
            create_option(
                name="item",
                description="要更改的網址項目",
                option_type=3,
                required=True,
                choices=[
                    create_choice("preview_url", "預覽網址"),
                    create_choice("download_url", "下載網址"),
                ],
            ),
            create_option(name="url", description="新網址，空格將自動取代為換行", option_type=3, required=True),
            create_option(
                name="subscriber",
                description="更改網址的訂閱者，限管理員使用",
                option_type=6,
                required=False,
            ),
        ],
    )
    async def url_append(self, ctx, item, url, subscriber: discord.Member = None):
        if subscriber is None:
            subscriber = ctx.author.mention.replace("!", "")
        else:
            subscriber = subscriber.mention.replace("!", "")

        url = url.split(" ")
        url = "\n" + "\n".join(url)
        if self.authorCheck(ctx, subscriber):
            data = SQL_inquiry(
                f"SELECT `{item}` FROM `subscribers` WHERE `subscriber`={subscriber}", 1
            )
            if not data:
                await ctx.send(f"{subscriber} 不在訂閱者名單內", delete_after=5)
            else:
                url = data + url
                query = (
                    f'UPDATE `subscribers` SET `{item}`="{url}" WHERE `subscriber`="{subscriber}"'
                )
                if await self.changeData(ctx, query):
                    await ctx.send("更改成功", hidden=True)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    async def info(self, ctx, target, target_type):
        if self.channelCheck(ctx):
            if target_type == 0:  # 訂閱者
                query = f'''SELECT artists.artist, artists.mark, subscribers.preview_url, subscribers.download_url
                            FROM artists LEFT JOIN subscribers ON artists.subscriber=subscribers.subscriber
                            WHERE artists.subscriber = "{target}"'''
                data = SQL_inquiry(query)
                if data:
                    message = f"{target}：\n>>> 訂閱繪師："

                    if len(data) == 0:
                        message += "無"  # 無訂閱繪師
                    else:
                        artists = list(map(lambda x: f"`{x[0]}`{x[1]}", data))
                        message += "、".join(artists)
                    message += f"\n預覽：{data[0][2]}\n下載：{data[0][3]}"
                    await ctx.send(message, hidden=True)
                else:
                    await ctx.send("無此訂閱者或該訂閱者沒訂閱任何繪師", hidden=True)

            elif target_type == 1:  # 繪師
                query = f'''SELECT artists.subscriber, artists.lastUpdateTime, artists.mark, artists.status,
                            subscribers.preview_url, subscribers.download_url
                            FROM artists LEFT JOIN subscribers ON artists.subscriber=subscribers.subscriber
                            WHERE artists.artist = "{target}"'''
                data = SQL_inquiry(query, 1)
                if data:
                    subscriber, update_time, mark, status, preview, download = data
                    message = f"`{target}`{mark}：\n>>> 訂閱者： {subscriber}\n更新狀態："

                    if status == 1:
                        message += "新增訂閱資料後未更新\n"
                    elif get_date() - update_time >= datetime.timedelta(days=30):
                        message += f"本月尚未更新，上次更新日期為 `{update_time}`\n"
                    elif status == 0:
                        message += f"本月(`{update_time}`)已更新\n"
                    elif status == 2:
                        message += "本月繪師停更\n"
                    message += f"預覽：{preview}\n下載：{download}"

                    await ctx.send(message, hidden=True)
                else:
                    await ctx.send("無人訂閱此繪師", delete_after=5)
        else:
            await ctx.send("頻道錯誤", delete_after=5)

    @cog_ext.cog_subcommand(
        base="subscribe",
        subcommand_group="info",
        name="artist",
        description="查詢繪師資料",
        guild_ids=guildID,
    )
    async def info_artist(self, ctx, artist):
        await self.info(ctx, artist, 1)

    @cog_ext.cog_subcommand(
        base="subscribe",
        subcommand_group="info",
        name="subscriber",
        description="查詢訂閱者資料",
        guild_ids=guildID,
    )
    async def info_subscriber(self, ctx, subscriber: discord.Member):
        subscriber = subscriber.mention.replace("!", "")
        await self.info(ctx, subscriber, 0)

    @cog_ext.cog_subcommand(base="manage", description="檢查超過30天未更新的訂閱者，管理員用", guild_ids=guildID)
    async def check(self, ctx):
        if self.managerCheck(ctx):
            limitDate = get_date() - datetime.timedelta(days=30)  # 30天前的日期
            query = f'SELECT artist, subscriber, status, lastUpdateTime FROM `artists` WHERE `lastUpdateTime` < "{limitDate}" ORDER BY `subscriber`, `lastUpdateTime`'  # 查詢上次更新日期小於30天前日期的繪師
            nonupdateArtists = SQL_inquiry(query)
            message = "超過(含)30天未更新：\n>>> "
            if nonupdateArtists:  # 有未更新的繪師

                subscribers = {}
                for (
                    artist,
                    subscriber,
                    status,
                    lastUpdateTime,
                ) in nonupdateArtists:  # 將繪師及其訂閱者整理為dict
                    if status == 1:
                        lastUpdateTime = "新增訂閱資料後未更新"
                    else:
                        lastUpdateTime = lastUpdateTime.strftime("%m-%d")
                    data = [artist, lastUpdateTime]

                    if subscriber not in subscribers.keys():
                        subscribers[subscriber] = [data]
                    else:
                        subscribers[subscriber].append(data)

                for subscriber, datas in subscribers.items():  # 轉為要顯示的文字
                    message += f"{subscriber}："
                    for artist, lastUpdate in datas:
                        message += f"`{artist}`（{lastUpdate}）"
                        if artist != datas[-1][0]:
                            message += "、"
                    message += "\n"
            else:
                message += "無"
            await ctx.send(message)
            await ctx.send(
                "若已更新但還是在清單中，請確認更新時使用指令`+update 繪師 日期（mm-dd）`或告知管理者更新日期，繪師無更新請使用`+noupdate 繪師`"
            )

    @cog_ext.cog_subcommand(
        base="subscribe",
        description="上傳非常態訂閱的圖包",
        guild_ids=guildID,
        options=[
            create_option(name="artist", description="圖包作者", option_type=3, required=False),
            create_option(
                name="subscriber",
                description="上傳的訂閱者，限管理員使用",
                option_type=6,
                required=False,
            ),
        ],
    )
    async def upload(self, ctx, artist="", subscriber=""):
        if subscriber != "":
            subscriber = subscriber.mention.replace("!", "")  # 有指定訂閱者
        else:
            subscriber = ctx.author.mention.replace("!", "")

        if self.authorCheck(ctx, subscriber):
            subscriber = SQL_getData("subscribers", "subscriber", subscriber, 1)
            if subscriber:
                if not artist:
                    await ctx.send(f"{subscriber[0]} 上傳了圖包\n>>> 下載網址：\n{subscriber[2]}")  # 有填寫繪師名稱
                else:
                    await ctx.send(
                        f"{subscriber[0]} 上傳了 `{artist}` 的圖包\n>>> 下載網址：\n{subscriber[2]}"
                    )
            else:
                await ctx.send("訂閱者名單中沒有 {subscriber[0]} 這個人", delete_after=3)
        else:
            await ctx.send("沒有權限或頻道錯誤", hidden=True)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.id == self.config.overview_msg:
            self.config.overview_msg = 0
            write_yaml("config", self.config, "subscribe")

    @commands.command(hidden=True)
    async def overview(self, ctx):
        await ctx.message.delete()
        if await self.bot.is_owner(ctx.author):
            await self.print_overview()


def setup(bot):
    bot.add_cog(SUBSCRIBE(bot))
