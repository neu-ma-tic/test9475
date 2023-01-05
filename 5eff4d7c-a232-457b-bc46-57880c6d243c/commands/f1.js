const Discord = require("discord.js");

exports.run = async (client, message, args) => {
  
let user = message.mentions.users.first();
 if (!user) return message.reply('**Você não mencionou o usuario que você quer correr!**').catch(console.error);
 const Corrida = "<@" + message.author.id + ">" 
 const corrida2 = " <@" + user.id + ">"
 var falas = [" fez **200** metros 🏎 ....."," fez **500** metros 🏎 ..........."," fez **800** metros 🏎 .............."," fez **1000** metros 🏎 ................."," fez **1500** metros 🏎 ............................","Explodiu 🔥 ","Bateu e pegou fogo 🔥" ]
 message.channel.send({
 "embed": {
 "title": "🏎 Corrida",
 "description": " O " + Corrida + " e" + corrida2 + " **estao disputando uma corrida**" ,
 "color": "65535",
 
 "fields": [
 {
 "name":"Sobre a corrida:",
 "value": "O " + Corrida + "\n" + falas[Math.round(Math.random() * falas.length)] + "\n" + "O " + corrida2 + "\n" + falas[Math.round(Math.random() * falas.length)],
 "inline": false
 }
 ]
 }
 })
 }

/********************/
exports.config = {
 name: 'corrida',
 aliases: ['corrida']
}