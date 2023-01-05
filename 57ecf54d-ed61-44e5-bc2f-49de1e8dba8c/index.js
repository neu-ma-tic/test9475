const express = require('express');
const app = express();
const port = 3000;

 
app.get('/', function(request, response){ response.send(`Монитор активен. Локальный адрес: http://localhost:${port}`); });
app.listen(port, () => console.log());
const Discord = require('discord.js');
const client = new Discord.Client();

client.on('message', msg =>{
if (msg.content === 'ping')
  {
    msg.reply('Понг!')
  }
});

client.login(process.env.DISCORD_TOKEN);