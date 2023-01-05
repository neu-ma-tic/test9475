import discord
from discord.ext import commands
from replit import db
from datetime import datetime
import pytz

country_time_zone = pytz.timezone("Brazil/West")

class Works(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Works Cogs is on')

    
    @commands.command(aliases=['aw', 'add_w'])
    async def add_trabalho(self, ctx, acronym : str = None, date_limit : str = None, *, name : str = None):
        """Adiciona lembrete de atividade
            :sigla: Sigla de uma disciplina
            :data de término: Data limite no formato dd/mm/aa
            :name: Nome da atividade
            :link: Link para a atividade[Opcional]
        """
        if not acronym:
            return await ctx.send("**Usage: !add_trabalho <sigla> <data> <nome_da_atividade> <link>(Opcional)**")   
        
        if name.split()[-1].find('http') == 0:
            link = name.split()[-1]
            name = ' '.join(name.split()[0:-1])
        else:
            link = ' '

        self._work_add_callback(ctx, acronym, date_limit, name, link)

    async def _work_add_callback(self, ctx,  acronym : str, date_limit : str, name : str, link : str):

        await ctx.defer()
    
        acronyms_keys = db.prefix("ac")
        if not "ac" + acronym in acronyms_keys:
            return await ctx.respond("**A Sigla digitada não foi encontrada**")

        # Date check and format
        date_limit = date_limit.split('/')
        if len(date_limit) < 2 or len(date_limit) > 3:
            return await ctx.respond("Insira uma data válida")
        
        if len(date_limit) == 2:
            yy = 2000 + 21
        else:
            yy = 2000 + int(date_limit[2])
        mm = int(date_limit[1])
        dd = int(date_limit[0])
    
        time_in_sec = (datetime(yy, mm, dd, hour=22, minute=59, tzinfo=country_time_zone)).timestamp()

        if not db.prefix("w"):
            new_key = str(100)
            keys = db.prefix("w")
        else:
            keys = db.prefix("w")
            new_key = int(keys[-1][1:]) + 1

        if not 'w' + str(new_key) in keys:
            db["w" + str(new_key)] = [acronym, time_in_sec, name, link]

        await ctx.respond(f"`{name}` **adicionado com sucesso**")
    

    @commands.command(aliases=['del_w', 'dw', 'del_work'])
    async def del_trabalho(self, ctx):
        " Ao digitar o comando a lista de tarefas será mostrada. Digite um id para excluí-lo."
        # Show all ids
        keys = db.prefix("w")
        txt = []
        for key in keys:
            txt.append(f"`{key[1:]}`**- {db[key][2]}**\n")
        txt.append("**\nDigite um id para ser apagado**")
        embed = discord.Embed(title='Ids cadastrados', description=' '.join(txt))
        await ctx.send(embed=embed)

        def check(author):
            def inner_check(message):
                if message.author == author:
                    msg = message.content
                    if 'w' + msg in keys:
                        return True
                    else:
                        return False
            return inner_check
        
        message = await self.client.wait_for('message', check=check(ctx.author), timeout=30)

        id = message.content
        if db["w" + str(id)]:
            await ctx.send(f"`{db[ 'w'+ str(id)][2]}` Deletado com sucesso!")
            del db["w" + str(id)]
        else:    
            await ctx.send(f"**O id `{id}` não foi encontrado**")
        
    @commands.command(aliases=['sw', 'hw'])
    async def trabalhos(self, ctx):
        self.work_list_callback(ctx)

    async def _work_list_callback(self, ctx):

        await ctx.defer()

        txt = []
        subjects_keys = db.prefix("ac")
        for subject_acronym in subjects_keys:
            
            txt.append(f"\n**{db[subject_acronym]}** ({subject_acronym[2:]})\n")

            for work_id in db.prefix("w"):
                work = db[work_id]

                # Check acronym
                if work[0] == subject_acronym[2:]:
                    if work[1] >= datetime.now(country_time_zone).timestamp():
                        time_sec = int(work[1])
                        name = work[2]
                        link = work[3]
                        txt.append(f"`{work_id[1:]}` [{name}]({link}) termina <t:{time_sec}:R>\n")
        
        embed=discord.Embed(title='__Tarefas__', description=' '.join(txt))
        await ctx.respond(embed=embed)
    
    async def _work_edit_callback(self, ctx, work_id : int, acronym : str = None, date : str = None, name : str = None, link : str = None):
        if acronym == None and date == None and name == None and link == None:
            return await ctx.respond("**Você precisa fornecer pelo menos um parâmetro**")
        
        await ctx.defer()
        
        key = 'w' + str(work_id)

        if not key in db.prefix('w'):
            return await ctx.respond("**A sigla digitada não foi encontrada**")

        params = db[key]
        if acronym != None:
            params[0] = acronym
            db[key] = params
            await ctx.respond(f"**Sigla de `{params[2]}` alterada com sucesso para `{acronym}`**")

        if date != None:
            if not await self.check_hour_format(ctx, date):
                return await ctx.respond("Insira uma data válida")

            date = date.split('/')
            if len(date) == 2:
                yy = 2000 + 21
            else:
                yy = 2000 + int(date[2])
            mm = int(date[1])
            dd = int(date[0])
        
            time_in_sec = (datetime(yy, mm, dd, hour=22, minute=59, tzinfo=country_time_zone)).timestamp()
            params[1] = int(time_in_sec)
            db[key] = params
            await ctx.respond(f"**Data de `{params[2]}`  alterada com sucesso para** <t:{params[1]}:d>")

        if name != None:
            params[2] = name
            db[key] = params       
            await ctx.respond(f"**Nome alterada com sucesso para `{params[2]}`**")

        if link != None: 
            params[3] = link
            db[key] = params
            await ctx.respond("**Link alterada com sucesso**")

    async def check_hour_format(self, ctx, date_str : str):
        try:
            datetime.strptime(date_str,"%d/%m/%y")
        except ValueError:
            try:
                datetime.strptime(date_str,"%d/%m")
            except ValueError:
                return False
        return True
        
'''
class GiveView(discord.ui.View):
    """ View for the give skill. """

    def __init__(self, member: discord.Member, target: discord.Member, timeout: Optional[float] = 180):
        super().__init__(timeout=timeout)
        self.member = member
        self.target = target
        self.used: bool = False

        self.foods: Dict[str, Dict[str, str]] = self.get_foods()

        options = [
            discord.SelectOption(label=food, emoji=values['emoji'])
            for food, values in self.foods.items()]

        foods_select = discord.ui.Select(placeholder="What do you wanna give them?",
        custom_id="give_select_id", min_values=1, max_values=1, options=options)

        foods_select.callback = partial(self.give_button, foods_select)

        self.children.insert(0, foods_select)

    def get_foods(self) -> Dict[str, Dict[str, str]]:
        data = {}
        with open('./extra/slothclasses/foods.json', 'r', encoding="utf-8") as f:
            data = json.loads(f.read())
        return data

    async def give_button(self, button: discord.ui.button, interaction: discord.Interaction) -> None:
        """ Gives someone something. """


        selected = interaction.data['values'][0]
        option = self.foods[selected]

        embed = discord.Embed(
            title=f"__{option['name']}__",
            description=f"{option['emoji']} {option['sentence']} {option['emoji']}".format(member=self.member, target=self.target),
            color=discord.Color.magenta(),
            timestamp=interaction.message.created_at
        )

        embed.set_author(name=self.member.display_name, url=self.member.display_avatar, icon_url=self.member.display_avatar)
        embed.set_thumbnail(url=self.target.display_avatar)
        embed.set_image(url=choice(option['gifs']))
        embed.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon.url)

        await interaction.response.send_message(content=self.target.mention, embed=embed)
        await self.disable_buttons(interaction, followup=True)
        self.used = True
        self.stop()

    @discord.ui.button(label='Nothing', style=discord.ButtonStyle.red, custom_id='nothing_id', emoji="❌", row=2)
    async def nothing_button(self, button: discord.ui.button, interaction: discord.Interaction) -> None:
        """ Cancels the give action. """

        await self.disable_buttons(interaction)
        self.stop()

    async def disable_buttons(self, interaction: discord.Interaction, followup: bool = False) -> None:
        """ Disables all buttons of the view menu. """

        for child in self.children:
            child.disabled = True

        if followup:
            await interaction.followup.edit_message(message_id=interaction.message.id, view=self)
        else:
            await interaction.response.edit_message(view=self)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return self.member.id == interaction.user.id'''
"""
db
w[num] = [acronym, time_in_sec, name, link]
"""
def setup(client) -> None:
    client.add_cog(Works(client))
