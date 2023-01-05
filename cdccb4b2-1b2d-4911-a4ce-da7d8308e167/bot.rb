require "discordrb"

def run(token)
	# Now with slash commands!
	bot = Discordrb
end

# Validates token
token_file = IO.readlines(".token")
if  1 < token_file.length() <= 0
	abort("Token file can only feature one line containing the bot token.")
else
	run(token_file[0])
end


