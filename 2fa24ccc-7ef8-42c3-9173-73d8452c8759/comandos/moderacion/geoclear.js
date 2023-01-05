const Discord = require("discord.js");
const Model = require("../../modelos/warn_member")
module.exports.run = async (client, message, args) =>{
  
  if(!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send(`${message.author}, no tienes permisos para usar este comando`);

  var mencionado = message.mentions.members.first();

  let document = await Model.find();
  if(!document){
    return message.channel.send(`${message.author} no hay ningun usuario almacenado`);
  }
  for(step = 0; step < document.length; step++){
    var datos = document[step];
    let data = await Model.findOne({
        guildid: message.guild.id,
        memberid: datos.memberid
      }).catch(e => console.log(e));
      let pito = await data.updateOne({
        warnings: 0
      });
  }
  
  console.log(document)
  /*
  var { warnings } = msgModel

  if(1 > warnings) return message.channel.send(`${message.author} la persona no tiene ni una advertencia`);

  try{
    let form = await msgModel.updateOne({
      warnings: 0
    })
  }catch(err){
    console.log(err)
    return message.channel.send(`${message.author}, perdon ocurrio un error al meter los datos a la db`)
  }*/
  const embed = new Discord.MessageEmbed()
  .setTitle("!Se elimino todos los usuarios con warns¡")
  .setAuthor(message.author.username, message.author.displayAvatarURL({dynamic:true}))
  .setDescription(`${message.author} Bien, Todos los usuarios con advertencias haora no tienen ni una`)
  .setFooter(message.guild.name)
  .setTimestamp()
  .setColor("GREEN")
  .setThumbnail(message.guild.iconURL({dynamic:true}))

  message.channel.send(embed)
/*
  const md = new Discord.MessageEmbed()
  .setTitle("!Se te quitaron todas las advertencias¡")
  .setAuthor(mencionado.user.username, mencionado.user.displayAvatarURL({dynamic:true}))
  .setDescription(`**${mencionado.user.username}** Se te quitaron todas las advertencias, ahora no tienes ninguna`)
  .setFooter(message.guild.name)
  .setTimestamp()
  .setColor("GREEN")
  .setThumbnail(message.guild.iconURL({dynamic:true}))

  mencionado.send(md).catch((err) =>{})*/
  }
module.exports.config = {
  name: "geoclear",
  aliases: ["geoeliminacion"],
  cooldown: "5s",
  description: "Elimina todas las advertencias de todos los usuarios",
  usage: "!geoclear",
  category: "moderación"
}