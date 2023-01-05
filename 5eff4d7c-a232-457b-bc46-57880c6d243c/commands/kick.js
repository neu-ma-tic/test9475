const Discord = require("discord.js");
const { MessageEmbed } = require("discord.js");

module.exports = {
  name: "kick",
  category: "moderação",
  description: "Expulsa alguém do servidor",
  usage: "kick <@user> <raeson>",
  run: (client, message, args) => {
    
    if(!message.member.hasPermission("KICK_MEMBERS")) {
      return message.channel.send(`**${message.author.username}**, você não tem permissão pra usar esse comando`)
    }
    
    if(!message.guild.me.hasPermission("KICK_MEMBERS")) {
      return message.channel.send(`**${message.author.username}**, Eu não tenho permissão pra usar esse comando`)
    }
    
    let target = message.mentions.members.first();
    
    if(!args[0]) {
      return message.channel.send(`**${message.author.username}**, Por favor mencione a pessoa que deseja expulsar`)
    }
    
    if(target.id === message.author.id) {
     return message.channel.send(`**${message.author.username}**, Você não pode expulsar você mesmo`)
    }
    
let reason = args.slice(1).join(" ");
    if (!reason) reason = "-";
    
    const embed = new MessageEmbed()
      .setTitle("Membro expulsado")
      .setColor("RANDOM")
      .setThumbnail(target.user.displayAvatarURL)
      .setDescription(
        `Ação : Kick \nRazão: ${reason} \nUsuário: ${target } \nStaff: ${message.member}`
      )
      .setTimestamp();
    
    message.channel.send(embed)
    
    target.kick(args[0]);
    
    
    
  }
}