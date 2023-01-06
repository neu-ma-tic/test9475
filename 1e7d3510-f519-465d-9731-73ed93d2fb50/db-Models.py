class DBQuery:
    def __init__(self, db_connection):
        self.cursor = db_connection.cursor()

    def add_discord_users(self, discord_username, discord_numtag, discord_user_id, email_address, verify_code, verified, verify_calls):
        ''' Add into discord_users table'''

        add_discord_user = ("INSERT INTO discord_users "
                            "(discord_username, discord_numtag, discord_user_id, email_address, verify_code, verified, verify_calls) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (discord_username, discord_numtag, discord_user_id, email_address, verify_code, verified, verify_calls)

        self.cursor.execute(add_discord_user, data)
