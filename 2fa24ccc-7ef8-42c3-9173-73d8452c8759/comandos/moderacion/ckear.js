const Discord = require("discord.js");

module.exports.run = (client, message, args) => {
  if(!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send(`${message.author} no tienes permisos para usar este comando.`);
  if(!args[0]) return message.channel.send(`${message.author} ¿ cuantos mensajes elimino ?`);

  var monto = parseInt(args[0])

  if(monto > 100) return message.channel.send(`${message.author} solo puedes eliminar 100 mensajes, si quieres eliminar un monto mayor usa purge`);
  
  if(0 >= monto) return message.channel.send(`${message.author} dime un monto del 1 al 100`);

  message.channel.bulkDelete(monto).catch(a => {
    return message.chnanel.send(`${message.author} no tengo permisos para eliminar mensajes.`)
  })
  const embed = new Discord.MessageEmbed()
  .setTitle("!Se Eliminaron mensajes¡")
  .setDescription(`${message.author} elimino ${monto} mensajes.`)
  .setAuthor(message.author.username,message.author.displayAvatarURL({dynamic:true}))
  .setFooter(message.guild.name)
  .setTimestamp()
  .setColor("BLUE")
  message.channel.send(embed)
}

module.exports.config = {
  name: "clear",
  aliases: ["eliminar","bulkDelete","clean"],
  cooldown: "10s",
  description: "Elimina mensajes en cantidad !",
  usage: "!clear [cantiad de mensajes a eliminar]",
  category: "moderación"
}