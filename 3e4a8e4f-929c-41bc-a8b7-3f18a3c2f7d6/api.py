import uuid

from replit import db

key = 'api_keys'


def create(user):
    api_key = uuid.uuid4().hex
    api_keys = {}

    try:
        api_keys = db[key]
    except KeyError:
        pass

    api_keys[user] = api_key
    db[key] = api_keys

    return api_key


def get(user):
    return db[key][user]


def get_all():
    return db[key]


def delete(user):
    api_keys = get_all()
    del api_keys[user]
    db[key] = api_keys


def delete_all():
    del db[key]


if __name__ == '__main__':
    print(get_all())
