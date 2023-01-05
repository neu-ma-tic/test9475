
const express = require("express")
const app = express()
app.get("/", (req, res) => {res.send("...")})

app.listen(3000, () => {console.log("Project is ready!")})

let Discord = require("discord.js")
let client = new Discord.Client()
let TypingChannel = ("803501601997848616")
let DenoChannel = ("803261151982649374")
let Token = ("NzQzNTQ0MjM0NDI2MTA1OTg2.XzWNhw.cZp5VliBypCodXWlqiIeFJii2h0")

client.on("message", message => {
if(message.author.bot) return;{
  if(message.channel.id === DenoChannel)
 message.author.send("test")
}
})
//   console.log(message.author.username,"sent",":",message.content,":")
//   // with async/await:
// async function replyAndLog() {
//   let sent = await message.reply(message.content); // this returns the message you just sent
// }

// // with <Promise>.then():
// message.reply(message.content).then(sent => { // 'sent' is that message you just sent
//   let id = sent.id;
//   console.log(id);
// });
// }
// })
// client.on("message", message => {
// if(message.channel.id == TypingChannel){
// message.author.send(message.content)
// // console.log(message.author.id)
client.login(Token)
