from discord.ext import commands


links = {'povijesna umjetnost': "https://zoom.us/j/94476613530?pwd=RjNYN1k3N1lLL2xMTjVWcU45QWg1dz09",
         'fizički jezik': "https://zoom.us/j/94614599793?pwd=OVorQlkxc2I4bzJzeFN6K1hQN3VKQT09",
         'informatička umjetnost': "https://zoom.us/j/95044701988?pwd=VHIrU0haYWdkKzRMdW5TS2dnbGVhdz09",
         'vjeronaučka znanost': "https://zoom.us/j/5806900932?pwd=UjJ4a09IenpnRjdIYjZZenJHbVk2dz09",
         'matematička umjetnost': "https://zoom.us/j/95326842691?pwd=L2xJbEJ6QVdySlkvdjlwQVhxRmJVZz09",
         'likovna znanost': "https://us04web.zoom.us/j/78406547199?pwd=a0tFM1FEd3ZPTHhGSnluTGVaWWR1dz09",
         'geografijska geologija': "https://us04web.zoom.us/j/77168933982?pwd=S3NFWTBTdS9tY0xxaFoxS1FCd3FYQT09",
         'biologijska umjetnost': "https://zoom.us/j/91061057551?pwd=UkpmNFNQMFY2SElieGk3aWpvY2Jodz09",
         'kemija': "https://zoom.us/j/99340765881?pwd=VkR4ZEJLVlhhTEdaTUw3TWN3akw4QT09",
         'engleska kultura': "https://zoom.us/j/94661236258?pwd=RUxPTkVqWnhmUGNqUE5YQldZQ0lHQT09",
         'glazbena smrt': "https://zoom.us/j/93898945081?pwd=cFZxOXdLMU9DMUNtTWJXTXRtVWtsQT09",
         'hrvatski sad možda dobar': "https://zoom.us/j/94917840731?pwd=K05DbGRBdklST0RENStwQk96azZZZz09"
         }


class Links(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def link(self, ctx, subject):
        if 'mat' in subject.lower():
            await ctx.send(links['matematička umjetnost'])
        elif 'eng' in subject.lower():
            await ctx.send(links['engleska kultura'])
        elif 'fiz' in subject.lower():
            await ctx.send(links['fizički jezik'])
        elif 'gla' in subject.lower():
            await ctx.send(links['glazbena smrt'])
        elif 'geo' in subject.lower():
            await ctx.send(links['geografijska geologija'])
        elif 'lik' in subject.lower():
            await ctx.send(links['likovna znanost'])
        elif 'kem' in subject.lower():
            await ctx.send(links['kemija'])
        elif 'vje' in subject.lower():
            await ctx.send(links['vjeronaučka znanost'])
        elif 'inf' in subject.lower():
            await ctx.send(links['informatička umjetnost'])
        elif 'bio' in subject.lower():
            await ctx.send(links['biologijska umjetnost'])
        elif 'pov' in subject.lower():
            await ctx.send(links['povijesna umjetnost'])
        elif 'hrv' in subject.lower():
            await ctx.send(links['hrvatski sad možda dobar'])
        else:
            await ctx.send(f'Sorry, >> {subject} << link does not exist in our database')

    @commands.command()
    async def all_links(self, ctx):
        for name, value in links.items():
            await ctx.send(name + ': ' + value)


class Classes(commands.Cog):

    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Links(client))



