from core import CogInit
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


class BASIC(CogInit):
    @cog_ext.cog_subcommand(
        base="extension",
        options=[
            create_option(
                "folder",
                "分類資料夾",
                3,
                True,
                choices=[
                    create_choice("cmds", "cmds"),
                    create_choice("events", "events"),
                    create_choice("games", "games"),
                ],
            ),
            create_option("extension", "extension", 3, True),
        ],
    )
    async def load(self, ctx, folder, extension):
        if await self.bot.is_owner(ctx.author):
            try:
                self.bot.load_extension(f"{folder}.{extension}")
            except commands.ExtensionAlreadyLoaded:
                try:
                    self.bot.reload_extension(f"{folder}.{extension}")
                except Exception as e:
                    raise e
                else:
                    await ctx.send(f"> **{extension}** has been reloaded.", delete_after=3)
            except Exception as e:
                raise e
            else:
                await ctx.send(f"> **{extension}** has been loaded.", delete_after=3)
        else:
            await ctx.send("請不要冒充作者", delete_after=3)

    @cog_ext.cog_subcommand(
        base="extension",
        options=[
            create_option(
                "folder",
                "分類資料夾",
                3,
                True,
                choices=[
                    create_choice("cmds", "cmds"),
                    create_choice("events", "events"),
                    create_choice("games", "games"),
                ],
            ),
            create_option("extension", "extension", 3, True),
        ],
    )
    async def unload(self, ctx, folder, extension):
        if await self.bot.is_owner(ctx.author):
            try:
                self.bot.unload_extension(f"{folder}.{extension}")
            except Exception as e:
                await ctx.send(f"Something went wrong, exception:***{e}***", hiddne=True)
                print(e)
                print()
            else:
                await ctx.send(f"> **{extension}** has been unloaded.", delete_after=3)
        else:
            await ctx.send("請不要冒充作者", delete_after=3)


def setup(bot):
    bot.add_cog(BASIC(bot))
