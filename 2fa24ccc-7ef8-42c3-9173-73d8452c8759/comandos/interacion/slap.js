const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  var mencionado = message.mentions.members.first() || client.users.cache.get(args[0])

  if(!mencionado) return message.channel.send(`${message.author}, digame a quien abofetear`);

  if(mencionado.id === message.author.id) return message.chanenl.send(`${message.author} no puedes pegarte a ti mismo`);

  if(mencionado.id === client.user.id) return message.chanenl.send(`${message.author} ¿porque pegarme :sob: ?`);
  let gif = await gifs.sfw.slap();
  const embed = new Discord.MessageEmbed()
  .setTitle(`**${message.author.username}** le d io una abofeteada a **${mencionado.user.username}**`)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "slap",
  aliases: ["abofetear"],
  cooldown: "5s",
  description: "Abofetea a un miembrro",
  usage: "!slap @persona",
  category: "interacción"
}