const { MessageEmbed } = require("discord.js");

module.exports = {
    name: "invite",
    aliases: ["https://discord.com/api/oauth2/authorize?client_id=934843397032787978&permissions=8&scope=bot"],
    category: "info",
    description: "Gives you an invite link for the bot.",
    usage: "invite",
    /**
     * @param {import("discord.js").Client} client Discord Client instance
     * @param {import("discord.js").Message} message Discord Message object
     * @param {String[]} args command arguments
     * @param {Object} settings guild settings
    */
    run: async (client, message, args, settings) => {
        const bicon = client.user.displayAvatarURL();

        const embedMsg = new MessageEmbed()
        .addField("Invite link", `[Invite me to your server!](${process.env.BOT_INVITE_LINK})`)
        .addField("Official Discord server", `[Join my official Discord server!](${process.env.SUPPORT_SERVER_INVITE_LINK})`)
            .setColor("#fabbcc")
            .setThumbnail(bicon);

        return message.channel.send(embedMsg);
    }
};