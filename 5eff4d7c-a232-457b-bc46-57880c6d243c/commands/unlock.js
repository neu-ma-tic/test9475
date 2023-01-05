const Discord = require("discord.js")

exports.run = (client, message, args) => {

 if (!client.lockit) client.lockit = [];
 if (!message.member.hasPermission("MANAGE_CHANNELS")) return message.reply("**Você nao tem permissão para usar este comando!** "); message.channel.createOverwrite(message.guild.id, {
 SEND_MESSAGES: true
 })
 message.channel.send(`**${message.author} abri este canal, digite b!lock para fecha-lo!**`);
// De unlock só trocar no SEND_MESSAGES: false, para SEND_MESSAGES: null
 };