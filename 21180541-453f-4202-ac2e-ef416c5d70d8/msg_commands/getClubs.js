const { MessageEmbed, MessageActionRow, MessageButton, MessageCollector } = require('discord.js');

const [color, allowed, title] = ['#ab00ff', 10, 'c?clubs'] // Allowed -> Default items it shows (change to smaller value to test pagination)
let [search, page, totalPages] = ['', 1, 1]

module.exports = {
    name: 'clubs',
    description: `
    Command: c?clubs
    Description: Returns a list of the existing clubs
    Format: c?clubs [search (optional)] [page]`,

    async execute(msg, ...args) {

        if (!args?.length) {
            // msg.channel.send(this.description);

            let fields = { name: 'help', value: this.description }
            page = 0

            setEmbed({ msg, fields, clubChannels: null, page: 1, actionButton: null, embeddedMessage: null, collectible: false })
            return
        }

        const [inputPage, ...inputSearch] = [/^\d+$/.test(args[args.length - 1]) ? parseInt(args?.pop()) : 1, ...args]

        search = inputSearch?.length > 0 ? inputSearch.join('-') : ''

        // console.log('Normal', msg.guild)
        // console.log('JSON', JSON.parse(JSON.stringify(msg.guild)))
        
        const clubChannels = msg.guild.channels.cache
            .sort()
            .filter(c => c.type === 'GUILD_TEXT' && c.name.endsWith('club') && c.name.indexOf(search) !== -1)
            .map(c => {
                const president = msg.guild.roles.cache.find(r => r.name === `${c.name}-president`)?.members
                    .map(m => `${m.user.tag}`)

                return {
                    name: c.name, president: president?.length ? president : undefined
                }
            })

        totalPages = Math.ceil(clubChannels.length / allowed) || 1
        page = inputPage < 1 ? 1 : (inputPage > totalPages ? totalPages : inputPage)

        const fields = paginate({ clubChannels, page })
        setEmbed({ msg, fields, clubChannels, page, actionButton: null, embeddedMessage: null, collectible: true })
    }
}

// Returns an array with the fields for the current page
const paginate = ({clubChannels, page, ...rest}) => {
    const [start, end] = [(page - 1) * allowed, page * allowed]

    const returnedChannels = clubChannels.slice(start, end)

    return [{ name: title, value: `List of available clubs${search ? ` for the search '${search}'` : ''}:\n\n${returnedChannels.map(c => `Club: ${c.name}. President: ${c.president || 'unset'}`).join('\n')}` }]
}

// Creates / updates an embed message, plus its buttons, and collector sent by the bot
const setEmbed = async ({ msg, fields, clubChannels, page, actionButton, embeddedMessage, collectible, ...rest }) => {
    const needsPagination = !!(totalPages > 1)

    const embed = new MessageEmbed()
        .setColor(color)
        // .setTitle(title)
        // .setAuthor(`Cornflower`, 'https://cdn.discordapp.com/avatars/887481802476912711/5d8acf6398f0cf79344e54533695105c.webp?size=256', 'https://discord.js.org')
        .addFields(
            fields
        )

    if (needsPagination)
        embed.setFooter(`Page ${page} of ${totalPages}`)

    const components = collectible && needsPagination ?
        [new MessageActionRow()
            .addComponents(
                new MessageButton()
                    .setCustomId('TMK-left')
                    .setLabel('◀')
                    .setStyle('SECONDARY')
                    .setDisabled(!(page > 1))
            )
            .addComponents(
                new MessageButton()
                    .setCustomId('TMK-right')
                    .setLabel('▶')
                    .setStyle('SECONDARY')
                    .setDisabled(!(page < totalPages))
                // .setEmoji('833087684691361803')
            )
        ] : null

    // If it's null (first call), send message, otherwise we add an event to listen to the button actions
    if (actionButton) {
        actionButton?.update({ embeds: [embed], components })
    } else if (embeddedMessage && rest.isLastInteraction) {
        // If there was no action button clicked, and there is an embeddedMessage === collector died from timeout
        embeddedMessage.edit({ embeds: [embed], components: [] })
    }
    else {
        const embeddedMessage = await msg.channel.send({ embeds: [embed], components })

        msg.react('✅');

        if (collectible && needsPagination) {
            const collector = embeddedMessage.createMessageComponentCollector({ componentType: 'BUTTON', time: 30000 })

            collector.on('collect', async actionButton => {
                if (actionButton.user.id === msg.author.id) {
                    if (actionButton.customId === 'TMK-left') {
                        page--
                    } else if (actionButton.customId === 'TMK-right') {
                        page++
                    }

                    const fields = paginate({clubChannels, page})
                    setEmbed({ msg, fields, clubChannels, page, actionButton, embeddedMessage, collectible: true })
                } else {
                    actionButton.reply({ content: `These buttons aren't for you!`, ephemeral: true })
                }
            })

            collector.on('end', async collected => {
                setEmbed({ msg, fields, clubChannels, page, actionButton: false, embeddedMessage, collectible: false, isLastInteraction: true })
            })
        }
    }
}

// Collector usage: 
// 1) Create buttons on embed message
// 2) Assign collector to buttons
// 3) Whenever a button is pressed, we update the embed message
// When the collector time dies, remove the buttons that had a collector attached