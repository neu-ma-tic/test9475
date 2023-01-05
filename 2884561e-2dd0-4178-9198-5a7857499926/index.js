const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = '-';

client.once('ready', () => {
		console.log('Admin is now online!')
}

client.on('message', message =>{
	if(!message.content.startsWith(prefix) || message.author.bot ) return;
	
	const args = message.content.slice(prefix.length).split(/ +/);
	const command = args.shift().toLowerCase();
	
	
	if(command === 'ping'){
		message.channel.send('faggot');
	} else if (command == 'youtube'){
		message.channel.send('youtube.com');
}
	
client.login("MzQxMzgwNTM5MDU3NTY5Nzky.WX59Zw.Tzy9mIW4rW7SWkmMrAV8xC2ODrE")
