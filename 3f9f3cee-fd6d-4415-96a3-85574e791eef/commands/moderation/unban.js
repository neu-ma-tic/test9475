const { Client, CommandInteraction } = require("discord.js");

module.exports = {
    name: 'unban',
    description: "unban a member",
    userPermission: ["ADMINISTRATOR"],
    options: [
        {
            name: 'userid',
            description: 'user that you want to unban',
            type: 'STRING',
            required: true
        },
    ],

    /** 
     * @param {Client} client 
     * @param {CommandInteraction} interaction
     * @param {String[]} args
     */
    run: async(client, interaction, args) => {
        const userId = interaction.options.getString("userId");

        interaction.guild.members.unban(userId)
        .then((user) => {
            interaction.followUp({
                content: `success unbanned ${user.tag} in this server!`
            });
        })
        .catch(() => {
            interaction.followUp({
                content: "Please specify a valid banned member's id",
            })
        })
    },
};