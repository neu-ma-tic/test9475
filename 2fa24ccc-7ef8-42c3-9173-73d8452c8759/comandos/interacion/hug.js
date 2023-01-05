const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  var mencionado = message.mentions.members.first() || client.users.cache.get(args[0])

  if(!mencionado) return message.channel.send(`${message.author}, digame a quien va a abrazar`);

  if(mencionado.id === message.author.id) return message.chanenl.send(`${message.author} no puedes abrazarte a ti mismo`);
  let gif = await gifs.sfw.hug();
  const embed = new Discord.MessageEmbed()
  .setTitle(`**${message.author.username}** le dio un abrazo a **${mencionado.user.username}**`)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "hug",
  aliases: ["abrazar"],
  cooldown: "5s",
  description: "Dale un abrazo a alguien",
  usage: "!hug @persona",
  category: "interacción"
}