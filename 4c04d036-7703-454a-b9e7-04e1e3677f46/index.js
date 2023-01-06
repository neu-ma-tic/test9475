const Discord = require("discord.js");
const client = new Discord.Client();

client.on("ready", () => {
    console.log("Estoy listo!");
 });
 
 client.on("message", (message) => {
   if(message.content.startsWith("ping")) {
     message.channel.send("pong!");
   }
 
 });
 
 client.login("zg3MzgzOTc4MzE0NDMyNTUz.X9UKeQ.EUB6fcy12L2XxbDfnlVStg-of_4");