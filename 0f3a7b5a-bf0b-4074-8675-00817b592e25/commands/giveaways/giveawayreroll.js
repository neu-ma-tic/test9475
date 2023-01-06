const { MessageEmbed } = require('discord.js')

module.exports = {
    name : 'giveawayreroll',
    category : 'giveaway',
    description : 'Преизбиране на нов победител на giveaway',

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */

    run : async(bot, message, args) => {
        if(!message.member.hasPermission('MANAGE_MESSAGES')) return message.channel.send('Нямате права за използване на тази команда!')
        if(!args[0]) return message.channel.send('Моля, посочете ID на съобщението')

        const giveaway = bot.giveaways.giveaways.find((g) => g.messageID === args[0]);
        if(!giveaway) return message.channel.send('Не можах да намеря дадения giveaway!')

        bot.giveaways.reroll(giveaway.messageID)
            .then(() => {
                message.channel.send("Giveaway рестартиран!");
            })
            .catch(err => {
                console.log(err)
            })
    }
}