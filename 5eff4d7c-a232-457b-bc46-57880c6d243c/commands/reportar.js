const Discord = require("discord.js")

module.exports.run = async (client, message, args) => {

  let user = message.mentions.users.first();
  let canal = message.guild.channels.cache.find(ch => ch.id === "749040121747341394");

let motivo = args.slice(1).join(" ");
    if (!motivo) motivo = "Nada foi informado!";

  const embed = new Discord.MessageEmbed()
    .setTitle("Nova denúncia na área!")
    .setColor("#FFFFF1")
    .setThumbnail(message.author.displayAvatarURL())
    .addField("Autor:", message.author)
    .addField("Usuário Reportado:", `${user}`)
    .addField("Motivo", motivo)
    .setFooter("ID do Autor: " + message.author.id)
    .setTimestamp()
  await message.channel.send(`${message.author} a denúncia foi enviada com sucesso!`);
  canal.send(embed)
}