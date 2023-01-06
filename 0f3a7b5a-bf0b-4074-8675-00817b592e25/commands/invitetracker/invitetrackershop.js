const { MessageEmbed } = require('discord.js')
module.exports = {
    name : 'invitesshop',
    category : 'invitetracker',
    description : 'Връща това, което потребителят може да купи с покани',
    prefix : "!",

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */

    run : async(client, message, args) => {
        let adminroleId = config.COMMANDS.admin_role_ID;

        const Embed = new MessageEmbed()
            .setColor('#0099ff')
            .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
            .setTimestamp()
            .setTitle('Invite Shop')
            .setDescription("**5** Invites -> \`Custom Phone Number\`\n" +
            "**10** Покани -> \`Персонализиран номер на автомобилна табела\`\n" +
            "**20** Покани -> \`+10 Точки приоритет при опашки при влизане в сървъра\`\n\n" +
            "`More to Come...`\n\n")
            .setFooter(`Requested by ${message.author.tag}`, message.author.displayAvatarURL({ dynamic: true }))
            .addField('How can I get my reward?',`DM some of the <@&${adminroleId}> for more Info!`)
            await message.channel.send(Embed)
    }
}