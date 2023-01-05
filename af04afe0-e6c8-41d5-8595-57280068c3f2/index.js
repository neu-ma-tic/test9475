var dbd = require("dbd.js")
var fs = require("fs")

const bot = new dbd.Bot({
token: process.env.TOKEN,
prefix: "$getServerVar[prefix]"
})
 
//bot status
bot.status({
  text: process.env.BOT_ACTIVITY_TEXT,
  type: process.env.BOT_ACTIVITY_TYPE,
  time: 12
})
 
bot.onMessage()

//variable
bot.variables({
 prefix: process.env.PREFIX,
 bank:"0",
 cash:"0",
 diamond:"0",
 fish:"0",
 fishrod:"0",
 car:"0",
 house:"0",
 laptop:"0",
 fuel:"0",
 health:"100",
 hungry:"100",
 thirsty:"100",
 pizza:"0",
 drink:"0",
 hm:"0",
 daily: process.env.DAILY_SALARY,
 monthly: process.env.MONTHLY_SALARY
})
  
 //commands handler
var reader = fs.readdirSync("./economy/").filter (file => file.endsWith(".js"))
for(const file of reader) {
  const command = require(`./economy/${file}`)
  bot.command({
name: command.name, 
aliases: command.aliases,
code: command.code
  })
}

require('http').createServer((req, res) => res.end('Bot is alive!')).listen(3000)