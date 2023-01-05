module.exports = {
    name: "stop",
    category: "music",
    description: "Stops playing music.",
    usage: "stop",
    /**
     * @param {import("discord.js").Client} client Discord Client instance
     * @param {import("discord.js").Message} message Discord Message object
     * @param {String[]} args command arguments
     * @param {Object} settings guild settings
    */
    run: async (client, message, args, settings) => {
        const STOP_EMOJI = "⏹️";

        const serverQueue = client.musicGuilds.get(message.guild.id);
        if (!serverQueue) {
            return message.reply("There isn't a song currently playing.")
                .then(m => m.delete({
                    timeout: 5000
                }));
        }

        message.react(STOP_EMOJI)
            .catch((err) => { // Probably don't have permissions to react
                message.channel.send("Stopping...");
            }).finally(() => {
                serverQueue.songs = [];
                client.musicGuilds.delete(message.guild.id);
                serverQueue.voiceChannel.leave();
            });
    }
}