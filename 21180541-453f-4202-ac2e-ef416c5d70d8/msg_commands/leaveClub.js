const { Permissions } = require('discord.js');
const { formatClubName, handleError } = require('../helpers')

module.exports = {
    name: 'leave',
    description: `\`\`\`
    Command: c?leave
    Description: Leave a club.
    Format: c?leave [clubName]\`\`\`
    `,
    
    
    async execute(msg, ...args) {
        const clubName = formatClubName(args)
        if (!clubName) {
            msg.channel.send(this.description)
            return
        }

        const clubChannel = msg.guild.channels.cache.find(channel => channel.name === clubName)

        if (!clubChannel) {
            msg.channel.send(`Cannot find any club with name ${clubName}`)
            return
        }

        clubChannel.permissionOverwrites.edit(msg.member.id, {
            VIEW_CHANNEL: false,
        })

        msg.channel.send(`You have left club ${clubName}`)
    }
}