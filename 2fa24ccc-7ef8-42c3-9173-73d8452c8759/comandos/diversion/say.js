const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{
  if(!args.join(" ")) return message.channel.send(`${message.author} digame qeu tengo que decir`);

  if(args.join(" ").length > 1000) return message.channel.send(`${message.author}, el texto es muy largo`)

  message.channel.send(args.join(" "))
  }
module.exports.config = {
  name: "say",
  aliases: ["decir"],
  cooldown: "3s",
  description: "!Dire algo¡",
  usage: "!say [texto]",
  category: "diversión"
}