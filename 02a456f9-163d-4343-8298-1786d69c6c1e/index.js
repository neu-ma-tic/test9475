const express = require('express');
const app = express();
app.get("/", (request, response) => {
  const ping = new Date();
  ping.setHours(ping.getHours() - 3);
  console.log(`Ping recebido às ${ping.getUTCHours()}:${ping.getUTCMinutes()}:${ping.getUTCSeconds()}`);
  response.sendStatus(200);
});
app.listen(process.env.PORT);
const Discord = require("discord.js");
const client = new Discord.Client(); 
const config = require("./config.json"); 


client.on("guildMemberAdd", async (member) => { 

  let guild = await client.guilds.cache.get("875833148213178408");
  let channel = await client.channels.cache.get("875833148213178411");
  
  if (guild != member.guild) {
    return console.log("Sem boas-vindas pra você!");
   } else {
      let embed = await new Discord.MessageEmbed()
      .setColor("#ff84a3")
      .setAuthor(member.user.tag, member.user.displayAvatarURL())
      .setTitle('Boas-vindas')
      .setImage("https://img/sav.gif")
      .setDescription(`**${member.user}**, bem-vindo(a) ao servidor **${guild.name}**! Atualmente estamos com **${member.guild.memberCount} membros**, divirta-se conosco! :heart:
      
      Siga a sav.grp no Instagram: https://www.instagram.com/sav.grp/ `)
      .setThumbnail(member.user.displayAvatarURL({ dynamic: true, format: "png", size: 1024 }))
      .setFooter("Seja Muito Bem Vindo(a)!")
      .setTimestamp();

    channel.send(embed);
  }
});




client.on("guildMemberRemove", async (member) => { 

  let guild = await client.guilds.cache.get("875833148213178408");
  let channel = await client.channels.cache.get("875833148213178411");
  if (guild != member.guild) {
    return console.log("Algum saco pela saiu do servidor. Mas não é nesse, então tá tudo bem :)");
   } else {
      let embed = await new Discord.MessageEmbed()
      .setColor("#ff84a3")
      .setAuthor(member.user.tag, member.user.displayAvatarURL())
      .setTitle('Adeus!')
      .setImage("http://img/sav.gif")
      .setDescription(`**${member.user.username}**, saiu do servidor! :broken_heart:`)
      .setThumbnail(member.user.displayAvatarURL({ dynamic: true, format: "png", size: 1024 }))
      .setFooter("Adeus !")
      .setTimestamp();

    channel.send(embed);
  }
});

client.on('message', message => {
     if (message.author.bot) return;
     if (message.channel.type == 'dm') return;
     if (!message.content.toLowerCase().startsWith(config.prefix.toLowerCase())) return;
     if (message.content.startsWith(`<@!${client.user.id}>`) || message.content.startsWith(`<@${client.user.id}>`)) return;

    const args = message.content
        .trim().slice(config.prefix.length)
        .split(/ +/g);
    const command = args.shift().toLowerCase();

    try {
        const commandFile = require(`./commands/${command}.js`)
        commandFile.run(client, message, args);
    } catch (err) {
    console.error('Erro:' + err);
  }
});

client.login(process.env.TOKEN); 

