const express = require("express")
const app = express()

app.get("/",(req,res) => {
    res.send("hello hell!")
})

app.listen(3000, () =>{
  console.log("Project is ready!")
})
let Discord = require("discord.js")
let client = new Discord.Client()

client.on("guildMemberAdd", member => {
 if(member.guild.id === "727128843768299520") {
 client.channels.cache.get("727245422443364383").send(`<a:6041_te_caGE:788381115647131658>Bine ai venit pe server ${member}<a:6041_te_caGE:788381115647131658>
 Te rugam sa citesti regulamentul primit in privat!<a:8663_AtencaoTKF:788381097091268648>
 Only For Gamers iti ureaza distractie placuta <a:dancecoolkids:801754601748824064> `)
 }
})

client.on("ready", () => {
  console.log("Ready")
  client.user.setPresence({activity: {name: "prefix o4g!"}, status:"idle"})
}) 
client.on("message", message => {
  if(message.content === "o4g!creator"){
    message.channel.send("Creat de Movistar")
  }
  if(message.content.startsWith("o4g!a/f")) {
let replies = ["Adevarat", "Fals"] 
message.channel.send(replies[Math.floor(Math.random() * replies.length)]) 
}
if(message.content.startsWith("o4g!da/nu")) {
let replies = ["Da", "Nu"] 
message.channel.send(replies[Math.floor(Math.random() * replies.length)]) 
}
  if (message.content.startsWith("o4g!dm")){
       let user = message.mentions.users.first()
  const bruh = message.content.slice("".length).trim().split(/ +/);
 bruh.shift().toLowerCase().split(" ")[0]
  user.send(bruh.join(" ")) 
message.channel.send(`Mesaj trimis`)   
    }
  if(message.content.startsWith("o4g!say")){

 let sentence = message.content.split(" ");
 sentence.shift();
 sentence = sentence.join(" ");

 message.channel.send(sentence);
}
  if(message.content === "o4g!rules") {
      let embed = new Discord.MessageEmbed()
    .setTitle("Regulament:")
    .setDescription(`
                   <a:Sirenevermelha:801528236613697587> Pentru o bună colaborare te rugăm să citești regulamentul de mai jos:
                   <a:Sirenevermelha:801528236613697587> Folosește un limbaj adecvat și decent atât pe chat cât și pe voice.
                    <a:Sirenevermelha:801528236613697587> Nu posta lucruri irelevante pentru server.
                    <a:Sirenevermelha:801528236613697587> Folosește channel-urile speciale pentru comenzi/poze/discuții.
                    <a:Sirenevermelha:801528236613697587> Atenție la scrisul cu CAPS LOCK/spam pentru că se sancționează automat de către boți. (warn)
                    <a:Sirenevermelha:801528236613697587> Reclamele la alte servere de discord sau alte grupuri de facebook sunt interzise și se sancționează cu restricție sau ban permanent, depinde de abatere!!
                    <a:Sirenevermelha:801528236613697587> Pentru orice neînțelegere/nelămurile vă rugăm să contactați pe cineva din staff (@moderator/@admin) pentru a clarifica situația.
                    `)
    .setColor("RED")
    .setFooter("by Movistar")
    message.channel.send(embed)
  }
  })
client.login("NzcyNjg4OTI5MjIwMDY3MzM4.X5-UpA.gGkSnxmdc-xS-d9dIXalCYxlMwM")