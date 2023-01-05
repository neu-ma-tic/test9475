const db = require('quick.db')
const ms = require('parse-ms')
const Discord = require('discord.js')

exports.run = async (client, message, args, config) => {


    let timeout = 86400000 // 24 hours in milliseconds, change if you'd like.
    let amount = 500
    // random amount: Math.floor(Math.random() * 1000) + 1;


    let daily = await db.fetch(`daily_${message.author.id}`);

    if (daily !== null && timeout - (Date.now() - daily) > 0) {
        let time = ms(timeout - (Date.now() - daily));

        message.channel.send(`You already collected ur daily reward, you can come back and collect it in **${time.hours}h ${time.minutes}m ${time.seconds}s**!`)
    } else {
    let embed = new Discord.RichEmbed()
    .setAuthor(`Daily`, message.author.displayAvatarURL)
    .setColor("GREEN")
    .setDescription(`**Daily Reward**`)
    .addField(`Collected`, amount)

    message.channel.send(embed)
    db.add(`money_${message.author.id}`, amount)
    db.set(`daily_${message.author.id}`, Date.now())
        
    }

}