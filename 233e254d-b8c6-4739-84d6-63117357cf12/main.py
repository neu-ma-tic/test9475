import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import time

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person / bot!"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="Bing Bong"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragment(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$abyss"):
        character = msg.split("$abyss ", 1)[1]
        buildlink = "Build Link Incoming"
        if character.lower() == "raiden":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1o10231c1o2ep21128031wbStaffOfHoma2hp11124atk_2253atki1110_932583083978789a00N05uk0148R19m12L1ar2p5xk0349V11Y7aS0822pdxk084aR12L03U01y6plxk0g45l01q8902ac2ptxk0943j05c18Q0aY1pB1bStaffOfHomapN0e"
        elif character.lower() == "benny":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1410241a1g141411131c141q11134atk_2253atki1110_9325830839787aburst_dmg_22466a00R05xk0149r03R0ac28E155xk0347j0aq39616Y15d1k0446323B08K1a235lxk0j43x09z08y25D05txk0948l22L15D07g05B1cSkywardBlade5N0e"
        elif character.lower() == "xiangling":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1r12131wbStaffOfHoma2hp11134atk_2253atki1110_9325830839787aburst_dmg_22488a05S059k0147j0aL45g09S0s56k0345B0ak26329t1sd9k0448Q05g09s23z0sl6k0j43j07411d42F2stak094a_47n08J01H4sB1bStaffOfHomasN0e"
        elif character.lower() == "xingqiu":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1s11131wgSacrificialSword1r11134atk_2253atki1110_9325830839787aburst_dmg_22439905S05gk0149F17l08E2ak2t5gk0341H45B09-0ai3tduk044aY19W08R16Y1tl9k0i44t16Y1711ak2ttuk094a233g01u77E0tB1gSacrificialSwordtQ0e"
        elif character.lower() == "ayaka":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1z20241a1314142111f29resonance2si11159critRate_2154dmg_2608moveSPD_210bstaminaDec_210ecryo_enemyRes_3-3088960M053k014ac23e08l26i2A53k0341m95Y0921a42Ad3k0445n0ag49a13e0Alek0e44z12i2ae11q8At3k0a41m94z13L0921AB1dAquilaFavoniaAN0e"
        elif character.lower() == "mona":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1g10131c1g1q11144dmg_2608moveSPD_210bstaminaDec_210ecryo_enemyRes_3-3017a05M04ek0144i2aY19J18J0h59k0345U0aq38J04t1hd4k0i4a-09823x01q8httk094aX25l04z13U0hB1aTheWidsithhR0e"
        elif character.lower() == "venti":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1p10141a1t14142114cryo44dmg_2608moveSPD_210bstaminaDec_210ecryo_enemyRes_3-3028800E05tk014ac28R14o25l0q5tk0345n07d18W0ac2qdtk074ac25z01d48r2qlxk0745U08R14n11U8qttk0741L39z06c35U0qB1bSkywardHarpqN0e"
        elif character.lower() == "diona":
            buildlink = "Here's the link for " + character.capitalize(
            ) + ": https://frzyc.github.io/genshin-optimizer/#/flex?v=4&d=1710131c172a111148moveSPD_210bstaminaDec_2104dmg_260ecryo_enemyRes_3-3015500K05ak014aS02638r13r085uk0345g0262aq39z08d6k024ai31U88E14z18lek0241Qg6213x0ae18tek0b48W06J11db9-08B1eSacrificialBow8Jae"
        else:
            buildlink = "That character couldn't be found dumbass"
        await message.channel.send(buildlink)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

    if msg.startswith("$gamerecord"):
        await message.channel.send("https://www.hoyolab.com/genshin/")


keep_alive()

client.run(os.getenv("TOKEN"))
