const express = require('express');
const app = express();
const port = 3000;
const config = require('./config.json');
app.get("/", function (request, response) {
response.sendFile(__dirname + '/Pagina.html');});
app.listen(port, () => console.log(`Todo bien, todo correcto :D`));
const Discord = require('discord.js');
const client = new Discord.Client();
client.on('ready', () => {
console.log(`Inciado Como: ${client.user.tag}!`);
client.user.setPresence( {
  
activity: {name: `Viendo sl!help`,
type: "PLAYING"},
status:"online"});})
client.setMaxListeners (200)

//Codigos de regalo :D

//hola
client.on('message', msg => {
  if (msg.author == client.user){return}
  if (msg.author.id == "159985870458322944"){return}
  let message = msg.content.toLowerCase()
  if(message.includes("hola")) {
    msg.reply('Hola :D')
  }});


//Si contiene ejemplo1 o ejemplo2 va a contestar
client.on('message', msg => {
  if (msg.author.bot == client.user){return}
  let message = msg.content.toLowerCase()
  if(message.includes ("ejemplo1") || message.includes("ejemplo2") ) {
    msg.channel.send('te contestesto si pusiste alguna de esas palabras')
  }
});



//Si contiene palabra 1 Y palabra 2 contesta
client.on('message', msg => {
  if (msg.author == client.user){return}
  let message = msg.content.toLowerCase()
  if(message.includes ("palabra1") && message.includes("palabra2")  ) {
    msg.channel.send(` Contesto si escribiste las 2 cosas`)
  }});
 




//Si contiene algunas de estas palabras borra el mensaje
client.on('message', msg => {
  if(msg.content.includes('Puto')
     || msg.content.includes('Gil')
     || msg.content.includes('Maricon')
     || msg.content.includes('Hijo de puta')
     || msg.content.includes('Hijueputa')
    ){msg.delete()
    }});

//Preguntale: ¿Como me llamo?
client.on('message', msg => {
  if (msg.author == client.user){return}
  let message = msg.content.toLowerCase()
  if(message.includes ("como me llamo") ) {
    msg.channel.send(` te llamas ${msg.author} :D`)
  }});

client.login("ODM1MzI2ODUxNDUwNDA0OTM0.YIN0wQ.F1l4Lk7k6JaEW5L3UKZI90lZcnY")