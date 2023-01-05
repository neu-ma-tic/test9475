import discord

TOKEN = "ODU0NjA3ODU1MTM1MjI3OTA0.YMmZlg.4BGjw8csCVnjIxeZlsOuuNwnRy8"

client = discord.client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".ping"):
        await message.channel.send("pong")


@client.event
async def on_ready():
    print("running")
client.run(TOKEN)
print(client.user.name)