const settings = require('../assets/settings.json')
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed } = require('discord.js');
const colors = require('../assets/colors.json')

module.exports = class Command {
    constructor(client, options) {
        this.client = client;
        this.name = options.name;
        this.description = options.description || 'No description provided';
        this.category = options.category || '';
        this.cooldown = options.cooldown || 2,
        this.userPermissions = options.userPermissions || ['SEND_MESSAGES'];
        this.options = options.options  || [];
    }
    /**
     * @param {CommandInteraction} interaction
     * @param {CommandInteractionOptionResolver} options
    */
    run(interaction, options){
        throw new Error(`The ${this.name} command has no run method`);
    }

    /**
    * Return a error embed
    * @param {Interaction} interaction
    * @param {String} title
    * @param {String} text
    */
    errorMessage(interaction, title, text) {
        let embed = new MessageEmbed()
            .setColor(colors.errorcolor)
            .setDescription(`${text}`)
        if(title) embed.setTitle(title)
        return interaction.reply({ embeds: [embed] })
    }
    
    /**
    * Return a error embed
    * @param {Interaction} interaction
    * @param {String} title
    * @param {String} text
    */
    succesMessage(interaction, title, text) {
        let embed = new MessageEmbed()
            .setColor(colors.succescolor)
            .setDescription(`${text}`)
        if(title) embed.setTitle(title)
        return interaction.reply({ embeds: [embed] })
    }
}