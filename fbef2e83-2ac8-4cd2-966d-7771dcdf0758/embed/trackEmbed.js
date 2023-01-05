const { MessageActionRow, MessageSelectMenu } = require('discord.js');

module.exports = {
    trackEmbed: new MessageActionRow()
        .addComponents(
            new MessageSelectMenu()
                .setCustomId('track')
                .setPlaceholder('Select Track')
                .addOptions([
                    {
                        label: 'Pwnable',
                        description: 'like Systme hacking',
                        value: 'pwnable',
                    },
                    {
                        label: 'Reversing',
                        description: 'analysis Program',
                        value: 'reversing',
                    },
                    {
                        label: 'WebHacking',
                        description: 'Hack a Web',
                        value: 'webhacking',
                    }
                ]),
        )
};