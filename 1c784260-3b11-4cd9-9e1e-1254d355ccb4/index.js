const Discord = require('discord.js');
const client = new Discord.Client();

client.login('NzEwOTM0ODQyNjc3NjU3NjUw.Xr7tcw.xAkt9D0ND5fcWwzAKrpGRQmK1_4');

client.once('ready', () => {
  console.log("BOT is successfully Online!");
});

client.on("message", message => {
  if(message.content == "!hello")
  {
    message.channel.send("Hey, I am here. Use !help to see all the available commands!");
  }
});