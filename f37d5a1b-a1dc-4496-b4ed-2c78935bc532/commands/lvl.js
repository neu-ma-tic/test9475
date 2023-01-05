const Discord = require('discord.js');

const Levels = require('discord-xp');

module.exports = {
    name: "lvl",
    description: "sends level",

    async run(bot, message, args) {

        const target = message.mentions.users.first() || message.author; 
        let user = await Levels.fetch(target.id, message.guild.id); 
        if (!user){ return message.reply("Seems like this user has not earned any xp so far.") } 
        message.reply(`**${target.username}** is currently **Level - ${user.level}** and has **${user.xp} XP**.`);
        
    }
}