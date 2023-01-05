const Discord = require("discord.js");
const ms = require("ms")
const Model1 = require("../modelos/warn_sistem");
const Model2 = require("../modelos/warn_member");
const Mutedb = require("../modelos/tempmute");
//persona = message.member
module.exports.run = async (message, persona) =>{
  console.log(Model2)
  let document = await Model1.findOne({
    guildid: message.guild.id
  }).catch(err => console.log(err))

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
      var dbMsgConfig = await dbMsg.save();
    }catch(err){
      console.log(err)
    }
    }else{
      var dbMsgConfig = document;
    }
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
        var dbMsgUser = await dbMsg.save();
      }catch(err){
        console.log(err)
      }
      }else{
        var dbMsgUser = documento
      }
      console.log(`dbMsgUser:${dbMsgUser}`)
      var { warnings } = dbMsgUser;
      var warns = warnings
      var {
        roleTime,
        roleid,
        kicktime,
        bantime,
        mutetime,
        temprole,
        role,
        kick,
        ban,
        tempmute,
        times
      } = dbMsgConfig;

      let roles = "";
      if(message.guild.id === "798959397375705148"){
        roles="799445905371430932"
      }else{
        roles="807851480311660544"
      }
      console.log(roles)
      if(ban){
        console.log("ban")
        if(warns === 10){
          console.log("ban asion")
          const embed = new Discord.MessageEmbed()
          .setTitle(`!Te Banearon de ${message.guild.name}¡`)
          .setDescription(`Se te dio un **BAN PERMANENTE** por llegar a las **${warnings}** advertencias, si crees que el baneo fue injusto repórtalo con un admin`)
          .setColor("RED")
          .setFooter("Brin bot")
          .setTimestamp()
          .setAuthor(persona.user.username,persona,user.displayAvatarURL({dynamic:true}))

          persona.send(embed).catch(e => {})
          persona.ban()
          console.log("ban completo")
          return embed
        }
      }
      console.log(persona)
      console.log(warns)
      if(warns === 7){
        console.log("mute 7 horas 7 warns")
        const embed = new Discord.MessageEmbed()
        .setTitle(`!Se te muteo en ${message.guild.name}¡`)
        .setDescription(`Se te **MUTEO** en el servidor por 7h porque llegaste a las **${warnings}** advertencias, si crees que fue injusto repórtalo con un admin`)
        .setColor("RED")
        .setFooter("Brin bot")
        .setTimestamp()
        .setAuthor(persona.user.username, persona.user.displayAvatarURL({dynamic:true}))


        persona.send(embed).catch(e => {})
            let mute = new Mutedb({
             guildid: message.guild.id,
             userid: persona.id,
             rolid: roles,
             time: Date.now()+25200000
        });
        console.log("mute 7 horas casi listo")
         persona.roles.add(roles)
         console.log("mute 7 horas exitoso")
        return embed
      }
      if(warns === 5){
        console.log("mute 3 hora 5 warns")

        const embed = new Discord.MessageEmbed()
        .setTitle(`!Se te muteo en ${message.guild.name}¡`)
        .setDescription(`Se te **MUTEO** en el servidor por 3h porque llegaste a las **${warnings}** advertencias, si crees que fue injusto repórtalo con un admin`)
        .setColor("RED")
        .setFooter("Brin bot")
        .setTimestamp()
        .setAuthor(persona.user.username, persona.user.displayAvatarURL({dynamic:true}))

        persona.send(embed).catch(e => {})
            let mute = new Mutedb({
             guildid: message.guild.id,
             userid: persona.id,
             rolid: roles,
             time: Date.now()+10800000
        });
       persona.roles.add(roles)
       console.log("mute 1 hora completo")
       return embed
      }
      if(warns === 3){
        console.log("mute 1 hora 3 warns")
        const embed = new Discord.MessageEmbed()
        .setTitle(`!Se te muteo en ${message.guild.name}¡`)
        .setDescription(`Se te **MUTEO** en el servidor por 1h porque llegaste a las **${warnings}** advertencias, si crees que fue injusto repórtalo con un admin`)
        .setColor("RED")
        .setFooter("Brin bot")
        .setTimestamp()
        .setAuthor(persona.user.username, persona.user.displayAvatarURL({dynamic:true}))

        persona.send(embed).catch(e => {})
            let mute = new Mutedb({
             guildid: message.guild.id,
             userid: persona.id,
             rolid: roles,
             time: Date.now()+3600000
        });
         persona.roles.add(roles)
         console.log("mute 1 hora completo")
         return embed
      }
  }