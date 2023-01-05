const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  var mencionado = message.mentions.members.first() || client.users.cache.get(args[0])

  if(!mencionado) return message.channel.send(`${message.author}, digame a quien va ah darle de comer`);

  let text = `**${message.author.username}** le dio de comer ah **${mencionado.user.username}**`;
  if(mencionado.id === message.author.id) return text = `${message.author} esta comiendo`;
  let gif = await gifs.sfw.feed();
  const embed = new Discord.MessageEmbed()
  .setTitle(text)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "feed",
  aliases: ["comida"],
  cooldown: "4s",
  description: "Menciona a algiuen y dale de comer",
  usage: "!feed @persona",
  category: "interacción"
}