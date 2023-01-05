const Event = require("../Structres/Event.js");

const Discord = require("discord.js");

module.exports = new Event("guildMemberRemove", (client, member) => {

    const channel = member.guild.channels.cache.find(c => c.name == "歡迎");

    if (!channel) return;

    const embed = new Discord.MessageEmbed();

    embed
        .setTitle("成員離開")
        .setColor("RED")
        .setAuthor(member.user.tag)
        .setThumbnail(member.user.avatarURL({ dynamic: true }))
        // .setFooter(member.joinedAt.toUTCString())
        .addFields(
            {
                name: "帳號建立時間",
                value: member.user.createdAt.toUTCString(),
                inline: true
            }
            // {
            //     name: "成員加入時間",
            //     value: member.joinedAt.toUTCString(),
            //     inline: true
            // }
        )
        // .setTimestamp(member.joinedTimestamp);

    channel.send({ embeds: [embed] });

});