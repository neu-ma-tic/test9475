const { MessageEmbed } = require('discord.js')
module.exports = {
    name : 'whitelist',
    category : 'info',
    description : 'Returns More Info how to get whitelist role',
    prefix : "!",

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */
    

    run : async(client, message, args) => {
        const discordrulesChannelId = config.COMMANDS.discord_rules_ID;
        const rulesChannelId = config.COMMANDS.roleplay_rules_ID;
        const applicationanswersId = config.COMMANDS.application_answers_ID;

        // message.channel.send(
        //     `First of all read the ${client.channels.cache.get(discordrulesChannelId).toString()} and ${client.channels.cache.get(rulesChannelId).toString()} . The exam is entirely written. In order to send your answers you need to have an account. Age limit - 16+. Your application will be verified within approximately 16 days.  \n` +
        //     "This is the template for the application -> https://forms.gle/8uLVYfx8A7Wcn9Dm9. We are expecting only serious applications so come up with great story about your character! \n\n" +
        //     `Once you fill it out you can check your answer at our ${client.channels.cache.get(applicationanswersId).toString()} channel. ` +
        //     "MoonLabs Team thanks you for your patience!")


        const embed = new MessageEmbed()
            .setColor('#0099ff')
            .setTitle('Whitelist Информация')
            .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
            .setTimestamp()
            .setDescription(`Преди всичко прочетете ${client.channels.cache.get(discordrulesChannelId).toString()} и ${client.channels.cache.get(rulesChannelId).toString()} . Изпитът е изцяло писмен. За да изпратите отговорите си, трябва да имате Steam и Discord акаунт. Възрастова граница - 16+. Заявлението ви ще бъде проверено в рамките на приблизително 16 дни.  \n` +
            "Това е шаблонът за кандидатстване -> https://forms.gle/3jfZ2JEWAAjN5KTY7. Очакваме само сериозни кандидатури, така че измислете страхотна история за вашия герой! \n\n" +
            `След като го попълните, можете да проверите отговора отговорите на апликацията ви в ${client.channels.cache.get(applicationanswersId).toString()} канал. ` +
            "Екипът на MoonLabs ви благодари за търпението!")
            await message.channel.send(embed)
    }
}
