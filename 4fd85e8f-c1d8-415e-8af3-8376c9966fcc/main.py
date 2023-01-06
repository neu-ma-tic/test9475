import discord
class BotClient(discord.Client):

    names = ("Mattis", "Robin", "René", "Milan", "Leon", "Tyler")

    embed_error = discord.Embed(
        title = "Fehler", 
        description = "Sprich Deutsch du Hurensohn", 
        color = 0xff0000
    )

    embed_wrong_name = discord.Embed(
        title = "Fehler", 
        description = "Schreib den Namen richtig du Hurensohn", 
        color = 0xff0000
    )


    async def on_ready(self):
        print("Eingeloggt")


    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith("zitiere"):
            args = message.content.split(" ")[1:]
            if len(args) < 2:
                await message.channel.send(embed = self.embed_error, delete_after = 5)
            elif args[0] not in self.names:
                await message.channel.send(embed = self.embed_wrong_name, delete_after = 5)
            else:
                await message.channel.send(embed = discord.Embed(title = args[0], description = " ".join(args[1:]), color = 0x00ff0d))

        await message.delete()

    def new_method(self, args):
        print(len(args))
            


client = BotClient()
client.run("ODc0NjA4NDE1MzU4NDUxNzYy.YRJcjw.cuQAqv7eaT95laPRJO42Kleig3o")