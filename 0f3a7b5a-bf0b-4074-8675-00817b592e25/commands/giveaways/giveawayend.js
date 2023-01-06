module.exports = {
    name : 'giveawayend',
    category : 'giveaway',
    description : 'Приключване на активен giveaway',

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */

    run : async(bot, message, args) => {
        if(!message.member.hasPermission('MANAGE_MESSAGES')) return message.channel.send('Нямате права за използване на тази команда!')
        if(!args[0]) return message.channel.send('Моля, посочете ID на съобщението.')

        const giveaway = bot.giveaways.giveaways.find((g) => g.messageID === args[0]);
        if(!giveaway) return message.channel.send('Не можах да намеря дадения giveaway.')


        // bot.giveaways.edit(giveaway.messageID, {
        //     setEndTimestamp: Date.now()
        // }).then(()  => {
        //     message.channel.send(`Giveaway wil end in less than ${bot.giveaway.options.updateCountdownEvery / 1000} seconds`)
        // }).catch(err => {
        //     console.log(err)
        //     message.channel.send('An error occured')
        // })

        bot.giveaways.end(giveaway.messageID)
        .then(() => {
            message.channel.send('Успех! Подаряването приключи!');
        }).catch((err) => {
            message.channel.send('Не е намерен giveaway за ' + giveaway.messageID + ', моля, проверете и опитайте отново');
        });
        
    }
}