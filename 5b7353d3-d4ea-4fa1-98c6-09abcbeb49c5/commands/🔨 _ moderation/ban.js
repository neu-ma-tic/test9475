const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'ban',
	category: '🔨 | moderation',
	run: async (client, message, args) => {
		if (!message.member.hasPermission('BAN_MEMBERS')) {
			return message.channel.send('You are unable to ban members');
		}
		if (!args[0]) {
			return message.channel.send('Please mention a user!');
		}

		const member = message.mentions.members.first() || message.guild.members.cache.get(args[0]);

		const reason = args[1] ? args.splice(1).join(' ') : 'No Reason Given';
    const target = message.mentions.members.first()
    if(!target) return message.reply("Please mention someone to ban!");

    if(target.id === message.author.id) {
      return message.reply("You cannot ban yourself!")
    }
    let embed = new MessageEmbed()
    .setTitle("Member Banned!")
    .addField("target", `<@${target.user.id}>`)
    .addField("moderator", `<@${message.author.id}>`)
    .addField("reason", reason)
    .setColor('#d4151f')


		try {
			await member.ban({ reason });
			message.channel.send(`${member} has been banned!`);

      await client.channels.cache.get('936336524075757668').send(embed) 


		} catch (e) {
			return message.channel.send('User is not in the server!');
		}
	},
};
