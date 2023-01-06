module.exports = {
    name : 'giveawayedit',
    category : 'giveaway',
    description : 'Редактиране на активен в момента giveaway',

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

        const duration = args[1]
        if(!duration) return message.channel.send('Моля, въведете валидна продължителност')

        // const winners = args[2]
        const winners = parseInt(args[2]);
        if(!winners) return message.channel.send('Моля, посочете брой на печелившите')

        const prize = args.slice(3).join(" ")
        if(!prize) return message.channel.send('Моля, посочете наградата')

        
        bot.giveaways.edit(giveaway.messageID, {
            // setEndTimestamp: Date.now() + duration,
            addTime: duration,
            newWinnerCount: winners,
            newPrize: prize
        }).then(() => {
            // Here, we can calculate the time after which we are sure that the lib will update the giveaway
            const numberOfSecondsMax = bot.giveaways.options.updateCountdownEvery / 1000;
            message.channel.send('Успех! Подаръкът ще бъде актуализиран след по-малко от ' + numberOfSecondsMax + ' секунди.');
        }).catch((err) => {
            message.channel.send('Ненамерен giveaway за ' + giveaway.messageID + ', моля проверете и опитайте отново');
        });
    }
}