const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{

  if(!args.join(" ")) return message.channel.send(`${message.author} por favor hasme una pregunta`)
  
  if(args.join(" ").length > 50) return message.channel.send(`${message.author} la pregunta es muy grande, pregunta algo mas pequeño`)

  var options = ["si","no","claro","por supuesto","ne","nel pastel","puede que si","talvez","puede que no","hmm posiblemente","creo que si","creo que no"]
  let respuesta = options[Math.floor(Math.random()*(options.length))]
  const embed = new Discord.MessageEmbed()
  .setTitle("!Respuesta de tu pregunta¡")
  .addField("Pregunta:",args.join(" "))
  .addField("Respuesta:",respuesta)
  .setThumbnail(message.author.displayAvatarURL({dynamic:true,size:2048}))
  .setFooter(message.author.username)
  .setTimestamp()
  .setColor("RANDOM")
  message.channel.send(embed)
  }
module.exports.config = {
  name: "8ball",
  aliases: ["bola8"],
  cooldown: "3s",
  description: "!Preguntame algo¡",
  usage: "!8ball [pregunta]",
  category: "diversión"
}