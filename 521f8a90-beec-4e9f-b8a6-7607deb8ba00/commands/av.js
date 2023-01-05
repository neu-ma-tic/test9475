const {MessageEmbed} = require('discord.js');

module.exports = {
    name: 'av',
    aliases: ['avatar'],
    description: "Show's a users avatar!",
    async execute(client, message, args) {
        const user = message.mentions.users.first() || message.author;

        const embed  = new MessageEmbed()
        .setTitle(`${user.tag}'s Avatar`)
        .setDescription(`[Avatar URL](${user.avatarURL()})`)
        .setImage(user.displayAvatarURL({ dynamic: true, size: 2048}))
        .setTimestamp();

        message.channel.send(embed);
    }
}