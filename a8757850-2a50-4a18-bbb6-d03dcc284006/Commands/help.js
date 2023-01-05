const Command = require("../Structres/Command.js");
const Discord = require('discord.js');


module.exports = new Command({
    name: "help",
    description: "我的指令列表",
    aliases:[],
    permission: "SEND_MESSAGES",
    async run(message, args, client) {
const embed = new Discord.MessageEmbed()
.setTitle(`我的指令`)
.setColor('RANDOM')

client.commands.forEach(cmd => {
    embed.addField(`${cmd.name}`, `${cmd.description}`, true) 
})

message.reply({embeds: [embed]})

}})