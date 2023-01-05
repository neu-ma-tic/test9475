const express = require("express")
const app = express()
const SecretCode = "1020392059"

app.get("/", (req, res) => {
  res.send("Hello")
})

app.listen(3000, () => {
  console.log("Project is ready!")
})

let Discord = require("discord.js")
let client = new Discord.Client()

client.on("ready", () => {
  client.user.setPresence({ activity: {name: "Scanning for messages"}, status: "idle"})
})

client.on("message", message => {
  if(message.content === "ping"){
    message.channel.send("pong")
  }
  
  if(message.content === "Hello"){
    message.channel.send("Well Hello!")
  }
  if(message.content==="Destroy code: 12949830920409099393049JJKJOJNUHIHHIUHI394398928"){
    var i=0
    while(i<30){
      message.channel.send("Destroying")
      i=i+1
    }
  }
  if(message.content ===SecretCode){
    message.delete({timeout: 200})
    message.channel.send("Secret code detected activating code scanner: ")
    message.channel.send("Also I deleted the code cause its too secret to be given to the public")
    message.reply("Please hold")
    message.member.send("Ok so its so secret ill dm you");
    message.member.send("So there is absolutly nothing special about that code yet but ima add that soon");
    message.channel.send("he i DM'ed him the rest so u guys cant see it XD");
  }
}
)


client.login("ODExMjQ5NDE1MDQ1MzgyMTc2.YCvc5A.X2CH5y-RRJDdHM9fc1_QaFrdvFM")