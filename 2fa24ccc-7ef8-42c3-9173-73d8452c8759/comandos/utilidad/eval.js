const Discord = require("discord.js"); 
module.exports.run = async (client, message, args) => {
if(message.author.id !== "649015003499855894") return message.channel.send("Perdon solo mi creador peude usar este comando");
const codigo = args.join(" ")
if(!codigo){
  const a = new Discord.MessageEmbed()
  .setTitle("Error")
  .setDescription("cherylcan nesecitas decirme algo para evaluarlo")
  .setTimestamp()
  .setFooter(message.author.username)
  message.channel.send(a).then(msg =>{msg.delete({timeout:5000})})
  return a
}
try{
let evaluado = eval(codigo);
const a = new Discord.MessageEmbed()
.setTitle("Eval Brin bot")
.addField("Entrada:", "```js\n"+args.join(" ")+"\n```")
.addField("Salida:", "```js\n"+evaluado+"\n```")
.setColor("YELLOW")
message.channel.send(a).then(msg =>{msg.delete({timeout:10000})})
}catch(err){
  const i = new Discord.MessageEmbed()
  .setTimestamp()
  .setFooter(client.user.username, client.user.displayAvatarURL)
  .addField("Hubo un error con el codigo", "```js\n"+err+"\n```")
  .setColor("RANDOM")
  message.channel.send(i).then(msg =>{msg.delete({timeout:5000})})
  return i
}
}
module.exports.config = {
  name: "eval",
  aliases: ["evaluar"],
  cooldown: "3s",
  description: "Comando para testear codigos",
  usage: "!eval [code]",
  category: "eval"
}