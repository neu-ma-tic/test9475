const express = require('express');
const app = express();
app.get('/', (request, response) => {
	const ping = new Date();
	ping.setHours(ping.getHours() - 3);
	console.log(
		`Ping recebido às ${ping.getUTCHours()}:${ping.getUTCMinutes()}:${ping.getUTCSeconds()}`
	);
	response.sendStatus(200);
});
app.listen(process.env.PORT); // Recebe solicitações que o deixa online

const Discord = require('discord.js'); //Conexão com a livraria Discord.js
const client = new Discord.Client(); //Criação de um novo Client
const config = require('./config.json'); //Pegando o prefixo do bot para respostas de comando

client.on("guildMemberAdd", async (member) => { 

  let channel = await client.channels.cache.get("728041550306869280");
  let emoji = await member.guild.emojis.cache.find(emoji => emoji.name === "safadinho");
  if (guild != member.guild) {
    return console.log("Sem boas-vindas pra você! Sai daqui saco pela.");
   } else {
      let message = (`${emoji} Boas vindas ${member.user}, venha conversar e espero que goste do servidor! :) ${emoji}`)
    channel.send(message);
  }
});

client.on('ready', () => {
	let activities = [
			`Utilize ${config.prefix}help para obter ajuda`,
			`${client.guilds.cache.size} servidores!`,
			`${client.channels.cache.size} canais!`,
			`${client.users.cache.size} usuários!`
		],
		i = 0;
	setInterval(
		() =>
			client.user.setActivity(`${activities[i++ % activities.length]}`, {
				type: 'WATCHING' // PLAYING, WATCHING, LISTENING, STREAMING
			}),
		1000 * 60
	);
	client.user
		.setStatus('online') // idle, dnd, online, invisible
		.catch(console.error);
	console.log(
		`Estou online, em ${client.guilds.cache.size} servidores, ${
			client.channels.cache.size
		} canais e ${client.users.cache.size} usuários!`
	);
});

client.on('message', message => {
	if (message.channel.type === 'dm' || message.author.bot) return;
	if (!message.content.toLowerCase().startsWith(config.prefix)) return;
	if (
		message.content.startsWith(`<@!${client.user.id}>`) ||
		message.content.startsWith(`<@${client.user.id}>`)
	)
		return;

	const args = message.content
		.trim()
		.slice(config.prefix.length)
		.split(/ +/g);
	const command = args.shift().toLowerCase();

	try {
		const commandFile = require(`./commands/${command}.js`);
		commandFile.run(client, message, args);
	} catch (err) {
		console.error('Erro:' + err);
	}
});

client.login(process.env.TOKEN); //Ligando o Bot caso ele consiga acessar o token
