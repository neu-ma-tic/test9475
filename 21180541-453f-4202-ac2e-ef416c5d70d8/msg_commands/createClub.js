const { Permissions } = require('discord.js');
const { formatClubName, handleError } = require('../helpers')

module.exports = {
    name: 'create',
    description: `\`\`\`
    Command: c?create
    Description: Create a club with specified name.
    Format: c?create [clubName]\`\`\`
    `,
    
    async execute(msg, ...args) {
        if (!msg.member.permissions.has(Permissions.FLAGS.ADMINISTRATOR)) {
            return
        }

        const clubName = formatClubName(args)

        if (!clubName) {
            msg.channel.send(this.description)
            return
        }

        // Check if the channel exists
        const channels = msg.guild.channels.cache
        
        const clubChannel = channels.find(c => c.type === 'GUILD_TEXT' && c.name === clubName)

        const clubRole = msg.guild.roles.cache.find(r => r.name === `${clubName}-president`)
        if (clubChannel || clubRole) {
            msg.channel.send('There\'s already a club with that name')
            return
        }

        // If the category 'clubs' does not exist, we create it
        const textCategory = channels.find(c => c.type === 'GUILD_CATEGORY' && c.name.toLowerCase() === 'clubs')
        
        let categoryID = textCategory?.id

        if (!textCategory) {
            const category = await msg.guild.channels.create('clubs', {
                type: 'GUILD_CATEGORY',
                permissionOverwrites: [
                    {id: msg.guild.id, deny: ['VIEW_CHANNEL']},
                    {id: msg.author.id, allow: ['VIEW_CHANNEL']},
                ]
            })

            categoryID = category.id
        }
                
        // create the club channel and president role
        const presRole = await msg.guild.roles.create({
            name: `${clubName}-president`,
        }).catch(err => {
            msg.channel.send('Club with specified name is already created')
            console.log(err)
            return
        })
        
        const channel = await msg.guild.channels.create(clubName, {
            type: 'GUILD_TEXT',
            parent: categoryID || null,
            permissionOverwrites: [
                {
                    id: msg.guild.id,
                    deny: [Permissions.FLAGS.VIEW_CHANNEL]
                },
                {
                    id: presRole.id,
                    allow: [Permissions.FLAGS.VIEW_CHANNEL]
                }
            ]
        }).catch(err => {
            msg.channel.send('Failed to create club')
            handleError({errno: 1, message: 'Attempt to create club failed.', args: `c?create ${args}`})

            return
        })

        await msg.channel.send(`Club created`)
    }
}