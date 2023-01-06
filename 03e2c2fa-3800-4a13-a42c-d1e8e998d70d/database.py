import sqlite3
#Adat bazis csatlakoztatasa
con = sqlite3.connect('CSSOS.db')
#Cursor definialassa
c = con.cursor()
#Tablazat letrehozassa
c.execute("""CREATE TABLE IF NOT EXISTS tagok 
(discord_id INTEGER PRIMARY KEY, discord_name TEXT, job_date INT, bool INT);
""")
#c.execute("INSERT INTO tagok VALUES (ctx.user.id, 'Dusan', 0)")
#c.execute("INSERT INTO tagok VALUES (0, 'Dusan', 0, 0)")
#c.execute("INSERT INTO tagok VALUES (1, 'Tester', 0, 0)")
#c.execute("""UPDATE tagok
#             SET bool = 0 
#             WHERE discord_id = 0;""")
c.execute("SELECT * FROM tagok")
c.execute("SELECT discord_id, discord_name, job_date, bool Result FROM tagok")
formatted_result = [f"ID: {discord_id:<15} Nev: {disord_name:<15} Oraszam: {job_date:<15}Szolgalatban van: {bool:<15}" for discord_id, disord_name, job_date, bool in c.fetchall()]
print('\n'.join(formatted_result))

#c.execute("SELECT * FROM tagok WHERE discord_id = 12"))

#rows = c.fetchall()
#for tagok in rows:
 # print(rows)

con.commit()
print("Record succes")
con.close()