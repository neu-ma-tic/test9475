const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{

  const diversion = client.commands.filter(file => file.config.category == "diversión").map(file => file.config.name).join("` **|** `");

  const interacion = client.commands.filter(file => file.config.category == "interacción").map(file => file.config.name).join("` **|** `");

  const moderacion = client.commands.filter(file => file.config.category == "moderación").map(file => file.config.name).join("` **|** `");

  const musica = client.commands.filter(file => file.config.category == "musica").map(file => file.config.name).join("` **|** `");

  const utilidad = client.commands.filter(file => file.config.category == "utilidad").map(file => file.config.name).join("` **|** `");

  const command = client.commands.find(file => file.config.name == args[0]) || client.commands.find(file => file.config.aliases.includes(args[0]));

  if(!args[0] || !command){
    const msg = new Discord.MessageEmbed()
  .setTitle("Ayuda del bot")
  .setAuthor(message.author.username,message.author.displayAvatarURL({dynamic:true}))
  .setColor("GREEN")
  .setFooter(client.user.username)
  .setTimestamp()
  .setDescription(`${message.author.username} se te envio los comandos al privado`)
  message.channel.send(msg)
  const md = new Discord.MessageEmbed()
  .setTitle(`!Comandos de ${client.user.username}¡`)
  .setAuthor(message.author.username,message.author.displayAvatarURL({dynamic:true}))
  .setColor("GREEN")
  .setThumbnail(message.guild.iconURL({dynamic:true,size:2048}))
  .addField("<a:ADS_gameLIFE:801244495068921866> Diversión","`"+diversion+"`")
  .addField("<:staff:801242891543511100> Moderación","`"+moderacion+"`")
  .addField("Interacción","`"+interacion+"`")
  .addField("Música","`"+musica+"`")
  .addField("Utilidad","`"+utilidad+"`")
  .setFooter(`!help <nombre del comando>`)
  .setTimestamp()
  return message.author.send(md)
  }else{
    const help = new Discord.MessageEmbed()
    .setTitle(`¡Información de un comando!`)
    .setAuthor(message.author.username, message.author.displayAvatarURL({dynamic:true}))
    .setDescription(`Informacion del comando ${args[0]}`)
    .addField("Nombre:",command.config.name)
    .addField("Atajos:",command.config.aliases)
    .addField("Cooldown:",command.config.cooldown)
    .addField("Descripción:",command.config.description)
    .addField("Uso:",command.config.usage)
    .addField("categoría:",command.config.category)
    .setThumbnail(message.guild.iconURL({dynamic:true,size:2048}))
    .setFooter(`!help <nombre del comando>`)
    .setTimestamp()
    .setColor("BLUE")
    message.channel.send(help)
  }
  }
module.exports.config = {
  name: "help",
  aliases: ["ayuda"],
  cooldown: "3s",
  description: "comando para pedir ayuda sobre un comando ",
  usage: "!help / !help [comando]",
  category: "help"
}