const { Permissions } = require('discord.js');
const { formatClubName, handleError } = require('../helpers')

module.exports = {
    name: 'delete',
    description: `\`\`\`
    Command: c?delete
    Description: Delete a club
    Format: c?delete [clubName]\`\`\`
    `,
    
    async execute(msg, ...args) {
        try {
            if (!msg.member.permissions.has(Permissions.FLAGS.ADMINISTRATOR)) {
                return
            }

            const clubName = formatClubName(args)

            if (!clubName) {
                msg.channel.send(this.description)
                return
            }

            const channel = msg.guild.channels.cache.find(c => c.name === clubName)

            const presRole = msg.guild.roles.cache.find(r => r.name === `${clubName}-president`)
            const promises = [channel?.delete(), presRole?.delete()]

            if (promises.every(p => p === undefined)) {
                msg.channel.send('No club found.')
                return
            }

            await Promise.all(promises);
            msg.channel.send(`Deleted club ${clubName}`)

        } catch (err) {
            msg.channel.send('An error has occurred when trying to delete the club')
            handleError({errno: 2, message: 'Attempt to delete club failed.', args: `c?delete ${args}`})

            return
        }
    }
}