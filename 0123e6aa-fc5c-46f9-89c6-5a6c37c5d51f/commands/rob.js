const db = require('quick.db')
const Discord = require('discord.js')

exports.run = async (client, message, args, config) => {


    let user = message.mentions.members.first()
    let targetuser = await db.fetch(`money_${user.id}`) // fetch mentioned users balance
    let author = await db.fetch(`money_${message.author.id}`) // fetch authors balance


    if (!user) {
        return message.channel.send('Sorry, you forgot to mention somebody.')
    }
    if (author < 250) { // if the authors balance is less than 250, return this.
        return message.channel.send(':x: You need atleast 250$ to rob somebody.')
    }

    if (targetuser < 0) { // if mentioned user has 0 or less, it will return this.
        return message.channel.send(`:x: ${user.user.username} does not have anything to rob.`)
    }


    let random = Math.floor(Math.random() * 200) + 1; // random number 200-1, you can change 200 to whatever you'd like


    let embed = new Discord.RichEmbed()
    .setDescription(`${message.author} you robbed ${user} and got away with ${random}!`)
    .setColor("GREEN")
    .setTimestamp()
    message.channel.send(embed)


    db.subtract(`money_${user.id}`, random)
    db.add(`money_${message.author.id}`, random)
}