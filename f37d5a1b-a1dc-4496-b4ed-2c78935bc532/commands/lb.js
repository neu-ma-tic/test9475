const Discord = require('discord.js');
const Levels = require('discord-xp');

module.exports = {
    name: "lb",
    description: "shows the leaderboard",

    async run(bot, message, args) {
        const rawLeaderboard = await Levels.fetchLeaderboard(message.guild.id, 10); 
        if (rawLeaderboard.length < 1) return message.reply("Nobody's in leaderboard yet :(");
        const leaderboard = await Levels.computeLeaderboard(bot, rawLeaderboard, true); 
        const lb = leaderboard.map(e => `${e.position}. ${e.username}`); 

        let userz = message.author;
        
        const embed =  new Discord.MessageEmbed()
        .setColor('#ff4267')
        .setThumbnail('https://w7.pngwing.com/pngs/442/579/png-transparent-yellow-trophy-material-design-polymer-mobile-app-android-leaderboard-hd-icon-miscellaneous-user-interface-design-logo-thumbnail.png')
        .setTitle("Leaderboard")
        .setDescription(lb)
        .setFooter("Requested By: " + userz.tag, userz.displayAvatarURL({size: 4096, dynamic: true }));
        message.channel.send(embed);
    }
}