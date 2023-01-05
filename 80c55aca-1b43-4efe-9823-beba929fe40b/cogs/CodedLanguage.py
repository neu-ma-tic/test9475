import discord
from discord.ext import commands


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3


class CodeLanguage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def encrypt(self, ctx, code, *, message):
        output = ''
        if code == "0000":

            for char in message:
                if char.lower() in alphabet.lower():
                    if alphabet.find(char.upper()) < 23:
                        start = alphabet.find(char.upper())
                        new_char = alphabet[start + key]
                    else:
                        start = alphabet.find(char.upper())
                        new_char = alphabet[start - 23]

                else:
                    new_char = char

                output += new_char

        await ctx.channel.purge(limit=1)
        await ctx.send(f'Encrypted message: {output}')

    @commands.command()
    async def decrypt(self, ctx, code, *, message):
        output = ''
        if code == "0000":

            for char in message:
                if char.lower() in alphabet.lower():
                    if alphabet.find(char.upper()) > 2:
                        start = alphabet.find(char.upper())
                        new_char = alphabet[start - key]
                    else:
                        start = alphabet.find(char.upper())
                        new_char = alphabet[start - key]

                else:
                    new_char = char

                output += new_char

        await ctx.send(f'Decrypted message: {output}')


def setup(client):
    client.add_cog(CodeLanguage(client))

