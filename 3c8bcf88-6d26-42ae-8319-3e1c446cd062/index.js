const Discord = require('discord.js');
const client = new Discord.Client();
const keepAlive = require('./server.js')
keepAlive()
client.on('ready', () => {
  console.log('joined')
})
client.login(process.env.TOKEN);