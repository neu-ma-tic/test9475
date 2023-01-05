module.exports = {
    name: 'help',
    aliases: [],
    description: 'embed for the help page!',
    execute(client, message, args, Discord) {
        const newEmbed = new Discord.MessageEmbed()
        .setColor('RANDOM')
        .setTitle('Commands!')
        .setDescription('This embed shows what commands the bot can perform')
        .addFields(
            {name: 'Help', value: 'Brings this embed up!'},
            {name: 'Mod', value: '`Brings the help section for moderation commands!`'},
            {name: 'Fun', value: '`Brings the help section for fun commands!`'},
            {name: 'Utility', value: '`Brings  section for utility commands!`'},
            {name: 'Name', value: '`Brings  section for name commands!`'},
            {name: 'Test', value: '`Brings  section for test commands!`'},   
            {name: '-----------------------', value: '‎'},     
        )
        .setFooter('Bot made by ImJari#6285');
        message.channel.send(newEmbed);
    }
}