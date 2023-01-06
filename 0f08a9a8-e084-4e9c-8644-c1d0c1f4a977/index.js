const miftcmd = require("@miftikcz/miftcmd")
const client = new miftcmd({
    prefix: "?", 
    status: "s",
})

require("mift-uptimer")("https://DiscordBot.timilol.repl.co")



client.use.pre_build_help(cs)


client.use.pre_build_invite("https://discord.com/api/oauth2/authorize?client_id=902603404294127676&permissions=8&scope=bot")


client.log(process.env.token)