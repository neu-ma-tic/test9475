const { MessageEmbed } = require("discord.js")

module.exports = {
    commands: ['unban', 'ub'], // You Can Keep Any Name
    description: 'Unbans A User Using Its ID',  // Optional
    permissions: 'BAN_MEMBERS', // You Can Keep Any Permission
    permissionError: 'Nemáte dostatečné permisse na odbanování!',
    expectedArgs: '+unban User-ID', // Optional

    callback: (message, args) => {

        message.delete()
        const userID = args[0]
        if(!userID) return message.reply('Musíte použít ID Uživatela.') // If User ID Is Not Provided.
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();

        // To See If User Is Banned
        message.guild.fetchBans().then(bans => {
            if(bans.size == 0) return
            let bannedUser = bans.find(b => b.user.id == userID)

            if(bannedUser) { // If User Is Banned Then BOT Will Unban

                const embed =  new MessageEmbed()
                .setTitle('Uživatel byl odbanován')
                .setDescription(`<@${userID}> Byl odbanován`)
                .addField('Uživatelem:', message.author)
                .addField('User ID:', userID)
                .setColor('#313131')

                message.channel.send(embed).then(message.guild.members.unban(bannedUser.user))
            } else {
                message.reply('Nesprávné ID Zabanového uživatele.') // If User Is Not Banned.
                .then(msg => {
                    msg.delete({ timeout: 10000 });
                })
        .catch();
            }
        })


    }
}