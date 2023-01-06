import os
import requests

WEBHOOK = os.getenv('WEBHOOK')
USERNAME = 'Bot_Status'


def send_msg(msg):
    requests.post(WEBHOOK, data={'username': USERNAME, 'content': msg})
