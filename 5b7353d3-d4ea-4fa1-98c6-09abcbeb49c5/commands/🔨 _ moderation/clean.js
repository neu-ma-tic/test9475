const { MessageEmbed } = require('discord.js');

module.exports = {
    name: "clean",
    description: "Chat Cleaning (Message)",

    async run (client, message, args) {
        if (!message.member.hasPermission('MANAGE_MESSAGES')) {
			return message.channel.send("You can't do that!");
		}

        const amount = args.join(" ");

        if(!amount) return message.reply('Enter how many messages you want to delete')

        if(amount > 100) return message.reply(`You cannot delete more than 100 messages`)

        if(amount < 1) return message.reply(`Wait, you've already deleted it`)

        await message.channel.messages.fetch({limit: amount}).then(messages => {
            message.channel.bulkDelete(messages
    )});


    message.channel.send(`Successfully deleted **${amount}** messages!`).then(msg => msg.delete({ timeout: 3000 }));

    }
}