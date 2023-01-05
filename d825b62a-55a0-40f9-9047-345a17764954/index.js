const express = require('express')
const app = express();
const port = 3000

app.get('/', (req, res) => res.send('Yo boi!!'))

app.listen(port, () =>
console.log(`Your app is listening a http://localhost:${port}`)
);

const Discord = require('discord.js');
const {
    prefix,
    token
} = require('./conf/config.json');

const client = new Discord.Client();

client.once('ready', () => {
   console.log(`${client.user.tag}: NOW ONLINE!`)
});

client.login(token);