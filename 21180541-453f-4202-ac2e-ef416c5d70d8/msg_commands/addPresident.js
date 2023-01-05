const { Permissions } = require('discord.js');
const { getIDFromPing, formatClubName, handleError } = require('../helpers')

module.exports = {
    name: 'president',
    description: `\`\`\`
    Command: c?president
    Description: Set specified user as president of club
    Format: c?president [user] [clubName]\`\`\`
    `,

    async execute(msg, ...args) {
        if (!msg.member.permissions.has(Permissions.FLAGS.ADMINISTRATOR)) {
            return
        }

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

        const presRole = msg.guild.roles.cache.find(r => r.name === `${clubName}-president`)
        if (!presRole) {
            msg.channel.send(`Found no club with name ${clubName}`)
            return
        }

        // Remove current president
        presRole.members.forEach(member => {
            member.roles.remove(presRole.id)
        })

        user.roles.add(presRole)

        await msg.channel.send(`user ${user.displayName} is now president of ${rest.join(' ')}`)
    }
}