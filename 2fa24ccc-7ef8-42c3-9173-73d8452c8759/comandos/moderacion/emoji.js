const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{

  if(!args[0]) return message.channel.send(`${message.author} dime que emoji agrego`)

  var emojiid = Discord.Util.parseEmoji(args[0])

  if(emojiid.id === null) return message.channel.send(`${message.author} perdon emoji no valido`)

  var emoji = `https://cdn.discordapp.com/emojis/${emojiid.id}.${(emojiid.animated ? 'gif' : 'png')}`

  message.guild.emojis.create(emoji, emojiid.name)
  const embed = new Discord.MessageEmbed()
  .setTitle("¡Nuevo emoji!")
  .setDescription(`Se creo un emoji con el nombre ${emojiid.name}`)
  .setImage(emoji)
  .setAuthor(message.author.username, message.author.displayAvatarURL({dynamic:true}))
  .setColor("PURPLE")
  message.channel.send(embed)
  }
module.exports.config = {
  name: "emojicreate",
  aliases: ["createemoji","crearemoji"],
  cooldown: "5s",
  description: "Crea un emoji en el servidor !",
  usage: "!emojicreate [emoji]",
  category: "moderación"
}