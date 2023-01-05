const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{
  message.channel.send("en mantenimiento")
  }
module.exports.config = {
  name: "kick",
  aliases: ["expulsar"],
  cooldown: "10s",
  description: "Expulsa un miembro del servidor!",
  usage: "!kick",
  category: "moderación"
}