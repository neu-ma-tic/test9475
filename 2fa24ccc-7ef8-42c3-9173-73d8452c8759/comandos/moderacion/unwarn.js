const Discord = require("discord.js");
const Model = require("../../modelos/warn_member")
module.exports.run = async (client, message, args) =>{
  
  if(!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send(`${message.author} perdon, no tienes permisos para usar este comando`);

  var mencionado = message.mentions.members.first() || client.users.cache.get(args[0])

  if(!mencionado) return message.channel.send(`${message.author}, dime a que persona le quitare una advertencia`);

  if(mencionado.id === message.author.id) return message.channel.send(`${message.author}, no puedes quitarte una advertencia a ti mismo`);

  if(mencionado.id === client.user.id) return message.channel.send(`${message.author}, ¿ quitarme una advertencia ?`);

  let document = await Model.findOne({memberid: mencionado.id});

  if(!document){
    try{
    let pito = await new Model({
     guildid: message.guild.id,
     memberid: mencionado.id,
     warnings: 0
   })
   var msgModel = await pito.save();
   }catch(err){
     console.log(err)
     return message.channel.send(`Perdon, ocurrio un error al meter al meter los datos a la db`);
   }
  }else{
    var msgModel = document
  }
  let { warnings } = msgModel;
  console.log(msgModel)
  if(1 > warnings) return message.channel.send(`${message.author} la persona mencionada tiene menos de 1 advertencia`);
  let warning = warnings-1

  let form = await msgModel.updateOne({
    warnings: warning
  });
  const embed = new Discord.MessageEmbed()
  .setTitle("!Se quito una advertencia¡")
  .setDescription(`${message.author} le quito una advertencia a **${mencionado.user.username}**, haora tiene **${warning}** advertencias.`)
  .setFooter(message.guild.name)
  .setTimestamp()
  .setAuthor(message.author.username,message.author.displayAvatarURL({dynamic:true}))
  .setColor("GREEN")
  message.channel.send(embed)
  const md = new Discord.MessageEmbed()
  .setTitle("!Se te quito una advertencia¡")
  .setDescription(`**${message.author.username}** te quito una advertencia, haora tienes **${warning}** advertencias.`)
  .setFooter(message.guild.name)
  .setTimestamp()
  .setAuthor(mencionado.user.username, mencionado.user.displayAvatarURL({dynamic:true}))
  .setColor("GREEN")
  mencionado.send(md).catch(err =>{})
  }
module.exports.config = {
  name: "unwarn",
  aliases: [],
  cooldown: "10s",
  description: "Quita una warn a un usuario",
  usage: "!unwarn @persona",
  category: "moderación"
}