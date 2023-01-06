const discord = require('discord.js')
module.exports = {
    name: "mute",
    description: "Mutes someone",
    run: async(client, message, args) => {
        if(!message.member.hasPermission("MANAGE_MESSAGES")) return message.reply("You do not have permissions");

        const target = message.mentions.members.first()
        if(!target) return message.reply("Please mention someone to mute!");

        if(target.id === message.author.id) {
            return message.reply("You cannot mute yourself!")
        }

        let reason = args.slice(1).join(" ");
        if(!reason) return message.reply("Please give a reason to mute someone!")

        const memberrole = message.guild.roles.cache.find(r => r.name === "Member")
        const mutedrole = message.guild.roles.cache.find(r => r.name === "Muted");
        if(!memberrole) return message.reply("Couldnt find the `Member` role!")
        if(!mutedrole) return message.reply("Couldnt find the `Muted` role!")

        if(target.roles.cache.some(r => r.name === "Muted")) {
            return message.reply("The user is already muted!");
        }
        
        message.channel.send(`<@${target.user.id}> Muted.`)


        let embed = new MessageEmbed()
        .setTitle("Member Muted!")
        .addField("target", `<@${target.user.id}>`)
        .addField("moderator", `<@${message.author.id}>`)
        .addField("reason", reason)
        client.channels.cache.get('936336524075757668').send(embed)
        target.roles.add(mutedrole)
        
    }
}