from flask import Flask, render_template, request, jsonify
from threading import Thread
from globals import db_url, client, birthdays_db, command_logs_db
from replit import db
from database_controller import delete_log
from datetime import datetime, timedelta
import json, discord

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/cum')
def cum():
    return render_template("cum.html")


@app.route('/' + db_url + '/birthdays')
def birthdays():
    if client.user is None:
        return render_template("birthdays.html", data=False)
    if birthdays_db in db.keys():
        birthdays = json.loads(db[birthdays_db])["_records"]
        data = []
        for d in birthdays:
            record = {}

            guild = client.get_guild(d["_guild_id"])
            member = guild.get_member(d["_user_id"])
            nick = member.nick
            name = member.name

            month = d["_birthday"]["_month"]
            month = str(month) if month > 9 else "0" + str(month)
            day = d["_birthday"]["_day"]
            day = str(day) if day > 9 else "0" + str(day)

            record["is_greeted"] = d["_greeted_this_year"]
            record["birthday"] = month + "/" + day
            record["member_name"] = nick if nick else name
            try:
                record["member_avatar"] = member.display_avatar.url
            except:
                record[
                    "member_avatar"] = f"https://cdn.discordapp.com{member.avatar_url._url}"
            try:
                record["guild_icon"] = guild.icon.url
            except:
                record[
                    "guild_icon"] = f"https://cdn.discordapp.com{guild.icon_url._url}"
            record["guild_name"] = guild.name

            data.append(record)
    else:
        data = "There are no birthdays yet."
    data.sort(key=lambda d: d["birthday"])
    data.sort(key=lambda d: d["guild_name"])
    load = {"data": data}
    return render_template("birthdays.html", data=load)


@app.route('/' + db_url + '/cmdlogs')
def cmdlogs():
    if client.user is None:
        return render_template("cmdlogs.html", data=False)
    if command_logs_db in db.keys():
        command_logs = json.loads(db[command_logs_db])["records"]
        data = []
        version = "None..."
        for d in command_logs:
            record = {}

            channel = client.get_channel(d["channel_id"])
            guild = channel.guild
            member = guild.get_member(d["user_id"])
            nick = member.nick
            name = member.name
            avatar = None
            try:
                avatar = member.display_avatar.url
                version = str(discord.__version__) + " #1"
            except:
                avatar = f"https://cdn.discordapp.com{member.avatar_url._url}"
                version = str(discord.__version__) + " #2"

            record["member_name"] = nick if nick else name
            record["member_avatar"] = avatar
            record["guild"] = guild.name
            record["channel"] = d["channel"]
            # e.g. 2022 Aug 18, 14:23:29
            time = datetime.strptime(d["created_at"], '%Y %b %d, %H:%M:%S')
            time += timedelta(hours=2)
            time = time.strftime('%Y %b %d, %H:%M:%S')
            record["created_at"] = time
            record["log_id"] = d["log_id"]
            record["command"] = d["command"]
            data.append(record)

        print(f"verson: {version}")
    else:
        data = "Command logs are empty"
    load = {"data": data}
    return render_template("cmdlogs.html", data=load)


@app.route('/' + db_url + '/cmdlogs/delete', methods=['POST'])
def cmdlogs_delete():
    data = request.json
    resp = delete_log(data['log_id'])
    if resp:
        resp = jsonify('Log deleted successfully')
        resp.status_code = 200
        return resp
    else:
        resp = jsonify('Something went wrong during log deletion')
        resp.status_code = 500
        return resp


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
