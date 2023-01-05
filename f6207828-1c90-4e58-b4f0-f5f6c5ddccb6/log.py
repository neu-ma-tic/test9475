import discord
from discord.ext import commands
from datetime import datetime
import aiohttp
from io import BytesIO
from PIL import Image


class Logs(commands.Cog, name="Logs"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        logs = self.bot.get_channel(709374789424513028)  # <-- Insert the channel you want it logged to channel instead

        if message.author == self.bot.user:

            return

        elif message.author.bot:

            return

        elif message.attachments:

            async with aiohttp.ClientSession() as session:
                async with session.get(message.attachments[0].url) as response:
                    image_bytes = await response.read()

            with Image.open(BytesIO(image_bytes)) as my_image:

                if my_image.mode in ("RGBA", "P"):
                    my_image = my_image.convert("RGB")

                rotated = my_image.rotate(0, expand=True)
                buffer = BytesIO()
                rotated.save(buffer, "jpeg", optimize=True)
                buffer.seek(0)

            embed = discord.Embed(
                description=f"Image sent by <@{message.author.id}> in {message.channel} from {message.guild}:",
                color=0xff0000, timestamp=datetime.utcnow())
            embed.set_footer(text="Message ID: " + str(message.id), icon_url=message.author.avatar_url)
            file = discord.File(fp=buffer, filename="image.jpg")
            embed.set_image(url="attachment://image.jpg")

            await logs.send(file=file, embed=embed)

        elif message:

            embed = discord.Embed(
                description=f"Message sent by <@{message.author.id}> in {message.channel} from {message.guild}: \n\n{message.content}",
                color=0x4797b1, timestamp=datetime.utcnow())
            embed.set_footer(text="Message ID: " + str(message.id), icon_url=message.author.avatar_url)
            await logs.send(embed=embed)


def setup(bot):
    bot.add_cog(Logs(bot))
