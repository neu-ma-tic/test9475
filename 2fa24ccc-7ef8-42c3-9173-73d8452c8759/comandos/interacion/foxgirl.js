const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  let gif = await gifs.sfw.foxGirl();
  const embed = new Discord.MessageEmbed()
  .setTitle(`**${message.author.username}** una furrita`)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "fox",
  aliases: ["furra"],
  cooldown: "4s",
  description: "La imagen de una furra random",
  usage: "!furra",
  category: "interacción"
}