from replit import db
from utils import BOSSES
import utils
import time


def delete_all_subs():
    for key in db.keys():
        if key.endswith('sub'):
            print(key)
            del db[key]


def get_all_key_values():
    db_kv = {}
    for key in db.keys():
        db_kv[key] = db[key]
    return db_kv


def print_db(db_kv):
    for key, value in db_kv.items():
        print(f'{key}: {value}')


def get_all_bosses():
    return {boss: timer for (boss, timer) in db.items() if boss in BOSSES}


def write_logs_file(file_name='tmp.txt'):
    with open(file_name, 'w') as logs:
        logs.write(db['logs'])


def delete_logs():
    with open('log.txt', 'w') as logs:
        logs.write('--DELETED--\n')
        db['logs'] = ''
        utils.logger('DL: deleted logs')
        db['last_delete'] = str(time.time())


if __name__ == '__main__':
    write_logs_file()
