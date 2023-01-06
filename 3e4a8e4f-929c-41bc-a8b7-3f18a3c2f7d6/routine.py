import time
import utils

from replit import db
from datetime import date
from utils import minutes_sub, BOSSES
import db_utils


def delete_old_timers():
    utils.logger('DOT: ready')
    while True:
        utils.logger('DOT: check')
        for key in db.keys():
            if key.isdigit() and key in BOSSES:
                timer = db[key]
                if timer is not None and minutes_sub(timer) <= -180:
                    utils.logger(f'DOT: deleted {key}')
                    db[key] = None

        # 3h
        time.sleep(10800)


def delete_logs():
    utils.logger('DL: ready')
    last_delete = date.today()
    try:
        last_delete = date.fromtimestamp(float(db['last_delete']))
    except KeyError:
        db['last_delete'] = str(time.time())
    while True:
        days = (date.today() - last_delete).days
        utils.logger(f'DL: check, days: {days}')
        if days >= 10:
            db_utils.delete_logs()

        # 10 days
        time.sleep(864000)
