module.exports = {
    name: 'help',
    description: 'Just a command to see a list of commands.',
    execute(client, message, args, Discord){
        const helpembed = new Discord.MessageEmbed()
        .setTitle('Help')
        .setColor('#8210B6')
        .addFields(
            {name: '^help', value: 'Just a command to see a list of commands.'},
            {name: '^schedule', value: 'Just a command to see the current schedule for the Anubis Team.'},
            {name: '^image', value: 'Just a command to pick out an image from google. (^image dog)'},
            {name: '^invite', value: 'Just a command to get an invite link for your friends.'},
            {name: '^ping', value: 'Just a command to see if the Anubis Bot is online.'},
            {name: '^rep', value: 'Just a command to give and see a reputation of a player. (Coming Soon)'},
        )

        message.channel.send(helpembed);
    }
        
}