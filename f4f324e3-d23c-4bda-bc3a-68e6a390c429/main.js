const Discord = require('discord.js');
const client = new Discord.Client();
const keepAlive = require("./server")
const config = require('./config.json')
const command = require('./command')

client.once('ready', () => {
    client.user.setActivity('!help to get help (ez)', { type: 'PLAYING' }) 
	console.log('Ready!');

    //commands

    command(client, ['idiot', 'test'], (message) => {
        message.channel.send('sandwich')
    })
    command(client, 'embed', (message) => {
        const embed = new Discord.MessageEmbed()
           .setTitle('Commands')
           .setColor('#bbdbf3')
           .setDescription('This is the !help command if you did not need help then why are you even here?')
           .addFields(
               { name: 'Commands', value: '!idiot - Gives a "sandwich'}
                


           )
        message.channel.send(embed)
    })
});

keepAlive();
client.login(LOGIN)
