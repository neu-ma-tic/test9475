const { Permissions } = require('discord.js');
const { getIDFromPing, formatClubName, handleError } = require('../helpers')
const ms = require("ms");

module.exports = {
    name: 'tempmute',
    description: `\`\`\`
    Command: c?tempmute
    Description: Mute member from club channel
    Format: c?tempmute [user] [time] [clubName]
    Valid
    \`\`\`
    `,
    
    async execute(msg, ...args) {
        if (!args?.length) {
            msg.channel.send(this.description)
            return
        }

        const [userInput, dur, ...rest] = args
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

        setTimeout(() => {
            channel.permissionOverwrites.edit(user.id, {
                SEND_MESSAGES: true,
            }).then(()=> {
                msg.channel.send(`User ${user.displayName} is now unmuted from ${clubName}`)
            }).catch(err => {
                return
            })
        }, ms(dur))

        msg.channel.send(`User ${user.displayName} is now muted from ${clubName} for ${dur}`)
    }
}