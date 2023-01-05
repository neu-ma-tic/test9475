module.exports = {
    name: 'purge',
    aliases: ['clear'],
    description: 'This is a command that clears messages',
    async execute(client, message, args) {
        if(!args[0]) return message.reply("Please enter a valid amount of messages to erase");
        if(isNaN(args[0])) return message.reply("Please enter a real number");

        if(args[0] > 1000) return message.reply("You cannot delete more than 1000 messages!");
        if(args[0] < 1) return message.reply("You must delete more than 1 message!");

        await message.channel.messages.fetch({limit: args[0]}).then(messages =>{
            message.channel.bulkDelete(messages);
        })

        await message.channel.send('Your purge has finished!')
    }
}