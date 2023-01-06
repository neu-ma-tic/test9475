from __future__ import annotations

import discord
from discord import app_commands, Interaction
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from bot import ValorantBot

def self_bot(interaction: discord.Interaction) -> ValorantBot:
    bot: ValorantBot = getattr(interaction, "client", interaction._state._get_client())
    return bot

def owner_only() -> app_commands.check:
    """ Checks if the user is the owner of the bot. """
    async def predicate(interaction: Interaction):
        return await interaction.client.is_owner(interaction.user)
    return app_commands.check(predicate)

def cooldown_5s(interaction: discord.Interaction) -> Optional[app_commands.Cooldown]: 
    """
    Example cooldown:

        from discord.app_commands.checks import dynamic_cooldown
        from utils.checks import cooldown_10s, cooldown_5s

        @app_commands.command()
        @dynamic_cooldown(cooldown_5s)
        async def hello(self, interaction):
            print("Hello")
    """
    
    bot = self_bot(interaction)
    if interaction.user.id == bot.owner_id:
        return None
    return app_commands.Cooldown(1, 5)