from protótipo.bot import Bot
import os

bot = Bot()

if __name__ == "__main__":
    if os != "nt":
        
	    import uvloop

	    uvloop.install()
        
    bot.run()