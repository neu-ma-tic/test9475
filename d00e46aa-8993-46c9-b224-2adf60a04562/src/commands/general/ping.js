const Command = require('../../structures/Command');
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed } = require('discord.js');

module.exports = class extends Command {
    constructor(client) {
        super(client, {
            name: 'ping',
            description: 'No description provided',
            category: 'general',
            cooldown: 2,
            userPermissions: [],
            options: [],
        });
    }
    /**
     * @param {CommandInteraction} interaction
     * @param {CommandInteractionOptionResolver} options
    */
    async run(interaction, options) {
        let embed = new MessageEmbed()
            .setColor(this.client.colors.maincolor)
            .setAuthor({ name: `Ping of ${this.client.user.username}`, iconURL: this.client.user.displayAvatarURL()})
            .setDescription(`🏓 **Pong:** \`${Math.floor(this.client.ws.ping)}ms\``)
        return interaction.reply({ embeds: [embed] })
    }
}