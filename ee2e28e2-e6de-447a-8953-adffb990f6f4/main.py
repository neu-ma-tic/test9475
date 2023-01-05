from replit import db
import discord
from discord.utils import escape_mentions
from pytz import timezone
from discord.ext import commands, tasks
from discord.app.commands import Option, option

from typing import Dict
import json
import os
from datetime import datetime
from itertools import cycle

from datetime import datetime, timedelta
from time import sleep
import threading
import asyncio
import keep_alive
import pytz

country_time_zone = pytz.timezone("Brazil/West")
client = commands.Bot(command_prefix='!', intents=discord.Intents.all(),help_command=None)
guild_ids = [int(os.environ['SERVER_ID'])]

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def clear_db(ctx):
    for key in db.keys():
        del db[key]
    await ctx.send("**Banco de dados limpado**")

@client.command()
async def see_db(ctx):
    for key in db.keys():
        await ctx.send(f"`{key}` = `{db[key]}`")

@client.command()
async def tutorial(ctx):
    embed = discord.Embed(title="__Tutorial__", colour = ctx.author.colour,
    description="""\n\n
    __Trabalhos__

    **Para adicionar um trabalho é necessário que a matéria tenha uma sigla cadastrada.**
    ```
1  Adicionar uma sigla - !add_sigla\n

2  Adicionar atividade - !add_work\n

3  Lista com todas as atividades - !see_works

Para ver os argumentos do comando digite !help <nome_do_comando>
    ```
    """)
    await ctx.send(embed=embed)

"""
tasks.loop(count=1)
async def send_message(ctx, date):
    now = datetime.now().replace(microsecond=0)
    while str(now) != str(date):
        now = datetime.now().replace(microsecond=0)
        print(f"agora: {now} próxima data: {date}")
        await asyncio.sleep(1)
    await ctx.send("hora da guerra")


@client.command()
async def add_war(ctx, date):
    #war_date = (datetime.strptime(date, '%d/%m/%y %H:%M:%S') - timedelta(hours=0))
    war_date = datetime.now().replace(microsecond=0)
    await ctx.send(f"A data da próxima guerra foi definida para {war_date}")
    send_message.start(ctx, war_date)

"""



@client.command()
async def help(ctx, *, cmd: str =  None):
    """ Shows some information about commands and categories. 
    :param cmd: The command/category. """

    if not cmd:
        embed = discord.Embed(
            title="All commands and categories",
            description=f"```ini\nUse {client.command_prefix}help command or {client.command_prefix}help category to know more about a specific command or category\n\n[Examples]\n[1] Category: {client.command_prefix}help Works\n[2] Command : {client.command_prefix}help ping```",
            timestamp=ctx.message.created_at,
            color=ctx.author.color
            )

        for cog in client.cogs:
            cog = client.get_cog(cog)
            cog_commands = [c for c in cog.__cog_commands__ if hasattr(c, 'parent') and c.parent is None]
            commands = [f"{client.command_prefix}{c.name}" for c in cog_commands if not c.hidden]
            if commands:
                embed.add_field(
                    name=f"__{cog.qualified_name}__",
                    value=f"`Commands:` {', '.join(commands)}",
                    inline=False
                    )

        cmds = []
        for y in client.walk_commands():
            if not y.cog_name and not y.hidden:
                cmds.append(f"{client.command_prefix}{y.name}")

        embed.add_field(
            name='__Uncategorized Commands__',
            value=f"`Commands:` {', '.join(cmds)}",
            inline=False)
        await ctx.send(embed=embed)

    else:  
        cmd = escape_mentions(cmd)
        if command := client.get_command(cmd.lower()):
            command_embed = discord.Embed(title=f"__Command:__ {client.command_prefix}{command.qualified_name}", description=f"__**Description:**__\n", color=ctx.author.color, timestamp=ctx.message.created_at)
            return await ctx.send(embed=command_embed)

        # Checks if it's a cog
        for cog in client.cogs:
            if str(cog).lower() == str(cmd).lower():
                cog = client.get_cog(cog)
                cog_embed = discord.Embed(title=f"__Cog:__ {cog.qualified_name}", description=f"__**Description:**__\n```{cog.description}```", color=ctx.author.color, timestamp=ctx.message.created_at)
                cog_commands = [c for c in cog.__cog_commands__ if hasattr(c, 'parent') and c.parent is None]
                for c in cog_commands:
                    if not c.hidden:
                        cog_embed.add_field(name=c.qualified_name, value=c.help, inline=False)

                return await ctx.send(embed=cog_embed)
        # Otherwise, it's an invalid parameter (Not found)
        else:
            await ctx.send(f"**Invalid parameter! It is neither a command nor a cog!**")




### Work Slash commands ###
_work = client.command_group(name='trabalhos', description="For copy and pasting stuff.", guild_ids=guild_ids)
@_work.command(name="add", guild_ids=guild_ids)
@option(type=str, name="sigla", description="A sigla da disciplina.", required=True)
@option(type=str, name="data", description="O dia final da tarefa.", required=True)
@option(type=str, name="nome", description="The description of the giveaway.", required=True)
@option(type=str, name="link", description="Link para a atividade", required=False, default=' ')
async def _work_add_slash(ctx, sigla: str, data: str, nome: str, link: str) -> None:
    await client.get_cog("Works")._work_add_callback(ctx=ctx, acronym=sigla, date_limit=data, name=nome, link=link)

@_work.command(name="ver", guild_ids=guild_ids)
async def _work_see_slash(ctx) -> None:
    await client.get_cog("Works")._work_list_callback(ctx=ctx)


@_work.command(name="edit", guild_ids=guild_ids)
@option(type=int, name="id", description="O id da atividade", required=True)
@option(type=str, name="sigla", description="A sigla da disciplina.", required=False)
@option(type=str, name="data", description="O dia final da tarefa.", required=False)
@option(type=str, name="nome", description="The description of the giveaway.", required=False)
@option(type=str, name="link", description="Link para a atividade", required=False)
async def _work_add_slash(ctx, id : int, sigla: str = None, data: str = None, nome: str = None, link: str = None):
    await client.get_cog("Works")._work_edit_callback(ctx=ctx, work_id=id, acronym=sigla, date=data, name=nome, link=link)






### Siglas ###
_subjects = client.command_group(name='disciplinas', description="For copy and pasting stuff.", guild_ids=guild_ids)
@_subjects.command(name="add", guild_ids=guild_ids)
@option(type=str, name="sigla", description="A sigla da disciplina.", required=True)
@option(type=str, name="matéria", description="O nome da disciplina", required=True)
async def _subjects_add_slash(ctx, sigla: str, matéria : str) -> None:
    siglas = db.prefix("ac")
    if not "ac" + sigla in siglas:
        db["ac" + sigla] = matéria
        await ctx.respond(f"A matéria `{matéria}` foi ligada à sigla `{sigla}`")
    else:
        await ctx.respond("Esta sigla já está sendo usada para outra matéria")

@_subjects.command(name="listar", guild_ids=guild_ids)
async def _subjects_see_slash(ctx) -> None:
    await client.get_cog("Subjects")._subject_list_callback(ctx=ctx)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))