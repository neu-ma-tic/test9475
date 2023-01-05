
const fs = require('fs');
const Discord = require('discord.js');
const { prefix, token } = require('./config.json');
const client = new Discord.Client();
client.commands = new Discord.Collection();
var http = require('http');
const cooldowns = new Discord.Collection();



http.createServer(function (req, res) {
  res.write("I'm alive");
  res.end();
}).listen(8080);
console.log('I am Online' )

const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	client.commands.set(command.name, command);
}

client.on('message', message => {
	if (!message.content.startsWith(prefix) || message.author.bot) return;

	const args = message.content.slice(prefix.length).trim().split(/ +/);
	const command = args.shift().toLowerCase();

	if (command === 'ping') {
		message.channel.send('Pong.');
	} else if (command === 'beep') {
		message.channel.send('Boop.');
	}
});



client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
  console.log('Active and waiting' )
  client.user.setActivity(` ${client.guilds.cache.size} SERVERS`, {
        type: "WATCHING",
        url: "https://www.twitch.tv/psnoxyt"
    });
});






client.login(token); 
