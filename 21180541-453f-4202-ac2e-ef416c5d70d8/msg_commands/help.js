const fs = require('fs')
const { Collection } = require('discord.js')

const commands = new Collection()
const commandFiles = fs.readdirSync('./msg_commands').filter(file => (file.endsWith('.js') && !file.endsWith('help.js')))
for (const file of commandFiles) {
	const command = require(`./${file}`);
	// Set a new item in the Collection
	// With the key as the command name and the value as the exported module
	commands.set(command.name, command);
}

module.exports = {
    name: 'help',
    
    async execute(msg, input) {

        const command = commands.get(input)
        if (!command) {
            // no arguments, listing commands
            const commandList = [...commands.keys()].sort()
            let message = `\`\`\`List of available commands:`
            for (const commandName of commandList) {
                message = `${message}\nc?${commandName}`
            }
            message = `${message}\`\`\``
            msg.channel.send(message)
            return
        }
        msg.channel.send(command.description)
    }
}