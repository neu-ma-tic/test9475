const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  let gif = await gifs.sfw.waifu();
  const embed = new Discord.MessageEmbed()
  .setTitle(`**${message.author.username}** una waifu`)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "waifu",
  aliases: [],
  cooldown: "4s",
  description: "Una waifu",
  usage: "!waifu",
  category: "interacción"
}