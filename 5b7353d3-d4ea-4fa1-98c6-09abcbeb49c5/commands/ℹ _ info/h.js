  
const pagination = require('discord.js-pagination');
const Discord = require('discord.js');
const { PREFIX } = process.env;

module.exports = {
	name: 'h',
	aliases: ['h'],
	category: 'ℹ | info',
	description: 'Returns all commands, or one specific command info',
	usage: '[command | alias]',
	run: async (client, message, args) => {
            const General = new Discord.MessageEmbed()
        .setTitle(`__${client.user.username}'s commands__`)
        .setColor('#19a0d6')
        .setDescription(`4ME is a general bot for discord, it has almost everything, there are games, moderation, utlity, leveling, giveaways, and much more!
        If you want to go to the bot's website __[Web](https://rr.noordstar.me/3744709e)__


**\`Use the reactions under to change pages\`**

**__Help pages__**
**Page 2: 🔨 | Moderation**
**Page 3: ☄ | Utlity**`)
        .setTimestamp()


        const Moderation = new Discord.MessageEmbed()
        .setTitle('🔨 __| Moderation__')
        .setColor('#F4900C')
        .setDescription(`**\`ban\`: Ban someone**
**\`clean\`: Clean 1-99 mesagges**
**\`giverole\`: Give role to someone**
**\`kick\`: Kick someone**
**\`slowmode\`: Set slowmode in a channel**
**\`unban\`: Unban someone**`)
        .setTimestamp()


        const Utility = new Discord.MessageEmbed()
        .setTitle('☄ | Utlity')
        .setColor('#8CCAF7')
        .setDescription(`**\`afk\`: Ban someone**
**\`avatar\`: Get your own or someone else's avatar**
**\`binary\`: Ban someone**
**\`corona\`: Ban someone**
**\`decode\`: Ban someone**
**\`hack\`: Fake hack someone**
**\`hug\`: Ban someone**
**\`ig\`: Ban someone**
**\`ship\`: Check your relation with someone**`)
        .setTimestamp()

        const pages = [
                General,
                Moderation,
                Utility
        ]

        const emojiList = ["⬅", "➡"];

        const timeout = '120000';

        pagination(message, pages, emojiList, timeout)
    }, 
};