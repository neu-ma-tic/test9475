const express = require("express")
const app = express ()

app.get("/", (req, res) => {
  res.send("hello hell!")
})

app.listen(3000, () => {
  console.log("Project is ready!")
})
let Discord = require ("discord.js")
let client = new Discord.Client()


client.on("message", message => {
 if (message.content === "hi"){
   message.channel.send("Hello There!")
  }
})

client.login("ODU2NjI4NTk0MTA0NTk4NTY5.YNDzjA.og3OTMZq2KW44TNCsuBp7peUniA")
