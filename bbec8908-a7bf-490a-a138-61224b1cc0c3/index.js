const Discord = require("discord.js");
const Client = new Discord.Client({intents: 513});


// temp prefix
// DO THE COMMAND HANDLER
const PREFIX = "$";


Client.on("ready", ()=>{
  console.log("Client is online.");
});

Client.on("messageCreate", message => {
    if(message.author.bot) return;
  if(!message.content.startsWith(PREFIX)) return;

  
  let args = message.content.substring(PREFIX.length).split(" ")

  switch(args[0]) {
    case "ping":
      message.reply("Pong!");
      break;
    case "purge":
      if(!args[1]) return message.reply("Your missing 1 argument. You need to specify the amount of messages to purge.");
      if(args[1] != parseInt(args[1])) return message.reply("Purge number must be a number.");
      message.delete()
      message.channel.bulkDelete(args[1]);
      break;
  }
})

Client.login("OTU0MzgyODkyNDA0OTY1NDY2.YjSUVQ.acvpn6gmxyGqWkKwFo6R5fM2W-w");