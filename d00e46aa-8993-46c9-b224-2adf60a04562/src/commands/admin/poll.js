const Command = require('../../structures/Command');
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed } = require('discord.js');
const settings = require('../../assets/settings.json');
const reactions = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹']

module.exports = class extends Command {
    constructor(client) {
        super(client, {
            name: 'poll',
            description: 'Create a discord poll',
            category: 'admin',
            cooldown: 2,
            userPermissions: ['ADMINISTRATOR'],
            options: [
                {
                    name: 'message',
                    description: 'Message.',
                    type: 'STRING',
                    required: true,
                },
                {
                    name: 'choice1',
                    description: 'Choice 1',
                    type: 'STRING',
                    required: true,
                },
                {
                    name: 'choice2',
                    description: 'Choice 2',
                    type: 'STRING',
                    required: true,
                },
                {
                    name: 'choice3',
                    description: 'Choice 3',
                    type: 'STRING',
                    required: false,
                },
                {
                    name: 'choice4',
                    description: 'Choice 4',
                    type: 'STRING',
                    required: false,
                },
                {
                    name: 'choice5',
                    description: 'Choice 5',
                    type: 'STRING',
                    required: false,
                },
                {
                    name: 'choice6',
                    description: 'Choice 6',
                    type: 'STRING',
                    required: false,
                },
                {
                    name: 'choice7',
                    description: 'Choice 7',
                    type: 'STRING',
                    required: false,
                },
                {
                    name: 'choice8',
                    description: 'Choice 8',
                    type: 'STRING',
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
        let message = options.getString("message");
        let pollsChannel = interaction.guild.channels.cache.get(settings.polls_ID);

        let ops = [];

        options._hoistedOptions.forEach((opt) => {
            if(opt.name != 'message') {
                ops.push(opt)
            }
        })

        let embed = new MessageEmbed()
            .setColor(this.client.colors.maincolor)
            .setTitle(`${message}`)
            .setThumbnail(interaction.guild.iconURL({ dynamic: true}))
            .setDescription(ops.map((opt, i) => `${reactions[i]} - ${opt.name}`).join('\n'))
            .setFooter({ text: `Poll by ${interaction.member.user.tag}`})
        let msg = await pollsChannel.send({ embeds: [embed]})
        for (let i = 0; i < ops.length; i++) await msg.react(reactions[i])

        this.succesMessage(interaction, '', '**Succesfully created a new poll!**')
        return;
    }
}