import os
from typing import Union

import MySQLdb
import yaml
from addict import Dict


def read_yaml(file: str) -> Union[list, dict]:
    with open(file + ".yaml", "r", encoding="utf8") as f:
        data = yaml.safe_load(f)
        if not data:
            return {}
        else:
            return data


def write_yaml(file: str, data: Union[dict, list], category: str = None) -> None:
    if type(data) is Dict:
        data = data.to_dict()
    if category:
        with open(file + ".yaml", "r", encoding="utf8") as f:
            old_data = yaml.safe_load(f)
            old_data[category] = data
            data = old_data
    with open(file + ".yaml", "w", encoding="utf8") as f:
        yaml.safe_dump(data, f, encoding="utf8", allow_unicode=True)
    return


def conn():
    return MySQLdb.connect(
        host=os.environ["SQL_HOST"],
        user=os.environ["SQL_USER"],
        passwd=os.environ["SQL_PASSWD"],
        db=os.environ["SQL_DB"],
        charset="utf8",
        use_unicode=True,
    )


db = conn()


def get_cursor():  # 確認連線狀況並回傳cursor
    global db
    try:
        db.cursor().execute("SELECT 1")
    except:
        db = conn()
    finally:
        return db.cursor()


def SQL_modify(query):
    global db
    with get_cursor() as cursor:
        try:
            cursor.execute(query)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return


def SQL_inquiry(query, num: int = None):
    global db
    if num:
        query += f" LIMIT {num}"  # 有限制查詢筆數
    with get_cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        if result and num == 1:
            result = result[0]
    return result


def SQL_getData(table, column, data, num: int = None):
    return SQL_inquiry(f'SELECT * FROM {table} WHERE {column}="{data}"', num)


CONFIG = Dict(read_yaml("config"))

Config: Dict = CONFIG.config

Game: Dict = CONFIG.game

Emoji: Dict = CONFIG.emojis
