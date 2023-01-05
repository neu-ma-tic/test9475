const Command = require("../Structres/Command.js");

module.exports = new Command({
    name: 'ban',
    description: '封鎖一位成員',
    aliases: [],
    permission: "BAN_MEMBERS",
    async run(message, args, client) {
        try {
            const member = message.mentions.users.first();
            if (!member) return message.channel.send("請指定成員")
            if (member) {
                const memberTarget = message.guild.members.cache.get(member.id);
                memberTarget.ban().catch();
                message.channel.send("成員已被封鎖");

            } else { message.channel.send("找不到該成員") };
        }

        catch (error) {
            message.channel.send(error)
        }
    }
})