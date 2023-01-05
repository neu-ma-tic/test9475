//Stats Command but with fero-ms
const feroms = require('fero-ms')
const Command = require("../Structres/Command.js");
const Discord = require('discord.js')

module.exports = new Command({
    name: "stats",
    description: "顯示我的機器人資訊",
    aliases: [],
    permission: "SEND_MESSAGES",
    async run(message, args, client) {


        let totalSeconds = message.client.uptime / 1000;
        const days = Math.floor(totalSeconds / 86400);
        totalSeconds %= 86400;
        const hours = Math.floor(totalSeconds / 3600);
        totalSeconds %= 3600;
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = Math.floor(totalSeconds % 60);

        const uptime = `\`\`\`${days} days, ${hours} hours, ${minutes} minutes and ${seconds} seconds\`\`\``;


        // let uptime = client.uptime
        // const shortenedUptime = `\`\`\`${feroms.ms(uptime)}\`\`\``;

        const embed = new Discord.MessageEmbed()
            .setTitle(`${message.client.user.username} Stats`)
            .addFields(
                { name: "使用Arjuna機器人伺服器的數量:", value: `\`\`\`${client.guilds.cache.size}\`\`\``, inline: true },
                { name: "使用者數量:", value: `\`\`\`${client.users.cache.size}\`\`\``, inline: true },
                { name: "使用頻道數量", value: `\`\`\`${client.channels.cache.size}\`\`\``, inline: true },
                { name: "更新時間: ", value: uptime, inline: true },
                { name: "延遲:", value: `\`\`\`${Math.round(message.client.ws.ping)} ms\`\`\``, inline: true },
                { name: "RAM使用量: ", value: `\`\`\`${(process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2)} MB\`\`\``, inline: true },
            )
            .setColor("3498DB")

        message.reply({ embeds: [embed] })
    }
})