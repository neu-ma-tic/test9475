const ms = require('ms')
const { MessageEmbed } = require('discord.js')

module.exports = {
    name : 'giveawaystart',
    category : 'giveaway',
    description : 'Стартиране на giveaway',
    usage: '#канал време(20s) победители(2) {име на наградата} {giveaway описание/причина}',

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */

    run : async(bot, message, args) => {
        if(!message.member.hasPermission('MANAGE_MESSAGES')) return message.channel.send('Нямате права за използване на тази команда.')
        
        const channel = message.mentions.channels.first()
        if(!channel) return message.channel.send('Моля, посочете канал')

        const duration = args[1]
        if(!duration) return message.channel.send('Моля, въведете валидна продължителност')

        // const winners = args[2]
        const winners = parseInt(args[2]);
        if(!winners) return message.channel.send('Моля, посочете брой на печелившите')

        // const roleName = args[3]
        // if(!roleName) return message.channel.send('Моля, посочете задължителна роля за участие в giveaway')

        const stringExtractor = extract(['{','}']);
        let extractedArgs = stringExtractor(args.toString().replace(',', ' '));
        if (extractedArgs == null || extractedArgs == []) {
            return message.channel.send('Липсва име на наградата и/или описание на подаръка!')
        }
        let prize = extractedArgs[0].split(',').join(' ');
        let giveawayDescription = extractedArgs[1].split(',').join(' ');

        // const prize = prizeName
        if(!prize) return message.channel.send('Моля, посочете наградата')

        // const giveawaymsg = giveawayDescription
        if(!giveawayDescription) return message.channel.send('Моля, напишете съобщение описващо подаръка.')
        

        // NORMAL GIVEAWAY
        bot.giveaways.start(channel, {
            time : ms(duration),
            winnerCount: winners,
            prize : prize,

            // Only members who have not the "Suspended" role are able to sign into the giveaway and win
            // exemptMembers: (member) => !member.roles.cache.some((r) => r.name !== 'Suspended'),
            // exemptMembers: new Function('member', `return !member.roles.cache.some((r) => r.name === \'${roleName}\')`),
            hostedBy: config.GIVEAWAYS.hostedBy ? message.author : null,
            messages: {
                giveaway: (config.GIVEAWAYS.everyoneMention ? "@everyone\n\n" : '') + ` **${giveawayDescription}**\n\n 🎉🎉 **GIVEAWAY** 🎉🎉`,
                giveawayEnd: (config.GIVEAWAYS.everyoneMention ? "@everyone\n\n" : '') + "🎉🎉 **GIVEAWAY ПРИКЛЮЧИ** 🎉🎉",
                timeRemaining: "Оставащо време **{duration}**",
                inviteToParticipate: "Реагирай с 🎉 за да се присъединиш към giveaway",
                winMessage: `Поздравления, {winners}! Ти спечели **{prize}**! Моля пиши на лично на **${message.author}** за да получиш наградата си!`,
                embedFooter: "Giveaway Време!",
                noWinner: "Не можах да определя победител",
                hostedBy: 'Хостнат от {user}',
                winners: "победители",
                endedAt: 'Приключва на',
                units: {
                    seconds: "секунди",
                    minutes: "минути",
                    hours: 'часове',
                    days: 'дни',
                    pluralS: false
                }
            },
           
        })


        message.channel.send(`Giveaway започва в ${channel}`)
    }
}
function extract([beg, end]) {
    const matcher = new RegExp(`${beg}(.*?)${end}`,'gm');
    const normalise = (str) => str.slice(beg.length, end.length*-1);
    return function(str) {
        return str.match(matcher).map(normalise);
    }
}