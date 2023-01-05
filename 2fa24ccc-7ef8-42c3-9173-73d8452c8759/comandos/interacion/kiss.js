const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  var mencionado = message.mentions.members.first() || client.users.cache.get(args[0])

  if(!mencionado) return message.channel.send(`${message.author}, digame a quien besara`);

  if(mencionado.id === message.author.id) return message.chanenl.send(`${message.author} no puedes besarte a ti mismo`);

  if(mencionado.id === client.user.id) return message.chanenl.send(`${message.author} no puedes besarme a mi :flushed:`);
  let gif = await gifs.sfw.kiss();
  const embed = new Discord.MessageEmbed()
  .setTitle(`**${message.author.username}** le dio un beso a **${mencionado.user.username}**`)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "kiss",
  aliases: ["besar"],
  cooldown: "5s",
  description: "Besa a alguien uwu",
  usage: "!kiss @persona",
  category: "interacción"
}