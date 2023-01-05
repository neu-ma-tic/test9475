const Command = require('../../structures/Command');
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed } = require('discord.js');
const pm = require("pretty-ms");

module.exports = class extends Command {
    constructor(client) {
        super(client, {
            name: 'uptime',
            description: 'Shows discord bot uptime',
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
        const botembed = new MessageEmbed()
            .setAuthor({ name: `Uptime of ${this.client.user.username}`, iconURL: this.client.user.displayAvatarURL()})
            .setColor(this.client.colors.maincolor)
            .setDescription(`**${this.client.user.username} has been up for** \`${pm(this.client.uptime, {verbose: true})}\``)
        return interaction.reply({ embeds: [botembed ] })
    }
}