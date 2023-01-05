const Discord = require("discord.js");
const ms = require("ms")
const Model1 = require("../../modelos/warn_sistem");
const Model2 = require("../../modelos/warn_member");
const Mutedb = require("../../modelos/tempmute");
const WarnConfig = require("../../events/config");
const WarnUp = require("../../events/warnup");
module.exports.run = async (client, message, args) =>{
  if(!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send("no tienes permisos para usar este comando");
  if(!args[0]){
    return message.channel.send(`${message.author}, oye menciona a alguien o pon `+"`establecer`")
  }
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
      var dbmsgModel = await dbMsg.save();
    }catch(err){
      console.log(err)
    }
    }else{
      var dbmsgModel = document;
    }
    if(args[0] === "establecer"){
      if(args[1] === "mute"){
        if(!args[2]){
          return message.channel.send(`${message.author}, Para primero debe poner el número de advertencias para poner el rol y después seleccionar rol y escribe su nombre o la id si pone "false" no se usaran roles en el sistema`)
        }
        if(args[2] === "false"){
          try{
          let form = await dbmsgModel.updateOne({role: false})
          message.channel.send(`${message.author} okay no pondré ningún rol a los muteados`)
          }catch(err){
            console.log(err)
            message.channel.send("perdón ocurrió un error en la base de datos")
          }
        }else{
          let warns = parseInt(args[2]);
          console.log(warns)
          let role = message.mentions.roles.first() || message.guild.roles.cache.get(args[3]) 
          if(!isNaN(warns)){
            if(role){
              try{
                let form = await dbmsgModel.updateOne({
                  role: true,
                  roleTime: warns,
                  roleid: role.id
                });
                message.channel.send(
                  `Bien, se les dará a los miembros el rol **${role.name}** al llegar a las **${warns}** advertencias`
                  );
              }catch(err){
                console.log(err)
                return message.channel.send("perdón, no pude guardar la información en mi base de datos por el error: "+err)
              }
            }else{
              return message.channel.send("perdón el rol no es válido.")
            }
          }else{
            return message.channel.send("El número de advertencias para dar el rol solo lo puedes poner en números.")
          }
        }
      }else if(args[1] === "kick"){
        if(!args[2]){
          return message.channel.send("Dime a cuantas advertencias expulsaré al miembro")
        }
        if(args[2] === "false"){
          try{
            let form = await dbmsgModel.updateOne({ kick: false });
            message.channel.send("bueno, no expulsaré a nadie")
          }catch(err){
            return message.channel.send("hubo un error al meter los datos a la base de datos.")
          }
        }else{
          let warns = parseInt(args[2]);
          if(!isNaN(warns)){
            try{
              let form = await dbmsgModel.updateOne({
                kick: true,
                kicktime: warns
              })
              message.channel.send(`Bien, expulsaré a los miembros que lleguen a ${warns}`)
            }catch(err){
              return message.channel.send("hubo un error al meter los datos a mi base de datos")
            }
          }else{
            return message.channel.send("solo puedes poner las advertencias como numeros")
          }
        }
      }else if(args[1] === "ban"){
        if(!args[2]){
          return message.channel.send("dime a cuantas warns daré el ban")
        }
        if(args[2] === "false"){
          try{
          let form = await dbmsgModel.updateOne({
            ban: false
          })
          return message.channel.send("Esta bien, no daré ban")
          }catch(err){
            return message.channel.send("hubo un error al meter los datos a la db")
          }
        }else{
          let warns = parseInt(args[2])
          if(!isNaN(warns)){
            try{
              let form = await dbmsgModel.updateOne({
                ban: true,
                bantime: warns
              });
              return message.channel.send(`bien, le daré ban al miembro al llegar a las **${warns}** advertencias`)
            }catch(err){
              return message.channel.send("perdon hubo un problema al meter los datos a la db")
            }
          }else{
            return message.channel.send("Pon las advertencias en números.")
          }
        }
      }
      if(args[1] === "temp-mute"){
        if(!args[2]){
          return message.channel.send("Dime a cuantas advertencias dare el muteo temporal.")
        }
        if(args[2] === "false"){
          try{
          var form = await dbmsgModel.updateOne({
            tempmute: false
          })
          message.channel.send("Bien, no dare temp mute")
        }catch(err){
          messsage.channel.sen("Perdon hubo un problema al meter los datos a la base de datos")
        }
        }else{
          let warns = parseInt(args[2])
          let role = message.mentions.roles.first() || message.guild.roles.cache.get(args[3])
          let time = args[4]
          if(!isNaN(warns)){
            if(role){
              if(time){
               try{
                 
                  var form = await dbmsgModel.updateOne({
                    tempmute: true,
                    mutetime: warns,
                    temprole: role.id,
                    times: ms(time)
                  })
                   message.channel.send(`Bien, Muteare temporalmente por ${ms(ms(time))} ah las personas al llegar ah las ${warns} advertencias`)
                }catch(err){
                  console.log(err)
                  return message.channel.send(`Ocurrio un problema al meter los datos a la base de datos`)
                }
              }else{
                return message.channel.send("Dime de cuanto tiempo sera el temp mute")
              }
            }else{
              return message.channel.send("define el rol, rol no valido")
            }
          }else{
            return message.channel.send("pon las advertencias en numeros.")
          }
        }
      }else{
        return message.channel.send("instrucciones: !warn  <mute/kick/ban/temp-mute> <a cuantas advertencias se da oh false> <el rol, solo en caso de mute/temp-mute> <el tiempo  solo en caso de usar temp mute>")
      }
    }else{
      let persona = message.mentions.members.first() || message.guild.members.cache.get(args[0]);
      if(!persona){
        return message.channel.send("a que persona le pongo el warn ?")
      }
      let document = await Model2.findOne({
        guildid: message.guild.id,
        memberid: persona.id
      }).catch(e => console.log(e))
      if(!document){
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
        var dbmsgModel2 = document;
     }
      if(dbmsgModel2){
        try{
          var razon = message.content.split(" ").slice(2).join(" ");
          if(!razon) return message.channel.send("dígame una razón.");

          let { warnings } = dbmsgModel2;
          let warns = warnings+1;
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
          .setDescription(`${message.author} le pusiste una advertencia a **${persona.user.username}**, Razon: ${razon}. Ahora tiene ${warns} advertencias.`)
          .setFooter(message.guild.name)
          .setTimestamp()
          .setColor("GREEN")
          .setAuthor(message.author.username,message.author.displayAvatarURL({dynamic:true}))
          message.channel.send(embed)
          let form = await dbmsgModel2.updateOne({
            warnings: warns
          });
        }catch(err){
          console.log(err);
        }
      }
      WarnConfig.run(message, persona);
    }
  }
module.exports.config = {
  name: "warn",
  aliases: ["advertencia","advertir"],
  cooldown: "",
  description: "Un comando para poner una warn oh configurar el sistema de warns",
  usage: "instrucciones: !warn  @persona/<mute/kick/ban/temp-mute> <a cuantas advertencias se da oh false> <el rol, solo en caso de mute/temp-mute> <el tiempo  solo en caso de usar temp mute>",
  category: "moderación"
}