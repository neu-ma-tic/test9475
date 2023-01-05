const dbd = require("dbd.js")
 
const bot = new dbd.Bot({
token: (process.env.TOKEN), 
prefix: ","
})

bot.status({
 
text: "stay hydrated! ily",
 
type: "PLAYING",
  
status: "idle",
  
time: 12

})