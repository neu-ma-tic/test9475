const Discord = require("discord.js")

exports.run = async (client, message, args) => {
let totalSeconds = client.uptime / 1000;
  let hours = Math.floor(totalSeconds / 3600);
  totalSeconds %= 3600;
  let minutes = Math.floor(totalSeconds / 60);
  let seconds = totalSeconds % 60;

    const embed = new Discord.MessageEmbed()
    .setColor('RANDOM')
    .setThumbnail(`https://cdn.discordapp.com/avatars/705455105339818034/994cccf3c0dbed18a86b3d401a1c4922.png?size=2048`)
    .setAuthor('🤖 Minhas informações')
    .addField('**<:emoji_5:727170453260730381> Meu Nick**', `• ${client.user.tag}`)
    .addField('**:computer: Meu ID**', `• ${client.user.id}`)
    .addField('**<:emoji_6:727170480188030987> Meu Criador**', `• Dark22⃤#0571`)
    .addField('**:floppy_disk: Host**', `• Uptime Robot`)
    .addField('**<:javascriptnode:727172304605282374> Linguagem**', `• JavaScript`)
    .addField('**:wrench: Prefixo**', `• b!`)
    .addField('**:alarm_clock: Uptime**', `• ${hours.toFixed()} h, ${minutes.toFixed()} m, ${seconds.toFixed()} s`)
    .addField('**:satellite: Ping**', `• ${Math.round(client.ws.ping)} ms`)
    .addField('**:tools: Suporte**', `• https://discord.gg/bYdhGuU`)
    .addField('**<:pepemito:748591338387275888> Servidores**', `• ${client.guilds.cache.size}`)
    .addField('**:busts_in_silhouette: Usuários**', `• ${client.users.cache.size}`)
    .setFooter(`2020 © ${client.user.username}.`)
    .setTimestamp()

    message.channel.send(embed)
}