# Ce code est un exemple.










import discord
from discord.ext import commands

#\ Tout les "import" :
import random
import urllib
import urllib.request
import smtplib
#/ Fin des "import"

__version__ = "1.2.3.6"

bot = commands.Bot(command_prefix="/")
client = discord.Client()

def verify_connexion () :
    host = "http://google.com"
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def send_email (destinataire, object_du_mail, texte_du_mail) :   
    if verify_connexion() : 
        envoyeur = "Py-Send-Pro@outlook.com"
        password = "Zg>}dru$f<bVsS'#]IjE>,!I$P{]YtaIT49}_5"
        texte_du_mail = texte_du_mail + "\n\n\n\n\n\n\n[[Envoyé depuis Alto " + __version__ + "]]"

        msg = MIMEMultipart()
        msg["From"] = envoyeur
        msg["To"] = destinataire
        msg["Subject"] = object_du_mail

        msg.attach(MIMEText(texte_du_mail, "plain"))

        try :
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.ehlo()
            server.starttls()
            server.login("Py-Send-Pro@outlook.com", password)
            text = msg.as_string()
            server.sendmail(envoyeur, destinataire, text)
            server.quit()
            return True
        except :
            return False
    elif not verify_connexion() : 
        print ("[pas d'internet]")
        return False

@bot.event
async def on_ready():
    print("Je me suis connecté en {0.user}".format(bot) + ".")
    # game = discord.Game("I am looking to you.")
    # await client.change_presence(status=discord.Status.idle, activity=game)


# @bot.command(name="roll_dice", help="Simulates rolling dice. (temporaire)")
# async def roll(ctx, number_of_dice: int, number_of_sides: int):
#     dice = [
#         str(random.choice(range(1, number_of_sides + 1)))
#         for _ in range(number_of_dice)
#     ]
#     await ctx.send(', '.join(dice))

@bot.command(name="rep", help="Répond à votre question.")
async def rep(ctx):
    answer = ["Comme je le voit, oui.", "Je n'ai pas envie de te répondre.", "Concentre toi et demande moi à nouveau.", "Mes sources disent que non.", "Je ne peut pas le prédire maintenant.", "Essaye encore.", "Vous pouvez compter sur lui.", "Oui, définitivement.", "Certainement.", "Absolument.", "Certainement pas.", "Je ne te répondrait sûrement pas !", "Sans aucun doute.", "Mes sources me disent que non.", "Il serait temps d'arrêter.", "Je suis bien d'accord avec toi.", "…", "C'est une idée de génie !!!", "Toujours !", "Jamais !", "Moi, :gem:Forestia:gem:, ferai toujours mon possible pour vous aider.", "Concentre toi et réessaye."]
    len_answer = len(answer)
    r = random.randint(1, len_answer)
    await ctx.send(answer[r])

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Merci d'entrer tous les arguments demandés : \n/help")

@bot.command(name="random", help="(minimum) (maximum)")
async def random(ctx, mini: int, maxi: int):
    n = random.randint(mini, maxi)
    await ctx.send(n)

# @bot.command(name="e-mail", help="(destinataire) (Texte du mail)")
# async def e_mail(ctx, to: str, text: str):
# 	envoyé = send_email(to, "Message du bot Alto", text)
# 	if envoyé == True :
# 		await ctx.send("Message envoyé !")
# 		pass





bot.run("Nzk4MjgwODA0OTE5OTM1MDI1.X_yu7w.NioEFcwdMv37GIe-TNpF_Hp1w1g")
