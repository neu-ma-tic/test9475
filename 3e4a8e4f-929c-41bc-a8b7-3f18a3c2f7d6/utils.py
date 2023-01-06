import webhook
import time

from replit import db
from datetime import datetime

_429 = 1200

TIME_KILL = False
'''
logger = logging.getLogger('server')
logger.addHandler(logging.FileHandler('log.txt'))
logger.setLevel(logging.INFO)
'''

BOSSES = {
    '110': 30,
    '115': 35,
    '120': 40,
    '125': 45,
    '130': 50,
    '140': 55,
    '155': 60,
    '160': 65,
    '165': 70,
    '170': 80,
    '180': 90,
    '185': 75,
    '190': 85,
    '195': 95,
    '200': 105,
    '205': 115,
    '210': 125,
    '215': 135,
    'aggy': 1894,
    'mord': 2160,
    'hrung': 2160,
    'necro': 2160,
    'prot': 1190,
    'gele': 2880,
    'bt': 4320,
    'dino': 4320
}

MINUTES_IN_A_DAY = 1440
SUB_SUFFIX = 'sub'


def minutes_sub(timer):
    return timer - (round(time.time()) // 60)


def minutes_add(timer):
    return round(time.time()) // 60 + timer


def minutes_to_dhm(minutes):
    minutes = minutes_sub(minutes)
    negative = False
    if int(minutes) < 0:
        minutes *= -1
        negative = True
    days = minutes // MINUTES_IN_A_DAY
    minutes = minutes % MINUTES_IN_A_DAY
    hours = minutes // 60
    minutes = minutes % 60
    msg = f'{str(days) + "d " if days > 0 else ""}{str(hours) + "h " if hours > 0 else ""}{minutes}m'
    if not negative:
        return msg
    return '-' + msg


def get_timer(boss):
    if boss in BOSSES:
        try:
            return db[boss]
        except KeyError:
            return None
    else:
        return None


def set_timer(boss, timer):
    if boss in BOSSES:
        timer = int(timer)
        if timer == 0:
            db[boss] = None
        else:
            db[boss] = minutes_add(timer)
        return True
    return False


def get_subs(boss):
    if boss in BOSSES:
        subs = []
        boss_suffix = boss + SUB_SUFFIX
        try:
            subs = db[boss_suffix]
        except KeyError:
            db[boss_suffix] = subs
        return subs
    return None


def add_sub(boss, user_id):
    subs = get_subs(boss)
    if subs is not None and user_id not in subs:
        subs.append(user_id)
        db[boss + SUB_SUFFIX] = subs
        return True
    return False


def remove_sub(boss, user_mention):
    subs = get_subs(boss)
    if subs and user_mention in subs:
        subs.remove(user_mention)
        db[boss + SUB_SUFFIX] = subs
        return True
    return False


def usage(message):
    return f'I could not understand _{message}_\nCommands:\n__all/All/soon/Soon__: get all available timers. e.g. ' \
           f'_all_\n__g/G/get/Get boss__: to get a boss timer. e.g. _180_\n__boss timer__: to set a specific timer to a boss in minutes. Set the timer to _0_ to delete it. e.g. _180 56_, _180 0_' \
           f'\n__w/W/when/When boss__: get the timestamp when the boss is due in game(game timezone). e.g. _w 180_' \
           f'\n__boss__: it will reset a ' \
           f'boss timer to the default timer. e.g. _180_\n__sub/Sub boss boss ...__: subscribe to a/some boss/es, ' \
           f'when it/they will be due, you will be tagged in a message on discord. e.g. _sub 180 205 ' \
           f'prot_\n__unsub/Unsub boss boss ...__: unsub from a/some boss/es to not be anymore notified when it is ' \
           f'due. e.g. _unsub 180 205 prot_ '


def separator_label(category, separator='---------------------------------'):
    return separator + '\n' + category + '\n'


class Message:
    def __init__(self, content, author):
        self.content = content
        self.length = len(content)
        self.author_mention = author.mention
        self.author_id = author.id
        self.author_name = str(author)

    def __str__(self):
        return f'content:{self.content}, length:{self.length}, mention:{self.author_mention}, id:{self.author_id}'


def logger(msg):
    log = f'[{datetime.now()}] {msg}'
    print(log)
    with open('log.txt', 'a') as logs:
        logs.write(log + '\n')
    db['logs'] = db['logs'] + log + '\n'


def status(down):
    status_message = ''
    if down:
        logger('429')
        db['429'] = True
        status_message = f'Down for 20mins since {datetime.now()}'
    else:
        db['429'] = False
        status_message = f'Alive since {datetime.now()}'
    db['status'] = status_message
    webhook.send_msg(status_message)
