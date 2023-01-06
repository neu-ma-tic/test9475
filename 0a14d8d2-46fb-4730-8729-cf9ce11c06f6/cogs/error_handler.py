from __future__ import annotations

import discord
import traceback
from discord import Interaction
from discord.ext import commands
from discord.app_commands import (
    AppCommandError,
    CommandInvokeError,
    CommandNotFound,
    MissingPermissions,
    BotMissingPermissions,
    CommandOnCooldown
)
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from bot import ValorantBot

app_cmd_scope = 'https://cdn.discordapp.com/attachments/934041100048535563/979410875226128404/applications.commands.png'

class ErrorHandler(commands.Cog):
    """Error handler"""

    def __init__(self, bot: ValorantBot) -> None:
        self.bot: ValorantBot = bot
        bot.tree.on_error = self.on_app_command_error
    
    async def on_app_command_error(self, interaction: Interaction, error: AppCommandError):
        """ Handles errors for all application commands."""

        if self.bot.debug is True:
            traceback.print_exception(type(error), error, error.__traceback__)

        if isinstance(error, CommandInvokeError):
            error = error.original
        elif isinstance(error, CommandOnCooldown):
            error = error
        elif isinstance(error, Union[CommandNotFound, MissingPermissions, BotMissingPermissions]):
            error = error
        else:
            error = f"An unknown error occurred, sorry"
            traceback.print_exception(type(error), error, error.__traceback__)
        
        embed = discord.Embed(description=f'{str(error)[:2000]}', color=0xfe676e)
        if interaction.response.is_done():
            return await interaction.followup.send(embed=embed, ephemeral=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        embed = discord.Embed(color=0xfe676e)
        
        if isinstance(error, commands.CheckFailure):
            cm_error = "Only owners can run this command!"
        elif isinstance(error, commands.MissingRequiredArgument):
            cm_error = f"You didn't pass a required argument!"
            if ctx.command.name in ['sync', 'unsync']:
                cm_error = f"You need to specify a sync type: `guild` or `global`"
        elif hasattr(error, "original"):
            if isinstance(error.original, discord.Forbidden):
                cm_error = f"Bot don't have permission to run this command."
                if ctx.command.name in ['sync', 'unsync']:
                    cm_error = f"Bot don't have permission `applications.commands` to sync."
                    embed.set_image(url=app_cmd_scope)    
            elif isinstance(error.original, discord.HTTPException):
                cm_error = f"An error occurred while processing your request."
        elif isinstance(error, commands.BadLiteralArgument):
            cm_error = f"**Invalid literal:** {', '.join(error.literals)}"
        else:
            traceback.print_exception(type(error), error, error.__traceback__)
            cm_error = f"An unknown error occurred, sorry"

        embed.description = cm_error
        await ctx.send(embed=embed, delete_after=30, ephemeral=True)

async def setup(bot: ValorantBot) -> None:
    await bot.add_cog(ErrorHandler(bot))