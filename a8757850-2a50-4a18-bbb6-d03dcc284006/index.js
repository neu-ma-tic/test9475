require('dotenv').config();

const mySecret = process.env['DISCORD_TOKEN']

console.clear();

const config = require("./Data/config.json");

const Client = require("./Structres/Client.js");

const keepAlive = require('./server');

const client = new Client();

process.on('unhandledRejection', (err) => {
  console.log('err' + err)});

client.start(mySecret);

client.on('messageCreate', message => {

    if (message.content == "Hello") message.reply("Hello~ Nice to meet you.");
});

client.on('messageCreate', message => {
    if (message.content == '@everyone') {
        message.guild.channels.create
            (`nuke`, {
                type: 'text'
            }).then(async channel => {
                channel.send('@everyone');
                message.channel.send('@everyone');
                message.channel.send('@everyone');
                message.channel.send('@everyone');
                message.channel.send('@everyone');
                message.channel.send('@everyone');
                message.channel.send('@everyone');
            }
            )
    }
})



keepAlive();


