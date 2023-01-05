module.exports = {
    name: 'clear',
    description: "Just a command to clear chat",
    async execute(client, message, args) {
        if(!args[0]) return message.reply("How many messages should I clear?");
        if(isNaN(args[0])) return message.reply("Please enter a number.");

        if(args[0] > 200) return message.reply("You cannot clear more than 200 messages.");
        if(args[0] < 1) return message.reply("You have to clear more than one message.");

        await message.channel.messages.fetch({limit: args[0]}).then(messages =>{
            message.channel.bulkDelete(messages);
        }); 
    }
}