const Discord = require("discord.js");
const Model = require("../../modelos/warn_member")
module.exports.run = async (client, message, args) =>{
  
  if(!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send(`${message.author}, no tienes permisos para usar este comando`);

  var mencionado = message.mentions.members.first();

  if(!mencionado) return message.channel.send(`${message.author}, dime a que persona que le quitare todas las advertencias`);

  // if(mencionado.id === message.author.id) return message.channel.send(`${message.author}, no puedes quitarte las advertencias a ti mismo`);

  if(mencionado.id === client.user.id) return message.channel.send(`${message.author}, no puedo quitarme las advertencias a mi mismo`);

  let document = await Model.findOne({
     guildid: message.guild.id,
     memberid: mencionado.id 
     }).catch((err) => {})
  if(!document){
    try{
    let form = await new Model({
      guildid: message.guild.id,
      memberid: mencionado.id,
      warnings: 0
    });
    var msgModel = await form.save();
    }catch(err){
      return message.channel.send(`ocurrio un error al meter los datos a la db`)
    }
  }else{
    var msgModel = document
  }
  var { warnings } = msgModel

  if(1 > warnings) return message.channel.send(`${message.author} la persona no tiene ni una advertencia`);

  try{
    let form = await msgModel.updateOne({
      warnings: 0
    })
  }catch(err){
    console.log(err)
    return message.channel.send(`${message.author}, perdon ocurrio un error al meter los datos a la db`)
  }
  const embed = new Discord.MessageEmbed()
  .setTitle("!Quitaste todas las advertencias¡")
  .setAuthor(message.author.username, message.author.displayAvatarURL({dynamic:true}))
  .setDescription(`${message.author} Bien, le quitaste todas las advertencias a ${mencionado.user.username}, haora no tiene ninguna advertencia`)
  .setFooter(message.guild.name)
  .setTimestamp()
  .setColor("GREEN")
  .setThumbnail(message.guild.iconURL({dynamic:true}))

  message.channel.send(embed)

  const md = new Discord.MessageEmbed()
  .setTitle("!Se te quitaron todas las advertencias¡")
  .setAuthor(mencionado.user.username, mencionado.user.displayAvatarURL({dynamic:true}))
  .setDescription(`**${mencionado.user.username}** Se te quitaron todas las advertencias, ahora no tienes ninguna`)
  .setFooter(message.guild.name)
  .setTimestamp()
  .setColor("GREEN")
  .setThumbnail(message.guild.iconURL({dynamic:true}))

  mencionado.send(md).catch((err) =>{})
  }
module.exports.config = {
  name: "clearwarns",
  aliases: ["eliminar_warns"],
  cooldown: "10s",
  description: "Elimina todas las advertencias de un miembro",
  usage: "!clearwarns @persona",
  category: "moderación"
}