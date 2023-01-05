import discord


class arrows(discord.ui.View):

    
    @discord.ui.button(emoji=':arrow_right: ', style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.edit_message(embed=i[-1])
    






