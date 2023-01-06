const { MessageEmbed } = require('discord.js');

module.exports = {
    name: "suggest",
    aliases: ["sug"],
	run: async (client, message, args) => {

        const channel = message.guild.channels.cache.get('934896444807200779')
        if (!channel) return message.channel.send(`I could not find a room`)

        if (!args.slice(0).join(" ")) return message.channel.send('Specify what you want to suggest')
    
        const suggestionEmbed = new MessageEmbed()
            .setTitle("New suggestion!")
            .setAuthor(message.author.tag, message.author.displayAvatarURL({ dynamic: true }))
            .setDescription(`${args.slice(0).join(" ")}`)
            .setColor("#ffffff")
            .setTimestamp()

        let msg = await channel.send(suggestionEmbed);
        await msg.react("⬆")
        await msg.react("⬇")

        message.channel.send(`Your advice has been sent to the suggestion room`).then(msg => msg.delete({ timeout: 3000 }));
       
    }
}