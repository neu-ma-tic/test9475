const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  let gif = await gifs.sfw.meow();
  const embed = new Discord.MessageEmbed()
  .setTitle(`**${message.author.username}** un bonito gato`)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "cat",
  aliases: ["gato"],
  cooldown: "5s",
  description: "La imagen un gato",
  usage: "!cat",
  category: "interacción"
}