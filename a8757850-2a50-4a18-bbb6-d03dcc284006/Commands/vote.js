const Command = require("../Structres/Command.js");
const Discord = require('discord.js');

module.exports = new Command({
    name: 'vote',
    description: '投票',
    aliases:[],
    permission: "SEND_MESSAGES",

    async run(message, args, client){

        const channel = message.guild.channels.cache.get('channel id here'); //change the channel id to your channel id

        let suggestmessage = args.slice(1).join(' ');

        let suggestembed = new Discord.MessageEmbed()
        .setTitle('投票')
        .setDescription(`${suggestmessage}`)
        .setTimestamp()
        .setFooter(`${message.author.username}`)
        .setColor("RANDOM")
        

        let msg = await message.channel.send({embeds: [suggestembed]});

        msg.react("✅");
        msg.react("❌");


        

    }
});