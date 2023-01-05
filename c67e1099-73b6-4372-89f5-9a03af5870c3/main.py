import os
from discord_easy_commands import EasyBot
bot = EasyBot()
bot.setCommand("!Oniichan", "Konichiwua Onii-chan")
bot.setCommand("!Nya", "¡Nya!")
bot.run(os.environ['TOKEN'])