const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'kick',
	category: '🔨 | moderation',
	run: async (client, message, args) => {
		if (!message.member.hasPermission('KICK_MEMBERS')) {
			return message.channel.send('You are unable to kick members');
		}
		if (!args[0]) {
			return message.channel.send('Please mention a user!');
		}

    let reason = args.slice(1).join(" ");
    if(!reason) return message.reply("Please give a reason to mute someone!")

		const member = message.mentions.members.first() || message.guild.members.cache.get(args[0]);
    const target = message.mentions.members.first()
    if(!target) return message.reply("Please mention someone to kick!");
    if(target.id === message.author.id) {
      return message.reply("You cannot kick yourself!")
    } 
    let embed = new MessageEmbed()
    .setTitle("Member Kicked!")
    .addField("target", `<@${target.user.id}>`)
    .addField("moderator", `<@${message.author.id}>`)
    .addField("reason", reason)
    .setColor("red")


		try {
			await member.kick();
			message.channel.send(`${member} has been kicked!`);

      await client.channels.cache.get('936336524075757668').send(embed)
      
		} catch (e) {
			return message.channel.send('User isn\'t in this server!');
		}
	},
};
