const fs = require('fs')
const { Collection } = require('discord.js')

const commands = new Collection()

const commandFiles = fs.readdirSync('./slash_commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(`./slash_commands/${file}`);
	// Set a new item in the Collection
	// With the key as the command name and the value as the exported module
	commands.set(command.data.name, command);
}

module.exports = commands