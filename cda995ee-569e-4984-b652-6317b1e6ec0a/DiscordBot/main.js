const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = 'n!'

client.once('ready', () => {
    console.log('Asami is online?');
});

client.on('message', message =>{
    if(!message.content.startsWith(prefix || message.author.bot)) return;
    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();
    
    if(command === 'ping'){
        message.channel.send('pong?');
    };
    if(command == 'welcome'){message.channel.send('welcome new people. This server is built for playing OwO bot. I`m the manager here, type ^help for more command')};
    if(command == 'hello'){message.channel.send('hello')};
});

client.login('NzQ0OTE0MDA2MDExMTUwMzk3.XzqJOg.CbIHIQHEvsXbEEdz7SCGWDprXpM');    