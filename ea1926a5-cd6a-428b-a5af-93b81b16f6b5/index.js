const express = require("express");
const app = express();

app.listen(3000, () => {
  console.log("Project is running");
})

app.get("/", (req, res) => {
  res.send("Hello world!");
})

const Discord = require("discord.js");
const client = new Discord.Client({intents: ["GUILDS", "GUILD_MESSAGES"]})

client.on("messageCreate", message => {
  if (message.content === "nf") {
    let notifications = new Discord.MessageEmbed()
    .setTitle("Notification selection")
    .setDescription(" <:Twitch:456056053386444807> <@&973533730830417920> - Receive notifications about Twitch streams \n <:YouTube:456054604564529153> <@&973534371783004211> - Receive notifications about YouTube uploads.\n <:Reddit:456064302969782291> <@&973537024927760435> - Receive notifications about Reddit posts.\n :video_game: <@&973540934098767902> - Receive notifications about free games!")
    .setColor("RED")
    .setFooter("Contact staff for a chance to add your subreddit")
    .setTimestamp()
message.channel.send({embeds:[notifications]})
  }

  if (message.content === "cp") {
    let Country_picker = new Discord.MessageEmbed()
    .setTitle("Where are you from?")
    .setDescription(":one: - Asia \n:two: - Africa \n:three: - South America \n:four: - North America \n:five: - Antartica \n:six: - Europe \n:seven: - Oceania")
    .setColor("RED")
message.channel.send({embeds:[Country_picker]})
  }
  
})

client.login(process.env.token)