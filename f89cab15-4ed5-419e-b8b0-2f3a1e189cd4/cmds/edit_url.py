from core import CogInit, readFile, writeFile
from discord.ext import commands

urls = readFile("others")
authorId = readFile("setting")["authorId"]


class EDIT_URL(CogInit):
    @commands.command(hidden=True, usage="+add_url 分類 網址 <權重>")
    async def add_url(self, cxt, item, url, weight: int = 1):
        if cxt.author.id == authorId:
            if item in urls.keys():
                if url in urls[item].keys():
                    await cxt.send("此圖已在檔案中", delete_after=3)
                else:
                    try:
                        newurl = {url: weight}
                        urls[item].update(newurl)
                    except:
                        await cxt.send("新增失敗", delete_after=3)
                    else:
                        await cxt.send("新增完畢", delete_after=3)
            else:
                try:
                    newitem = {item: {url: weight}}
                    urls.update(newitem)
                except:
                    await cxt.send("新增失敗", delete_after=3)
                else:
                    await cxt.send("新增完畢", delete_after=3)
            writeFile("others", urls)
        await cxt.message.delete()

    @commands.command(hidden=True, usage="+del_url 分類 <網址>")
    async def del_url(self, cxt, item, url=""):
        if cxt.author.id == authorId:
            if url == "":
                try:
                    del urls[item]
                except:
                    await cxt.send("刪除失敗", delete_after=3)
                else:
                    await cxt.send("刪除成功", delete_after=3)
                    writeFile("others", urls)
            else:
                try:
                    del urls[item][url]
                except:
                    await cxt.send("刪除失敗", delete_after=3)
                else:
                    await cxt.send("刪除成功", delete_after=3)
                    writeFile("others", urls)
        await cxt.message.delete()

    @commands.command(hidden=True, usage="+edit_weight 分類 網址 權重")
    async def edit_url(self, ctx, item, url, weight: int):
        if ctx.author.id == authorId:
            try:
                urls[item][url] = weight
            except Exception as e:
                await ctx.send("更改失敗", delete_after=3)
                print(e, "\n")
            else:
                await ctx.send("更改成功", delete_after=3)
                writeFile("others", urls)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(EDIT_URL(bot))
