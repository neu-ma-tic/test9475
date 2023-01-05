const { Permissions } = require('discord.js');
const { getIDFromPing, formatClubName, handleError } = require('../helpers')

module.exports = {
    name: 'mute',
    description: `\`\`\`
    Command: c?mute
    Description: Mute member from club channel
    Format: c?mute [user] [clubName]\`\`\`
    `,
    
    async execute(msg, ...args) {
        if (!args?.length) {
            msg.channel.send(this.description)
            return
        }

        const [userInput, ...rest] = args
        const clubName = formatClubName(rest)
        const userID = getIDFromPing(userInput)

        const user = await msg.guild.members.fetch(userID).catch(err => {
            msg.channel.send(`Cannot find user ${userInput}`)
        })
        if (!user) return

        if (!clubName) {
            msg.channel.send(`Please specify a club name`)
            return
        }

        const channel = msg.guild.channels.cache.find(r => r.name === clubName)
        if (!channel) {
            msg.channel.send(`Found no club with name ${clubName}`)
            return
        }

        if (!msg.member.permissions.has(Permissions.FLAGS.ADMINISTRATOR) &&
            (!msg.member.roles.cache.find(r => r.name === `${clubName}-president`))
        ) {
            msg.channel.send(`Only administrators or club presidents can execute this command`)
            return
        }

        channel.permissionOverwrites.edit(user.id, {
            SEND_MESSAGES: false,
        })

        msg.channel.send(`User ${user.displayName} is now muted from ${clubName}`)
    }
}