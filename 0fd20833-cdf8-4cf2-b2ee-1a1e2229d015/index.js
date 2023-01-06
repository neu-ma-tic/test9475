const Discord = require("discord.js");
const Client = new Discord.Client();

Client.on("ready", () => {
  console.log('Logged in as ${Client.user.tag}!');
})

Client.on("message", msg => {
  if (msg.content === "ping") {
    msg.reply("pong");
  }
})

Client.login("ODc4NzQzNTI3NzQ2NTgwNTYw.YSFnrw.NAbNSTZbDXSwbC8yAoSbwqFG6yc");