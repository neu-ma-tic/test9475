const Discord = require("discord.js");

exports.run = async (client, message, args) => {
  
let user = message.mentions.users.first();
 if (!user) return message.reply('**VocÃª nÃ£o mencionou o usuario que vocÃª quer correr!**').catch(console.error);
 const Corrida = "<@" + message.author.id + ">" 
 const corrida2 = " <@" + user.id + ">"
 var falas = [" fez **200** metros ð ....."," fez **500** metros ð ..........."," fez **800** metros ð .............."," fez **1000** metros ð ................."," fez **1500** metros ð ............................","Explodiu ð¥ ","Bateu e pegou fogo ð¥" ]
 message.channel.send({
 "embed": {
 "title": "ð Corrida",
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