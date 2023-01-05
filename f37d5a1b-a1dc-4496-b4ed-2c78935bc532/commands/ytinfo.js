const Discord = require('discord.js');

const  Yt = require('yt-stats');

const  yt = new  Yt('ENTER-YOUR-API-KEY');

module.exports = {
    name: "ytinfo",
    description: "shows youtube channel information",

    async run(bot, message, args) {
        try{
            if(args.length==0){
                message.reply('Please enter a search query.');
            }
            else {
                let searchQuery = Array.from(args).toString().split(',').join(' ');
                let ytget = await yt.getChannel(searchQuery);

                const channelURL = 'https://www.youtube.com/channel/' + ytget.channelID;
                const title = ytget.channelTitle;
                const subscribers = ytget.subscribers; 
                const videoCount = ytget.videos; 
                const thumbnail = ytget.thumbnail; 
                const description = ytget.description; 
                const views = ytget.views; 
                const joinDate = ytget.joinDate;

                let user = message.author;

                let ytEmbed = new Discord.MessageEmbed()
                .setTitle(title)
                .setURL(channelURL)
                .setColor('#ff4267')
                .setThumbnail(thumbnail)
                .addFields(
                    { name: 'Description', value: description },
                    { name: 'Total Views', value: views },
                    { name: 'Subscribers', value: subscribers },
                    { name: 'Video Count', value: videoCount },
                    { name: 'Join Date', value: joinDate }
                )
                .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

                message.channel.send(ytEmbed);
            }

        } catch(error){
            console.error(error);
            message.reply('No results were found unfortunately.')
            .then(message => {
                message.react('🙁');
            });
        }
    }
}