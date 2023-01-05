const Discord = require("discord.js");
const { MessageEmbed } = require("discord.js");

module.exports = {
  name: "ban",
  category: "moderação",
  description: "Bane alguém do servidor",
  usage: "ban <@user> <raeson>",
  run: (client, message, args) => {
    
    if(!message.member.hasPermission("BAN_MEMBERS")) {
      return message.channel.send(`**${message.author.username}**, você não tem permissão pra usar esse comando`)
    }
    
    if(!message.guild.me.hasPermission("BAN_MEMBERS")) {
      return message.channel.send(`**${message.author.username}**, Eu não tenho permissão pra usar esse comando`)
    }
    
    let target = message.mentions.members.first();
    
    if(!args[0]) {
      return message.channel.send(`**${message.author.username}**, Por favor mencione a pessoa que deseja banir`)
    }
    
    if(target.id === message.author.id) {
     return message.channel.send(`**${message.author.username}**, Você não pode banir você mesmo`)
    }
    
let reason = args.slice(1).join(" ");
    if (!reason) reason = "-";
    
    const embed = new MessageEmbed()
      .setTitle("Membro banido")
      .setColor("RANDOM")
      .setThumbnail(target.displayAvatarURL)
      .setDescription(
        `Ação : Ban \nRazão: ${reason} \nUsuário: ${target } \nStaff: ${message.member}`
      )
      .setTimestamp();
    
    message.channel.send(embed)
    
    message.guild.members.ban(args[0]);
    
    
    
  }
}