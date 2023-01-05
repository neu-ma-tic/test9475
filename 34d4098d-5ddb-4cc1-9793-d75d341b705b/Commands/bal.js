const Discord = require('discord.js')
const colors = require('../colors.json')
const client = require('../index.js')
const db = require('quick.db')

module.exports = {
    name: 'bal',
    description: 'Sends you your economy bal',
    usage: 'bal [user]',
    category: 'Economy',
    guildOnly: true,
    async execute(message, args){
        let User = message.mentions.users.first() || message.author;

        let bal = await db.fetch(`money_${message.guild.id}_${User.id}`);
        let bank = await db.fetch(`bank_${message.guild.id}_${User.id}`)
        if (bal === null) bal = 0;
        if (bank === null) bank = 0;


        let balanceEmbed = new Discord.MessageEmbed()
            .setTimestamp()
            .setAuthor(User.tag, User.avatarURL({
                dynamic: true
            }))
            .setColor("BLUE")
            .addField("Coins:", `:moneybag: ${bal}`, true)
            .addField("Bank: ", `:moneybag: ${bank}`, true)
            .addField("Net worth:", `:moneybag: ${bank + bal}`)
        message.channel.send(balanceEmbed)
    }
}