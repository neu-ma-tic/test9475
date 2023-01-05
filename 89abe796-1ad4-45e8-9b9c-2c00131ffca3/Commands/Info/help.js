const { MessageEmbed } = require('discord.js')
const { readdirSync } = require('help')

module.exports = {
    name: 'help',
    aliases: ['h'],
    userPerms: ['SEND_MESSAGES'],
    clientPerms: ['SEND_MESSAGES', 'EMBED_LINKS'],
    description: "Shows all available bot commands.",
    run: async(client, message, args, prefix) => {
        if(!args[0]) {
            let categories = [];

            readdirSync("./Commands/").forEach((dir) => {
                const commands = readdirSync(`./Commands/${dir}/`).filter((file) => file.endsWith(".js"))
            
            const cmds = commands.map((command) => {
                let file = require(`../../Commands/${dir}/${command}`)
                if(!file.name) return "No command name.";

                let name = file.name.replace(".js", "");

                return `\`${name}\``;
            });

            let data = new Object();
            data = {
                name: dir.toUpperCase(),
                value: cmds.lenght === 0 ? "In progress." : cmds.join(" | "),
            };
            categories.push(data);
            })

            const embed = new MessageEmbed()
            .setTitle("Commands")
            .addFields(categories)
            .setDescription(`Use \`${prefix}help\` followed by a command name to get more additional information on a command. for example: \`${prefix}help ping\``)
            .setFooter({
              text: `Requested by ${message.author.tag}`
            })
            .setColor(message.guild.me.displayHexColor);
            return message.channel.send({ embeds: [embed] })
        } else {
            const command = client.commands.get(args[0].toLowerCase()) || client.commands.find((c) => c.aliases && c.aliases.includes(args[0].toLowerCase()));

            if(!command) {
                const embed = new MessageEmbed()
                .setTitle('Not Found')
                .setDescription(`Command not found, Use \`${prefix}help\` for all commands available`)
                .setColor(message.guild.me.displayHexColor);
                return message.channel.send({ embeds: [embed]})
            }
            const embed = new MessageEmbed()
            .setTitle("Command Details")
            .addField("COMMAND:",
            command.name ? `\`${command.name}\`` : "No name for this command"
            )
            .addField("ALIASES:",
            command.aliases ? `\`${command.aliases.join("` `")}\`` : "No aliases for this command."
            )
            .addField("USAGE:",
            command.usage ? `\`${prefix}${command.name} ${command.usage}\`` : `\`${prefix}${command.name}\``
            )
            .addField("DESCRIPTION", command.description ? command.description : "No description for this command."
            )
            .setFooter({
              text: `Requested by ${message.author.tag}`
            })
            .setColor(message.guild.me.displayHexColor);
            return message.channel.send({ embeds: [embed]});
        }
    }
}