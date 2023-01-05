import Discord, {Intents} from 'discord.js';

const client = new Discord.Client({
	intents: [
		Intents.FLAGS.GUILDS,
		Intents.FLAGS.GUILD_MESSAGES
	]
});

const token = process.env['TOKEN'];

client.on("ready", () => { 
	console.log(`client ready`) 
});

client.on("messageCreate", (msg) => { 
	if (msg.content === "marco") {
		msg.reply("pollo");
	}
});

client.login(token);
