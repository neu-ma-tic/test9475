const Discord = require("discord.js")

module.exports.run = async (client, message, args) => {
    
    
const regions = {
	brazil: 'Brazil',
	europe: 'Europe',
	hongkong: 'Hong Kong',
	india: 'India',
	japan: 'Japan',
	russia: 'Russia',
	singapore: 'Singapore',
	southafrica: 'South Africa',
	sydeny: 'Sydeny',
	'us-central': 'US Central',
	'us-east': 'US East',
	'us-west': 'US West',
	'us-south': 'US South'
};
const channels = message.guild.channels.cache;
    
    const embed = new Discord.MessageEmbed()
    .setColor('RANDOM')
    .setThumbnail(message.guild.iconURL({ dynamic: true }))
    .setAuthor('📑 Informações do Servidor')
    .addField('**✨ Nome do Servidor**', `• ${message.guild.name}`)
    .addField('**:computer: ID do Servidor**', `• ${message.guild.id}`)
    .addField('**👑 Dono**', `• ${message.guild.owner.user.tag}`)
    .addField('**🌎 Região**', `• ${regions[message.guild.region]}`)
    .addField('**💬 Canais de texto:**', `• ${channels.filter(channel => channel.type === 'text').size}`)
    .addField('**:busts_in_silhouette: Membros**', `• ${message.guild.memberCount}`)
    .addField('**<:nitro_booster:728467985903255583> Impulsos**', `• ${message.guild.premiumSubscriptionCount || '0'}`)
    .setFooter(`2020 © ${client.user.username}.`)
    .setTimestamp()

    await message.channel.send(embed)
}