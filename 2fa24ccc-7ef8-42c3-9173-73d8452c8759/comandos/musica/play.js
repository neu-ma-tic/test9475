const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{
  message.channel.send("si")
  }
module.exports.config = {
  name: "play",
  aliases: ["reproducir","p"],
  cooldown: "3s",
  description: "Reproduce una musica",
  usage: "!play [nombre de la cancion]",
  category: "musica"
}