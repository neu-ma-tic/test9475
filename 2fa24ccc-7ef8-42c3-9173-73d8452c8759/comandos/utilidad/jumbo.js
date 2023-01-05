const Discord = require("discord.js");

module.exports.run = async (client, message, args) =>{
  if(!args[0]) return message.channel.send(`${message.author}, dime el emoji que agrandare`);

  var emojiid = Discord.Util.parseEmoji(args[0])

  if(emojiid.id === null) return message.channel.send(`${message.author}, emoji no valido`)

  var emoji = `https://cdn.discordapp.com/emojis/${emojiid.id}.${(emojiid.animated ? 'gif' : 'png')}`

  message.channel.send(emoji)
  }
module.exports.config = {
  name: "jumbo",
  aliases: ["agrandar"],
  cooldown: "5s",
  description: "Agranda un emoji",
  usage: "!jumbo [emoji]",
  category: "utilidad"
}