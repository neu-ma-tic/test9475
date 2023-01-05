const express = require('express');

const app = express();

const port = 3000;

const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = '?';

const fs = require('fs');

client.commands = new Discord.Collection();

const commandFiles = fs
	.readdirSync('./commands/')
	.filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
	const command = require(`./commands/${file}`);

	client.commands.set(command.name, command);
}

client.once('ready', () => {
	console.log('Botten er online');
});



client.on('message', message => {
	if (!message.content.startsWith(prefix) || message.author.bot) return;

	const args = message.content.slice(prefix.length).split(/ +/);
	const command = args.shift().toLowerCase();

	if (command === 'ping') {
		client.commands.get('ping').execute(message, args);
	} else if (command == 'support') {
		client.commands.get('support').execute(message, args);
	} else if (command == 'staff') {
		client.commands.get('staff').execute(message, args);

};

app.get('/', (req, res) => res.send('Botten er online'));

app.listen(port, () =>
	console.log(`Botten er online på http://localhost:${port}`)
);

client.login(process.env.DISCORD_TOKEN);