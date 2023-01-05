const Discord = require('discord.js')////////Definimos Discord con el paquete discord.js/////
const client = new Discord.Client()/////Definimos el cliente de discord, para hacer eventos y loguearnos con el bot///////////
const { Client, MessageEmbed, Guild } = require('discord.js');////////Definimos estas cosas que luego nos servirán///////
require('dotenv').config();


client.on('message', (message) => {////////Abrimos un evento mensaje////////

  let prefix = '.'/////////Ponemos un prefijo para el bot, por ejemplo yo le puse un "."/////////

  if(message.author.bot) return;/////////Hacemos una condicional, para que si el autor de un mensaje es un bot, no continue con el codigo////////

  if(!message.content.startsWith(prefix)) return;/////////Hacemos una condicional, para que si el mensaje no empieza con el prefijo, no continue con el codigo///////////

  let usuario = message.mentions.members.first() || message.member;/////////Definimos usuario, que seria el autor del mensaje o la primera mencion//////
  const args = message.content.slice(prefix.length).trim().split(/ +/g);
  const command = args.shift().toLowerCase();///////////Definimos args y command que luego nos servirán/////////////

  if(command === 'ping'){/////////Hacemos una prueba de comando, en este caso puse ping/////////
    message.channel.send("pong")//////////Hacemos una respuesta del bot cuando se use este comando, por ejemplo, "pong"/////////
  }

})//////////Cerramos el evento mensaje//////////


const mySecret = process.env['OTEyNzc5NDE1ODM3MDkzOTQ5.YZ06Ew.n5kHQTJAymc3mvwWbcFAb4mfI3o']//////////Aqui pondremos el token, para eso pueden ir a ver mi video y enterarse como///////
client.login(mySecret)//////////////Hacemos que el codigo se loguee con el token del bot/////////////