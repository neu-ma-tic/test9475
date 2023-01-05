const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{

  if(!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send(`${message.author} no tienes permisos para usar este comando`)

  var mencionado = message.mentions.members.first() || client.users.cache.get(args[0])
  if(!mencionado) return message.channel.send(`${message.author}, menciona ah alguien para banearlo`);

  var razon = message.content.split(" ").slice(2)

  if(!razon) return message.channel.send(`${message.author}, dime alguna razon del baneo`);
  if(razon.join(" ").length > 30) return message.channel.send(`${message.author}, la razon es muy larga dime alguna mas corta`);

  if(mencionado.id === message.author.id) return message.channel.send(`${message.author}, no puedes banearte a ti mismo`);

  if(mencionado.id === client.user.id) return message.channel.send(`${message.author}, no me puedo banear a mi mismo`);
  mencionado.ban();
  const embed = new Discord.MessageEmbed()
  .setTitle("!Se baneo un miembro¡")
  .addField("Mod:",message.author.username)
  .addField("Miembro:",mencionado.user.username)
  .addField("Razon:",razon.join(" "))
  .addField("Tiempo:","no establecido")
  .setFooter(message.guild.name)
  .setTimestamp()
  .setColor("GREEN")
  message.channel.send(embed)
  }
module.exports.config = {
  name: "ban",
  aliases: ["baneo"],
  cooldown: "10s",
  description: "Banea un miembro del servidor !",
  usage: "!ban @persona [razon]",
  category: "moderación"
}