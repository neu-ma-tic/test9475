const Discord = require('discord.js');
const client = new Discord.Client();
const config = require("./config.json");

const welcome = require('./commands/Mod/welcome');
const loadCommands = require('./commands/load-commands');

client.once('ready', () => {
    console.log('Ready.')
    
    setInterval(() => {
        const statuses = [
            `twitch.tv/tiltlive`,
        ]

        const status = statuses[Math.floor(Math.random() * statuses.length)]
        client.user.setActivity(status, { type: "WATCHING"}) // WATCHING, STREAMING, LISTENING
    }, 5000)

    welcome(client)
    loadCommands(client)
    
})


// Member count //
client.on("ready", () => {
    const guild = client.guilds.cache.get('996142425397526548');
    setInterval(() => {
        const memberCount = guild.memberCount;
        const channel = guild.channels.cache.get('996469559336898571')
        channel.setName(`👥 Uživatelé: ${memberCount.toLocaleString()}`)
    }, 5000);
});
// Member count //

// AutoRole //
client.on('guildMemberAdd', member => {
    var role = member.guild.roles.cache.find(role => role.name == "🌐︱Uživatel")
    member.roles.add(role);
});
// AutoRole //

client.on('guildMemberAdd', member => {
    const embed = new Discord.MessageEmbed()
      .setColor('#313131')
      .setTitle('Vítej na server 𝙏𝙄𝙇𝙏𝙊𝙑𝙊 𝘿𝙊𝙐𝙋𝙀!')
      .setDescription(`Pokud máš jakékoliv otázky!`)
      .setThumbnail(member.user.displayAvatarURL())
      .addFields(
        { name: 'User:', value: `${member.user.tag}`, inline: true },
        { name: 'ID:', value: `${member.user.id}`, inline: true },
        { name: 'Joined at:', value: `${member.joinedAt}`, inline: true },
      )   
    member.send(embed);
  })

  client.on('message', msg => { 
    if (msg.channel.type === 'dm') {
        channel.send(msg);
    }
 });

client.on('voiceStateUpdate', (old, New) => {
    if(old.id !== client.user.id) return
    if(old.channelID && !New.channelID) client.queue.delete(old.guild.id)
})

client.login(config.token);
