import discord
import os

from keepAlive import keepAlive
from dotenv import load_dotenv
from discord.ext import tasks, commands
from getData import getValue, getDate

load_dotenv()
TOKEN = os.getenv('ACCESS_TOKEN')


bot = commands.Bot(command_prefix='!')


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.counter = 0
        self.bot = bot

        self.count_1 = False  # 5k
        self.count_2 = False  # 15k
        self.count_3 = False  # 25k
        self.count_4 = False  # 50k

        self.roleID = 863151327105515520

        self.getCount.start()
        self.verifyCount.start()

    @tasks.loop(seconds=90)
    async def getCount(self):
        self.counter = getValue()

    @tasks.loop(seconds=90)
    async def verifyCount(self):
        channel = self.bot.get_channel(859435816765358110)

        if self.counter >= 125000 and self.counter <= 150000:
            self.count_1 = False
            self.count_2 = False
            self.count_3 = False
            self.count_4 = False
        elif self.count_4 == False and self.counter <= 50000:
            await channel.send(f'<@&{self.roleID}> {self.counter:,} Kills Left')
            self.count_4 = True
        elif self.count_3 == False and self.counter <= 25000:
            await channel.send(f'<@&{self.roleID}> {self.counter:,} Kills Left')
            self.count_3 = True
        elif self.count_2 == False and self.counter <= 15000:
            await channel.send(f'<@&{self.roleID}> {self.counter:,} Kills Left')
            self.count_2 = True
        elif self.count_1 == False and self.counter <= 5.000:
            await channel.send(f'<@&{self.roleID}> {self.counter:,} Kills Left')
            self.count_1 = True
        else:
            pass

    @verifyCount.before_loop
    async def before_verifyCount(self):
        print('Aguardando a Inicialização do Sistema...')
        await self.bot.wait_until_ready()

    @getCount.before_loop
    async def before_getCount(self):
        print('Aguardando a Inicialização do Sistema...')
        await self.bot.wait_until_ready()


@bot.event
async def on_ready():
    print(f'Iniciado em {getDate()}')
    print(f'Conectou-se ao Discord!')
    print(f'Usuário: {bot.user.name}')
    print(f'ID: {bot.user.id}')

    MyCog(bot)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'Aguarde {error.retry_after} segundos, para utilizar o comando novamente')


@bot.command(name='worldboss', aliases=['wb', 'wbcount'])
@commands.cooldown(rate=1, per=60)
async def worldboss(ctx):
    counter = getValue()

    await ctx.send(f'{counter:,} Kills Left')


@bot.command(pass_context=True)
async def joinwbnotifications(ctx):
    member = ctx.message.author
    server = ctx.message.guild
    role = discord.utils.get(server.roles, name="wbnotify")
    await member.add_roles(role)
    await ctx.send('Cargo adicionado com sucesso!')

if __name__ == '__main__':
    keepAlive()
    bot.run(TOKEN)
