import discord
from core import CogInit, Config, Emoji
from discord.ext import commands


class CLEAN(CogInit):
    @commands.command(usage="+clean <最大數量>", help="清理bot的訊息")
    async def clean(self, ctx, limit: int = 999, target="<@719120395571298336>"):
        target = int(target.replace("!", "")[2:-1])

        def judge(msg: discord.Message) -> bool:
            return msg.author.id == target

        if target == Config.bot_id or ctx.author.id in Config.managers:
            await ctx.message.delete()
            count = len(await ctx.channel.purge(check=judge, limit=limit))
            await ctx.send(f"清除了 {(count)} 條訊息", delete_after=5)
        else:
            await ctx.send("You don't have permission or target is not a user.", delete_after=3)
            await ctx.message.delete()

    @commands.command(hidden=True)
    async def clean_channel(self, ctx):
        def check(reaction, user):
            if user == ctx.author and reaction.message.id == msg.id:
                return str(reaction.emoji) == Emoji.check

        if await self.bot.is_owner(ctx.author):
            await ctx.message.delete()
            msg = await ctx.send("確定刪除此頻道的所有訊息?", delete_after=6)
            await msg.add_reaction(Emoji.check)
            try:
                await self.bot.wait_for("reaction_add", timeout=5, check=check)
            except:
                await ctx.send("超出時間，指令取消", delete_after=3)
            else:

                def check(message: discord.Message):
                    return not message.pinned

                count = len(await ctx.channel.purge(check=check, limit=None))
                await ctx.send(f"清除了 {(count)} 條訊息", delete_after=5)
        else:
            await ctx.message.delete()
            await ctx.send(
                "You don't have permission or you are not in the target channel.", delete_after=3
            )


def setup(bot):
    bot.add_cog(CLEAN(bot))
