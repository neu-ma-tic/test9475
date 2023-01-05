const Discord = require("discord.js");

const cliente = require("nekos.life");

const gifs = new cliente();

module.exports.run = async (client, message, args) =>{

  var mencionado = message.mentions.members.first() || client.users.cache.get(args[0])

  if(!mencionado) return message.channel.send(`${message.author}, digame a quien vas ah cariñar`);

  let text = `**${message.author.username}** esta cariñando a **${mencionado.user.username}**`;
  if(mencionado.id === message.author.id) return text = `${message.author} se cariña`;

  if(mencionado.id === client.user.id) return message.chanenl.send(`${message.author} no puedes cariñarme a mi :flushed:`);
  let gif = await gifs.sfw.pat();
  const embed = new Discord.MessageEmbed()
  .setTitle(text)
  .setColor("PURPLE")
  .setImage(gif.url)
  .setFooter(message.guild.name)
  .setTimestamp()
  message.channel.send(embed)
  }
module.exports.config = {
  name: "pat",
  aliases: ["cariñar"],
  cooldown: "5s",
  description: "Cariña a alguien",
  usage: "!pat @persona",
  category: "interacción"
}