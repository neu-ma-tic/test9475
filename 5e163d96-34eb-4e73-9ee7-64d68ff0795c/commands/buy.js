const Discord = require('discord.js')
const db = require('quick.db')

exports.run = async (client, message, args, config) => {


    let author = db.fetch(`money_${message.author.id}`)

    if (args[0] == 'moderator') {
        if (!message.guild.roles.find("name", 'Moderator')) return message.channel.send('I could not find a role by the name of `Moderator`, check with the owners.')
        if (author < 700) return message.channel.send('You need atleast `700$` to purchase the moderator role.') // if the authors balance is less than 700$ return this, since the role costs 700$ in the store
        
        message.guild.members.get(message.author.id).addRole(message.guild.roles.find("name", 'Moderator'))

        db.subtract(`money_${message.author.id}`, 700)
        message.channel.send(message.author.tag + ' You successfully bought the Moderator role for `700$`')
    } else if(args[0] == 'admin') {
        if (!message.guild.roles.find("name", 'Admin')) return message.channel.send('I could not find a role by the name of `Admin`, check with the owners.')
        if (author < 1800) return message.channel.send('You need atleast `1800$` to purchase the admin role.') // if the authors balance is less than 700$ return this, since the role costs 700$ in the store
        message.guild.members.get(message.author.id).addRole(message.guild.roles.find("name", 'Admin')) // get the role & add it

        db.subtract(`money_${message.author.id}`, 1800)
        message.channel.send(message.author.tag + ' You successfully bought the Admin role for `1800$`')
    }





}