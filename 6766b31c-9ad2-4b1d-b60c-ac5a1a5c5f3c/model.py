from orm import *

class Code(Model):
    discord_id = int
    ark_kod = str

    def __init__(self, discord_id, ark_kod):
        self.discord_id = discord_id
        self.ark_kod = ark_kod



def get_user_or_false(discord_id):
    objects = Code.manager(db)
    users = list(objects.all())

    for user in users:
        if user.discord_id == discord_id:
            return user

    return False

db = Database('code.sqlite')
Code.db = db