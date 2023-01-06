const { MessageEmbed } = require('discord.js')
module.exports = {
    name : 'socials',
    category : 'info',
    description : 'Връща социалните мрежи на MoonLabsRP',
    prefix : "!",

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */

    run : async(client, message, args) => {
        // message.channel.send(
        //     "Discord - https://discord.gg/YqN4F6SDQz \n" +
        //     "Youtube -  https://www.youtube.com/channel/UCi4B_IETE7559MAWW0YGpXg/featured \n" +
        //     "Facebook - https://www.facebook.com/MoonLabs-RP-104983011745657 \n" +
        //     "Instagram - https://www.instagram.com/moonlabsrp/ ")


        const embed = new MessageEmbed()
            .setColor('#0099ff')
            .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
            .setTimestamp()
            .setTitle('Name Socials')
            .setDescription(
                "Discord - https://discord.gg/#\n" +
                "Youtube -  https://www.youtube.com/#\n" +
                "Facebook - https://www.facebook.com/#\n" +
                "Instagram - https://www.instagram.com/#/")
            await message.channel.send(embed)
    }
}
