const superagent = require('superagent');
const { MessageEmbed } = require('discord.js');
const settings = require('../assets/settings.json');

module.exports.updateMembers = async (client) => {
    setInterval(async () => {
        let guild = client.guilds.cache.get(settings.guest_ID);
        if(!guild) return;
        let memberCount = guild.channels.cache.get(settings.discordMembers_ID);
        if(!memberCount) return;

        const members = guild.members.cache.size;
        try {
            memberCount.setName(`👤 Members: ${members}`)
        } catch (error) {
            return client.logger.error(error);
        }
    }, 120000);
}

module.exports.updatePlayerCount = async (client) => { 
    setInterval(async () => {
        try {
            let guild = client.guilds.cache.get(settings.guest_ID);
            if(!guild) return;
            let playerCount = guild.channels.cache.get(settings.playerCount_ID)
            if(!playerCount) return;


            const { body } = await superagent.get("https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v0001/?appid=1241100");
            if(!body) return;
            if(body.response.result == 1){
                playerCount.setName(`👥 Players Online: ${body.response.player_count}`)
            } else {
                playerCount.setName(`👥 Players Online: 0`)
            }
        } catch (error) {
            return client.logger.error(error);
        }
    }, 120000)
}


module.exports.updateChangeLog = async (client) => {
    setInterval(async () => {
        try {
            let guild = client.guilds.cache.get(settings.guest_ID);
            if(!guild) return;
            let changeLogChannel = guild.channels.cache.get(settings.changeLog_ID);
            if(!changeLogChannel) return;
            
            let guildData = client.database.fetchGuild(settings.guest_ID)
            let oldGID = guildData.oldChangeLog;

            const { body } = await superagent.get("https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=1241100&count=1&maxlength=300&format=json");
            if(!body) return;
            let info = body.appnews.newsitems[0]

            if(oldChangeLog != info.title){
                let desc = info.contents.split(';')

                let embed = new MessageEmbed()
                    .setColor('BLUE')
                    .setThumbnail('https://img.gg.deals/5d/6d/093ef3c336ad32cdc21ebf2dedad47f91fbc_307xt176.jpg')
                    .setTitle(info.title)
                    .setDescription(desc[0])
                    .setURL(info.url)
                changeLogChannel.send({ embeds: [embed ]})

                guildData.oldChangeLog = info.title;
                await guildData.save();
            }
        } catch (error) {
            return client.logger.error(error);
        }
    }, 120000)
}