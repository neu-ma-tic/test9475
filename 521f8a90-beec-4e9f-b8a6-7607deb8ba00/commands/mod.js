module.exports = {
    name: 'mod',
    aliases: [],
    description: 'Replies with moderation commands!',
    execute(client, message, args, Discord) {
        const newEmbed = new Discord.MessageEmbed()
        .setTitle('Moderation Commands!')
        .setColor('RANDOM')
        .setDescription('Shows what moderation commands there are!')
        .addFields (
            {name: 'Purge', value: '`Helps clears messages!`'},
            {name: 'Mute', value: '`Mutes a User!`'},
            {name: 'Unmute', value: '`Unmutes a User!`'},
            {name: 'Ban', value: '`Bans a user!`'},
            {name: 'Kick', value: '`Kicks a user!`'},
         )
         .setFooter('Bot made by ImJari#6285')
         message.channel.send(newEmbed)
    }
}