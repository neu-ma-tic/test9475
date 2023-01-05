import os

import requests

api = "https://discord.com/api/v8/"
headers = {"Authorization": f"Bot {os.environ['BOT_TOKEN']}"}

applicationID = 719120395571298336


class RequestFailed(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return f"request failed, reason:{self.reason}"


# 編輯權限
def edit_permission(
    ID: int, idType: int, permission: bool, guildID, commandID, oldPermission=None
) -> str:
    url = f"/applications/{applicationID}/guilds/{guildID}/commands/{commandID}/permissions"

    permissions = []
    permissions.append(
        {
            "id": int(ID),  # role or user id
            "type": idType,  # 1:role, 2:user
            "permission": permission,  # T/F
        }
    )
    if oldPermission:
        permissions.extend(oldPermission["permissions"])

    json = {"permissions": permissions}

    r = requests.put(f"{api}{url}", headers=headers, json=json)
    if r.ok:
        return "更改成功"
    else:
        raise RequestFailed(r.reason)


# 取得指令列表
def get_commands(guildID: int = None) -> list:
    """
    回傳指令列表
    """
    if guildID:
        url = f"/applications/719120395571298336/guilds/{guildID}/commands"
    else:
        url = "/applications/719120395571298336/commands"
    r = requests.get(f"{api}{url}", headers=headers)
    if r.ok:
        return r.json()
    else:
        raise RequestFailed(r.reason)


# 編輯指令
def edit_command(default_permission: bool, commandID: int, guildID: int = None) -> str:
    if guildID:
        url = f"/applications/{applicationID}/guilds/{guildID}/commands/{commandID}"
    else:
        url = f"/applications/{applicationID}/commands/{commandID}"
    json = {  # name, description, options, default_permission
        "default_permission": default_permission
    }
    r = requests.patch(f"{api}{url}", json=json, headers=headers)
    if r.ok:
        return "更改成功"
    else:
        raise RequestFailed(r.reason)


# 取得指令權限列表
def get_command_permissions(guildID: int, commandID: int = None) -> list:
    if commandID:
        url = f"/applications/{applicationID}/guilds/{guildID}/commands/{commandID}/permissions"
    else:
        url = f"/applications/{applicationID}/guilds/{guildID}/commands/permissions"
    r = requests.get(f"{api}{url}", headers=headers)
    if r.ok:
        return r.json()
    else:
        raise RequestFailed(r.reason)
