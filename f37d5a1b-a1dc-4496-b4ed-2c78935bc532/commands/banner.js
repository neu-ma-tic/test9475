const Discord = require('discord.js');
const { default: axios } = require('axios');

module.exports = {
    name: "banner",
    description: "displays user banner",

    async run(bot, message, args) {
        let user = message.mentions.users.first() || message.author;

        axios.get(`https://discord.com/api/users/${user.id}`, {
            headers: {
                Authorization: `Bot ` + `ENTER-BOT-TOKEN`
            }
        })
        .then(response => {
            console.log(response);
            
            const { banner, accent_color } = response.data;

            if(banner){
                const extension = banner.startsWith('a_') ? '.gif' : '.png';
                const url = `https://cdn.discordapp.com/banners/${user.id}/${banner}${extension}`;

                const bannerEmbed = new Discord.MessageEmbed()
                .setColor('#ff4267')
                .setTitle(`${user.username}'s Banner`)
                .setURL(url)
                .setImage(url)
                .setFooter("Requested By: " + message.author.tag, message.author.displayAvatarURL({ size: 4096, dynamic: true }));

                message.channel.send(bannerEmbed);
            }
            else {
                message.reply('Banner not found.')
                .then(message => {
                    message.react('🙁');
                });
            }
        });
    }
}