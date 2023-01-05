from typing import Union

import yaml
from addict import Dict
from bidict import bidict
from core import (
    CogInit,
    edit_command,
    edit_permission,
    get_command_permissions,
    get_commands,
    read_yaml,
    write_yaml,
)
from discord.ext import commands
from discord_slash import cog_ext, error
from discord_slash.utils.manage_commands import create_choice, create_option


class slashCommands(CogInit):
    def __init__(self, bot):
        super().__init__(bot)
        self.cmd_map = bidict(read_yaml("config")["command_map"])

    def get_name(self, id_type: int, ID: int, guild: int) -> str:
        """
        取得身分組或user名稱
        """
        if id_type == 1:  # 身分組
            return self.bot.get_guild(guild).get_role(ID).name + f"({ID})"
        elif id_type == 2:  # user
            return self.bot.get_user(ID).name + f"({ID})"

    def cmd_mapping(self, thing: Union[str, int]):
        """
        將指令id和名稱互相映射
        """
        try:
            thing = int(thing)
        except:  # 輸入為名稱
            cmd_map = self.cmd_map
        else:  # 輸入為id
            cmd_map = self.cmd_map.inverse
        finally:
            thing = cmd_map[thing]
            if thing:
                return thing
            else:  # 無此id或名稱
                raise IndexError(f"no command {thing}")

    # 顯示指令列表
    @cog_ext.cog_subcommand(
        base="command",
        name="get_list",
        description="取得斜線指令列表",
        options=[create_option("guildid", "指定伺服器ID", 3, False)],
    )
    async def get_commands(self, ctx, guildid=None):
        r = get_commands(guildid)
        if type(r) is list:
            r = list(map(Dict, r))
            commands = Dict()
            command_map = self.cmd_map  # 指令id和名稱映射表
            # 將列表整理成{name : {id, 預設權限}}，及映射表{name : id}
            for command in r:
                command_map[command.name] = int(command.id)
                commands[command.name] = {
                    "id": int(command.id),
                    "default_permission": command.default_permission,
                }
            commands = yaml.safe_dump(commands.to_dict(), indent=4)  # 轉為可輸出的文字
            write_yaml("config", dict(command_map), "command_map")  # 將映射表寫入檔案中
            self.cmd_map = command_map
            await ctx.send(commands, hidden=True)
        else:  # request failed
            await ctx.send(r, hidden=True)

    # 編輯斜線指令
    @cog_ext.cog_subcommand(
        base="command",
        name="edit",
        description="編輯斜線指令",
        options=[
            create_option(
                name="default_permission",
                description="預設權限",
                option_type=3,
                required=True,
                choices=[create_choice("True", "是"), create_choice("False", "否")],
            ),
            create_option(name="command_name", description="指令ID", option_type=3, required=True),
            create_option(name="guildid", description="指定伺服器ID", option_type=3, required=False),
        ],
    )
    async def edit_command(self, ctx, default_permission, command_name, guildid=None):
        command_id = self.cmd_mapping(command_name)
        r = edit_command(default_permission, command_id, guildid)
        await ctx.send(r, hidden=True)

    # 顯示指令權限列表
    @cog_ext.cog_subcommand(
        base="command",
        subcommand_group="permission",
        name="get_list",
        description="取得斜線指令權限列表",
        options=[
            create_option(name="guildid", description="伺服器ID", option_type=3, required=True),
            create_option(name="command_name", description="指令名稱", option_type=3, required=False),
        ],
    )
    async def get_command_permission(self, ctx, guildid, command_name=None):
        if command_name:  # 有指定指令名稱，將名稱轉為id
            command_id = self.cmd_mapping(command_name)
        else:
            command_id = None
        r = get_command_permissions(guildid, command_id)  # 權限列表
        if type(r) is list:
            r = list(map(Dict, r))
            commands = []
            guild = self.bot.get_guild(int(guildid)).name + f"({guildid})"  # 取得伺服器名稱
            # 將權限列表整理成{command_name : {name : [權限]}}
            for command in r:
                cmd_name = self.cmd_mapping(command.id)
                permissions = []
                # 整理每個人的權限
                for permission in command.permissions:
                    name = self.get_name(permission.type, int(permission["id"]), int(guildid))
                    permissions.append({name: permission.permission})

                commands.append({cmd_name: permissions})
            await ctx.send(
                yaml.safe_dump({guild: commands}, indent=4, allow_unicode=True),
                hidden=True,
            )
        else:
            await ctx.send("request failed", hidden=True)

    # 修改指令權限
    @cog_ext.cog_subcommand(
        base="command",
        subcommand_group="permission",
        name="edit",
        description="修改斜線指令權限",
        options=[
            create_option(
                name="target",
                description="要修改權限的user/role",
                option_type=9,
                required=True,
            ),
            create_option(
                name="target_type",
                description="ID種類",
                option_type=4,
                required=True,
                choices=[create_choice(1, "身分組"), create_choice(2, "使用者")],
            ),
            create_option(
                name="permission",
                description="權限",
                option_type=3,
                required=True,
                choices=[create_choice("True", "是"), create_choice("False", "否")],
            ),
            create_option(name="guildid", description="伺服器ID", option_type=3, required=True),
            create_option(name="command_name", description="指令名稱", option_type=3, required=True),
        ],
    )
    async def edit_command_permission(
        self, ctx, target, target_type, permission, guildid, command_name
    ):
        command_id = self.cmd_mapping(command_name)
        r = edit_permission(target, target_type, permission, guildid, command_id)
        await ctx.send(r, hidden=True)

    # 在現有的權限後方擴充權限
    @cog_ext.cog_subcommand(
        base="command",
        subcommand_group="permission",
        name="append",
        description="擴充斜線指令權限",
        options=[
            create_option(
                name="target",
                description="要修改權限的user/role",
                option_type=9,
                required=True,
            ),
            create_option(
                name="target_type",
                description="ID種類",
                option_type=4,
                required=True,
                choices=[create_choice(1, "身分組"), create_choice(2, "使用者")],
            ),
            create_option(
                name="permission",
                description="權限",
                option_type=3,
                required=True,
                choices=[create_choice("True", "是"), create_choice("False", "否")],
            ),
            create_option(name="guildid", description="伺服器ID", option_type=3, required=True),
            create_option(name="command_name", description="指令名稱", option_type=3, required=True),
        ],
    )
    async def append_command_permission(
        self, ctx, target, target_type, permission, guildid, command_name
    ):
        command_id = self.cmd_mapping(command_name)
        old_permissions = get_command_permissions(guildid, command_id)
        r = edit_permission(target, target_type, permission, guildid, command_id, old_permissions)
        await ctx.send(r, hidden=True)

    # slash command error handler
    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, ex):
        if isinstance(ex, error.IncorrectFormat):
            await ctx.send("斜線指令格式錯誤，已進行紀錄", hidden=True)
        elif isinstance(ex, error.DuplicateCommand):
            await ctx.send("指令重複，已進行紀錄", hidden=True)
        elif isinstance(ex, error.IncorrectType):
            await ctx.send("輸入的參數類型錯誤", hidden=True)
        else:
            await ctx.send(f"發生例外錯誤 {ex}，已進行紀錄", hidden=True)
        if not await self.bot.is_owner(ctx.author):
            await self.bot.get_channel(812628283631206431).send(
                f"指令：/{ctx.name}(id:{ctx.command_id}, by:{ctx.author.mention})\n錯誤：{ex}"
            )

    # 斜線指令使用紀錄
    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        if not await self.bot.is_owner(ctx.author):
            msg = f"/{ctx.name}"
            if ctx.subcommand_name:
                msg += f" {ctx.subcommand_name} "
            if ctx.subcommand_group:
                msg += f" {ctx.subcommand_group} "
            for arg, value in ctx.kwargs.items():
                msg += f" `{arg}`:`{value}`"
            msg += f"\n(commandID:{ctx.command_id}, by:{ctx.author.mention})"
            await self.bot.get_channel(747054636778913853).send(msg)


def setup(bot):
    bot.add_cog(slashCommands(bot))
