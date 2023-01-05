const client = require('../../index.js');
const { PREFIX } = require('../../config.json');
const db = require('quick.db')
const { MessageEmbed } = require("discord.js")
const Levels = require("discord-xp")

client.on('messageCreate', async message => {

  
 
  
  if(message.author.bot) return;
  if(!message.guild) return;
  let prefix = await db.fetch(`prefix_${message.guild.id}`);
  if(prefix == null) {
    prefix = PREFIX;
  } else {
    prefix = prefix
  }

 

  if(message.content === `<@${client.user.id}>` || message.content === `<@!${client.user.id}>`) {
    const embed = new MessageEmbed()
    .setTitle("You have reached Special Operations Commander#3885")
    .setDescription(`Type ${prefix}help to check out all of my commands!`)
    .setColor("RED")
    .setFooter({
      text: `and pls dont ping me all the time`
    })
    .setThumbnail( message.author.displayAvatarURL({ dynamic: true }))
    message.channel.send({ embeds: [embed] })
    .setTimestamp()
  }
  if(!message.content.startsWith(prefix)) return;
  if(!message.member) message.member = await message.guild.fetchMember(message);
  const args = message.content.slice(prefix.length).trim().split(/ +/g);
  const cmd = args.shift().toLowerCase();
  if(cmd.length == 0) return;
  let command = client.commands.get(cmd)
  if(!command) command = client.commands.get(client.aliases.get(cmd));

  

if(command) {

    //USER PERMISSION
    if(!message.member.permissions.has(command.userPerms || [])) return message.channel.send(`You dont have \`${command.userPerms || []}\` permission`)

    //BOT PERMISSION
    if(!message.guild.me.permissions.has(command.clientPerms || [])) return message.channel.send(`I dont have \`${command.clientPerms || []}\` permission`)
}



 
  if(command) command.run(client, message, args, prefix)
})