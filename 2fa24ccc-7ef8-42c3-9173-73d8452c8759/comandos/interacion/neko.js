const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  let gif = await gifs.sfw.nekoGif();
  const embed = new Discord.MessageEmbed()
  .setTitle(`**${message.author.username}** un neko/chica gato`)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "neko",
  aliases: ["nekos"],
  cooldown: "5s",
  description: "La imagen de una chica gato random",
  usage: "!neko",
  category: "interacción"
}