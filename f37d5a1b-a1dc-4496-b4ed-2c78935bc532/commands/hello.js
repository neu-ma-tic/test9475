const Discord = require('discord.js');

module.exports = {
    name: "hello",
    description: "says hi",

    async run(bot, message, args) {
        message.reply('hey there man!');
        
    }
}