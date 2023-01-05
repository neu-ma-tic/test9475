from database_model import Birthdays, Birthday, Bdate
from commons import local_time
from globals import client, birthdays_db, command_logs_db
from replit import db
import json, uuid


class DatabaseError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


def get_birthdays() -> Birthdays:
    birthdays = Birthdays()
    if birthdays_db not in db.keys():
        return birthdays

    try:
        data = json.loads(db[birthdays_db])
    except:
        raise DatabaseError("Database data is fucked up")

    # TODO?
    for d in data["_records"]:
        birthdays.append(
            Birthday(d["_user_id"], d["_birthday"]["_month"],
                     d["_birthday"]["_day"], d["_guild_id"],
                     d["_greeted_this_year"]))
    return birthdays


def add_birthday(new_birthday: Birthday) -> bool:
    birthdays = get_birthdays()
    if birthdays.append(new_birthday):
        db[birthdays_db] = json.dumps(birthdays, default=lambda o: o.__dict__)
        return True
    return False


def delete_birthday(user_id, guild_id) -> bool:
    birthdays = get_birthdays()
    if birthdays.delete(user_id, guild_id):
        db[birthdays_db] = json.dumps(birthdays, default=lambda o: o.__dict__)
        return True
    return False


def greet_user(user_id, guild_id) -> bool:
    birthdays = get_birthdays()
    for birthday in birthdays.getRecords():
        if birthday.getUser() == user_id and birthday.getGuild() == guild_id:
            birthday.setGreetedThisYear(True)
            db[birthdays_db] = json.dumps(birthdays,
                                          default=lambda o: o.__dict__)
            return True
    return False


def is_it_time(birthdate: Bdate) -> bool:
    now = local_time()
    if now.hour < 10: return False
    if birthdate.getMonth() == now.month and birthdate.getDay() == now.day:
        return True
    return False


def get_default_channels():
    if "channels" in db.keys():
        datas = db["channels"]
        if len(datas) == 0:
            return None
        return datas
    return None


def get_default_channel(guild_id):
    if "channels" in db.keys():
        datas = db["channels"]
        for d in datas:
            if d["guild_id"] == guild_id:
                return d["channel_id"]
    guild = client.get_guild(guild_id)
    return guild.text_channels[0]


def update_default_channel(guild_id, channel_id) -> None:
    if "channels" in db.keys():
        channels = db["channels"]
        for channel in channels:
            if channel["guild_id"] == guild_id:
                channel["channel_id"] = channel_id
                db["channels"] = channels
                return
        channels.append({"guild_id": guild_id, "channel_id": channel_id})
        db["channels"] = channels
    else:
        db["channels"] = [{"guild_id": guild_id, "channel_id": channel_id}]


def reset_greetings() -> None:
    birthdays = get_birthdays()
    birthdays.resetGreets()
    db[birthdays_db] = json.dumps(birthdays, default=lambda o: o.__dict__)


def log_command(message) -> None:
    newRecord = {
        "username": message.author.name,
        "channel": message.channel.name,
        "command": message.content,
        "created_at": message.created_at.strftime("%Y %b %d, %H:%M:%S"),
        "user_id": message.author.id,
        "channel_id": message.channel.id,
        "guild_id": message.guild.id,
        "log_id": str(uuid.uuid1())
    }
    command_logs = get_logs()
    command_logs["records"].append(newRecord)
    db[command_logs_db] = json.dumps(command_logs,
                                     default=lambda o: o.__dict__)


def get_logs() -> Birthdays:
    if command_logs_db in db.keys():
        try:
            command_logs = json.loads(db[command_logs_db])
        except:
            raise DatabaseError("Database data is fucked up")
    else:
        command_logs = {"records": []}
    return command_logs


def delete_log(unique_id) -> bool:
    command_logs = get_logs()
    for i in range(len(command_logs['records'])):
        if command_logs['records'][i]['log_id'] == unique_id:
            command_logs['records'].pop(i)
            db[command_logs_db] = json.dumps(command_logs,
                                             default=lambda o: o.__dict__)
            return True
    return False
