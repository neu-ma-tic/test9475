module.exports = {
  name: 'serverinfo',
  description: 'serverinfo command',
  execute(message) {
    const Discord = require('discord.js');
    let args = message.content.split(" ").slice(0);
    let question = args.slice(1).join(" ");
    let server = message.guild
    let channels = message.guild.channels.cache
    let embed = new Discord.MessageEmbed()
      .setColor('RANDOM')
      .setTitle(`SERVER INFO FOR : ${server.name}`)
      .setThumbnail(message.guild.iconURL())
      .addField(`OWNER`, `${server.owner} \n ID : ${server.ownerID}`, true)
      .addField(`REGION `, `${server.region}`, true)
      .addField('MEMBERS', `${message.guild.memberCount}`, true)
      .addField('TEXT CHANNELS', `${channels.filter(channel => channel.type === 'text').size}`)
      .addField('VOICE CHANNELS', `${channels.filter(channel => channel.type === 'voice').size}`)
    message.channel.send(embed);
  }
}; 
