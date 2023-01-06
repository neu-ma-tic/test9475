import discord, os, json
from discord.ext import commands
from discord import B

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

if os.path.isfile("data.json"):
    with open("data.json", encoding="utf-8") as file:
        data = json.load(file)
else:
    data = {"Geschenke": []}
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def dump():
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


@bot.command(name="add")
async def add(ctx, *, text=None):
    if text == None:
        await ctx.reply("Du musst ein Geschenk angeben")
        return
    gb = {"Name": ctx.author.name, "Text": text}
    data["Geschenke"].append(gb)
    dump()
    await ctx.reply(
        "Dein Geschenk wurde hinzugefügt und kann nicht mehr entfernt werden!")


@bot.command(name="reveal")
async def reveal(ctx):
    embed = discord.Embed(title="Deine Geschenke Waffel",
                          color=discord.Color.random())
    components = [
        ActionRow(
            Button(label="-->Button<--",
                   custom_id="button_one",
                   style=ButtonStyle.blurple))
    ]
    main_msg = await ctx.send(embed=embed, components=components)

    def check_button(i: discord.Interaction, button):
        return i.author == ctx.author and i.message == main_msg

    interaction, button = await bot.wait_for('button_click',
                                             check=check_button)

    if button.custom_id == "button_one":
        embed_2 = discord.Embed(title="Deine Geschenke sind:",
                                color=discord.Colour.random())
        for i in data["Geschenke"]:
            name = i["Name"]
            geschenk = i["Text"]
            embed_2.add_field(name=f"Geschenk von {name}", value=geschenk)

        await ctx.send(embed=embed_2)


@bot.event
async def on_ready():
    print("Im Logged in")
    await bot.change_presence(
        activity=discord.Game("Waffels Geburtstag durch!"))


bot.run(
    "OTgyMDA4Nzk0NTEzMDM1Mzk0.GeNuom.f-TfGc8TC3hAplxg0wNl9uThuQV06Y02hU0zf8")
