const Command = require('../../structures/Command');
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed } = require('discord.js');

module.exports = class extends Command {
    constructor(client) {
        super(client, {
            name: 'avatar',
            description: 'Displays a user\'s avatar',
            category: 'general',
            cooldown: 2,
            userPermissions: [],
            options: [
                {
                    name: "user",
                    description: "The user u want the avatar from.",
                    type: "USER",
                    required: false,
                },
            ],
        });
    }
    /**
     * @param {CommandInteraction} interaction
     * @param {CommandInteractionOptionResolver} options
    */
    async run(interaction, options) {
        const member = options.getMember("user") || interaction.member;

        const embed = new MessageEmbed()
            .setColor(this.client.colors.maincolor)
            .setAuthor({ name: `Avatar for ${member.user.tag}`, iconURL: member.user.displayAvatarURL({dynamic: true})})
            .setImage(member.user.displayAvatarURL({format:'png', dynamic: true, size: 1024}))
        return interaction.reply({ embeds: [embed] })
    }
}