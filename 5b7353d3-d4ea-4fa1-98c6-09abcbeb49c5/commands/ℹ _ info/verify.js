const { MessageEmbed } = require('discord.js');
const Discord = require('discord.js');
module.exports = {
    name: 'reactionrole',
    description: "Sets up a reaction role message!",
	run: async (client, message, args) => {
        if (!message.member.hasPermission('ADMINISTRATOR')) {
			  return message.channel.send("You can't do that!");
        }
        const channel = '934924226161414155';
        const verifyRole = message.guild.roles.cache.find(role => role.name === "Member");

 
        const verifyEmoji = '✅';
        

        let embed = new Discord.MessageEmbed()
            .setColor('#00f719')
            .setTitle("Gavish & Ron's Server")
            .setDescription(`To get the <@&934874748553400370> role, react ✅`);
            
 
        let messageEmbed = await message.channel.send(embed);
        messageEmbed.react(verifyEmoji);

 
        client.on('messageReactionAdd', async (reaction, user) => {
            if (reaction.message.partial) await reaction.message.fetch();
            if (reaction.partial) await reaction.fetch();
            if (user.bot) return;
            if (!reaction.message.guild) return;
 
            if (reaction.message.channel.id == channel) {
                if (reaction.emoji.name === verifyEmoji) {
                    await reaction.message.guild.members.cache.get(user.id).roles.add(verifyRole);
                    
                    
                }
                
            } else {
                return;
            }
 
        });
 
        client.on('messageReactionRemove', async (reaction, user) => {
 
            if (reaction.message.partial) await reaction.message.fetch();
            if (reaction.partial) await reaction.fetch();
            if (user.bot) return;
            if (!reaction.message.guild) return;
 
 
            if (reaction.message.channel.id == channel) {
                if (reaction.emoji.name === verifyEmoji) {
                    await reaction.message.guild.members.cache.get(user.id).roles.remove(verifyRole);
                }
                
            } else {
                return;
            }
        });
    }
 
}   