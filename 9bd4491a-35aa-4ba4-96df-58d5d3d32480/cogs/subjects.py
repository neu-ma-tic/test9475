import discord
from discord.ext import commands
from replit import db
from typing import Optional

class Subjects(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Acronyms Cogs is on')

    @commands.command(aliases = ['asigla'])
    async def add_sigla(self, ctx, acronym : str = None, *, subject_name : str = None):
        """
            Cadastra uma sigla nova
            :sigla: Sigla para identificar uma disciplina
            :nome: Nome da disciplina
        """
        if not acronym:
            return await ctx.send("Por favor, insira uma sigla")
        
        if not subject_name:
            return await ctx.send("Por favor, insira um nome pra matéria")

        acronyms = db.prefix("ac")

        if not "ac" + acronym in acronyms:
            db["ac" + acronym] = subject_name
            await ctx.channel.send(f"A matéria `{subject_name}` foi ligada à sigla `{acronym}`")
        else:
            await ctx.send("Essa sigla já está sendo usada para outra matéria")

    @commands.command(aliases=['ss'])
    async def disciplinas(self, ctx):
        self._subject_list_callback(ctx)

    async def _subject_list_callback(self, ctx):
        """
            Ver todas as siglas cadastradas
        """
        await ctx.defer()
        
        if not db.prefix("ac"):
            return await ctx.respond("**Nenhuma sigla cadastrada**")
        
        keys = db.prefix("ac")

        embed = discord.Embed(title="__Disciplinas__ (Siglas)",
        colour=ctx.author.color,
        description = f'\n'.join(f"`{key[2:]}` - **{db[key]}**" for key in keys))
        await ctx.respond(embed=embed)

    @commands.command(aliases = ["dsigla"])
    async def del_sigla(self, ctx, acronym : str = None):
        """
            Deleta uma sigla cadastrada
            :sigla: sigla de uma matéria
        """
        if not acronym:
            return ctx.send("Por favor, insira uma sigla para deletar", delete_after=3)
        
        if "ac" + acronym not in db.prefix("ac"):
            return await ctx.send('**Sigla não encontrada**')
        
        del db["ac" + acronym]
        await ctx.send(f"**Sigla `{acronym}` deletada com sucesso**")


def setup(client) -> None:
    client.add_cog(Subjects(client))