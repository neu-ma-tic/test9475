const commands = require('../commandList')

module.exports = {
    name: 'interactionCreate',
    async execute(interaction) {
        if (!interaction.isCommand()) return

        const command = commands.get(interaction.commandName)
        if (!command) return

        try {
            await command.execute(interaction)
        } catch (err) {
            console.error(err)
            await interaction.reply({
                content: 'There was an error while executing the command!',
                ephemeral: true,
            })
        }
    }
}