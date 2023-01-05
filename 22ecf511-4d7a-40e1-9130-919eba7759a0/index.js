const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Express app!')
});

app.listen(3000, () => {
  console.log('server started');
});

const Discord = require('discord.js')
const client = new Discord.Client()

const prefix = process.env.prefix


const { GiveawaysManager } = require("discord-giveaways");
const manager = new GiveawaysManager(client, {
storage: "./giveaways.json",
updateCountdownEvery: 5000,
default: {
botsCanWin: false,
exemptPermissions: [],
embedColor: "#ffef08",
reaction: "🎁"
}
});
client.on("ready", () => {
  console.log(`[ - Bot is Online - ]`);
  console.log(`Name Bot : ${client.user.username}`);
  console.log(`Guilds : ${client.guilds.cache.size}`);
  console.log(`Users : ${client.users.cache.size}`);
  console.log(`Channels : ${client.channels.cache.size}`);
  client.user.setActivity(`${prefix}help`, {
    type: "PLAYING"
  });
});

client.giveawaysManager = manager;
client.on("message", message =>{
if(message.content === prefix + "help"){
const embed = new Discord.MessageEmbed()
.setTitle("All Giveaways Commands :")
.setColor("#ffef08")
.setThumbnail(client.user.avatarURL())
.addField(`${prefix}start`, "To Create Giveaway", true)
.addField(`${prefix}reroll`, "To Change new Winner", true)
.addField(`${prefix}end`, "To Ended Giveaway", true)
.addField(`${prefix}delete`, "To Deleted Giveaway", true)
.addField(`${prefix}edit`, "To Edit Giveaway", true)
.setFooter("Developer : !ZombieX#0001")
message.channel.send(embed)
}
})
client.on("message", async message =>{
if(message.content.startsWith(prefix + "start")){
if (!message.guild.member(message.author).hasPermission("ADMINISTRATOR"))
      return message.reply("**You Don't Have ` ADMINISTRATOR ` Permission**");

const ms = require('ms')
    const args = message.content.split(" ")
if(isNaN(args[1]) || !args[2] || !args.slice(3).join(' ')) return message.channel.send(new Discord.MessageEmbed()
.setTitle("❌ Error")
.setColor("RED")
.setDescription(`**Ex:** ${prefix}start 1 10s Nitro`)
)
message.delete()
        client.giveawaysManager.start(message.channel, {
            time: ms(args[2]),
            winnerCount: parseInt(args[1]),
            prize: args.slice(3).join(' '), 
            hostedBy: message.author ,
messages: {
giveaway: "🎁 **¦ ¡RECOMPENSA ACTIVA!**",
giveawayEnded: "🎁 **¦ ¡RECOMPENSA FINALIZADA!**",
timeRemaining: "Tiempo restante: **{duration}**!",
inviteToParticipate: "Reacciona con 🎁 para entrar!",
winMessage: `🥳 ¦ **{winners} has ganado \`{prize}\`**`,
embedColor: "#ffef08", 
embedFooter: "ismaaa__21 Giveaways",
noWinner: "❌ **¦ Sin Ganadores**",
hostedBy: "**Creado por: {user}**",
winners: "ganador(es)", 
endedAt: "Acabado en",
embedColorEnd:"#ffef08",  
units: {
seconds: "segundos",
minutes: "minutos",
hours: "horas",
days: "días",
pluralS: true 
}
}
})
}
})


client.on("message", (message) => {
if(message.content.startsWith(prefix + "reroll")){
if (!message.guild.member(message.author).hasPermission("ADMINISTRATOR"))
      return message.reply("**You Don't Have ` ADMINISTRATOR ` Permission**");
 
const messageID = message.content.split(" ").slice(1).join(" ")
        client.giveawaysManager.reroll(messageID, {
          messages:{
            congrat: `🥳 ¦ **{winners} Has ganado \`{prize}\`**`
          }
        }).then(() => {
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("GREEN")
             .setDescription('✅ ¦ Success! Giveaway rerolled' )
            );
        }).catch((err) => {
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("RED")
             .setDescription('❌ ¦ No giveaway found for ' + messageID + ', please check and try again')
            ) 
            
        });
}
});

client.on("message", (message) => {
if(message.content.startsWith(prefix + "delete")){
  if (!message.guild.member(message.author).hasPermission("ADMINISTRATOR"))
      return message.reply("**You Don't Have ` ADMINISTRATOR ` Permission**");

const messageID = message.content.split(" ").slice(1).join(" ")
client.giveawaysManager.delete(messageID).then(() => {
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("GREEN")
             .setDescription('✅ ¦ Success! Giveaway deleted' )
            );
        }).catch((err) => {
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("RED")
             .setDescription('❌ ¦ No giveaway found for ' + messageID + ', please check and try again')
            ) 
        });
}
});

client.on("message", (message) => {
if(message.content.startsWith(prefix + "end")){
  if (!message.guild.member(message.author).hasPermission("ADMINISTRATOR"))
      return message.reply("**You Don't Have ` ADMINISTRATOR ` Permission**");

const messageID = message.content.split(" ").slice(1).join(" ")
client.giveawaysManager.end(messageID).then(() => {
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("GREEN")
             .setDescription('✅ ¦ Success! Giveaway ended' )
            );
        }).catch((err) => {
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("RED")
             .setDescription('❌ ¦ No giveaway found for ' + messageID + ', please check and try again')
            ) 
        });
}
});
client.on("message", (message) => {
if(message.content.startsWith(prefix + "edit")){
  if (!message.guild.member(message.author).hasPermission("ADMINISTRATOR"))
      return message.reply("**You Don't Have ` ADMINISTRATOR ` Permission**");

const args = message.content.split(" ")
const messageID = args[1]
const des = message.content.split(" ").slice(2).join(" ")
if(!messageID || !des) return message.channel.send(new Discord.MessageEmbed 
.setTitle("❌ ¦ Error")
.setColor("RED")
.setDescription("Ex: !edit 874940332880576592 New Description")
)
client.giveawaysManager.edit(messageID, {
            newPrize: des, 
        }).then(() => {
            const numberOfSecondsMax = client.giveawaysManager.options.updateCountdownEvery / 1000;
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("GREEN")
             .send('✅ ¦ Success! Giveaway will updated in less than ' + numberOfSecondsMax + ' seconds.')
            ) 
            
        }).catch((err) => {
            message.channel.send(
             new Discord.MessageEmbed()
            .setColor("RED")
             .setDescription('❌ ¦ No giveaway found for ' + messageID + ', please check and try again')
            ) 
        });
}
});
client.login(process.env.token).catch(() => {
console.log("Token Invalid")
})