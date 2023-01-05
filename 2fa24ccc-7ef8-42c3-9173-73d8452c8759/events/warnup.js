const Discord = require("discord.js");
const ms = require("ms")
const Model1 = require("../modelos/warn_sistem");
const Model2 = require("../modelos/warn_member");
// persona = message.member
module.exports.run = async (message, persona, razon) =>{
  console.log(Model2)
  let document = await Model1.findOne({
    guildid: message.guild.id
  }).catch(err => console.log(err))
      console.log(`Document: ${document}`)
  if(!document){
    try{
      let dbMsg = await new Model1({
        guildid: message.guild.id,
        role: false,
        roletime: 0,
        roleid: '0',
        kick: false,
        kicktime: 0,
        ban: false,
        bantime: 0
      });
      var dbmsgModel = await dbMsg.save();
    }catch(err){
      console.log(err)
    }
    }else{
      var dbmsgModel = document;
    }
    console.log(`dbmsgModel: ${dbmsgModel}`)
      let documento = await Model2.findOne({
        guildid: message.guild.id,
        memberid: persona.id
      }).catch(e => console.log(e))
      console.log(`documento: ${documento}`)
      if(!documento){
      try{
        let dbMsg = await new Model2({
          guildid: message.guild.id,
          memberid: persona.id,
          warnings: 0
        });
        var dbmsgModel2 = await dbMsg.save();
      }catch(err){
        console.log(err)
      }
      }else{
        var dbmsgModel2 = documento
      }
      console.log(dbmsgModel2)
      if(dbmsgModel2){
        try{
          let { warnings } = dbmsgModel2;
          let warns = warnings+1
          const md = new Discord.MessageEmbed()
          .setTitle("!Se te puso una advertencia¡")
          .setDescription(`**${persona.user.username}** se te puso una advertencia, ten más cuidado para la próxima y revísate las reglas`)
          .addField("🎈 Staff:",`Brin Bot#3522`)
          .addField("🧨 Razón:",razon)
          .addField("💣 Advertencias",`tienes: ${warns}`)
          .setColor("RED")
          .setFooter("si tienes alguna queja con la warn habla con un mod")
          persona.send(md).catch(err =>{})
          const embed = new Discord.MessageEmbed()
          .setTitle("!Se puso una advertencia¡")
          .setDescription(`**${message.author.username}** no pongas el mismo mensaje 3 veces. Ahora tiene ${warns} advertencias.`)
          .setFooter(message.guild.name)
          .setTimestamp()
          .setColor("GREEN")
          .setAuthor(persona.user.username,persona.user.displayAvatarURL({dynamic:true}))
          message.channel.send(embed)
          let form = await dbmsgModel2.updateOne({
            warnings: warns
          });
        }catch(err){
          console.log(err)
        }
      }
  }