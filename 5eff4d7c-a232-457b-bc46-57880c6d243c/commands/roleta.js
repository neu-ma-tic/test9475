const Discord = require("discord.js");

exports.run = (bot, message, args) => {
 var random = Math.floor(Math.random() * (5 - 2 ) + 2);
 if (random === 3){

 let embed = new Discord.MessageEmbed()

 .setDescription(`Rodou o cartucho e você sobreviveu (sortudo)`)
 .setColor('RANDOM')
 .setFooter(`A bala ficou no cartucho ${Math.round(random)}`)

 message.reply(embed)

 }
 else {
 let embed2 = new Discord.MessageEmbed()

 .setDescription(`Rodou o cartucho e te acertou R.I.P`)
 .setColor('RANDOM')
 .setFooter(`A bala estava no cartucho ${Math.round(random)}`)
 
 message.reply(embed2)
 }


}

exports.help = {
 name: 'roleta-russa'
 }