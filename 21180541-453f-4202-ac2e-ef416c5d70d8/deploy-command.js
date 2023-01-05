const fs = require('fs');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const clientId = process.env.CLIENT_ID
const guildId = process.env.GUILD_ID
const token = process.env.DISCORD_TOKEN

const commands = [];
const commandFiles = fs.readdirSync('./slash_commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(`./slash_commands/${file}`);
	commands.push(command.data.toJSON());
}

const rest = new REST({ version: '9' }).setToken(token);

(async () => {
	try {
		await rest.put(
			Routes.applicationGuildCommands(clientId, guildId),
			{ body: commands },
		);

		console.log('Successfully registered application commands.');
	} catch (error) {
		console.error(error);
	}
})();