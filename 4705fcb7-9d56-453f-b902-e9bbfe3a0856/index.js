const keepAlive = require("./server")
const Discord = require("discord.js");
const fetch = require("node-fetch");
const client = new Discord.Client();
const Database = require("@replit/database")
const db = new Database()
sadWords = ["sad", "depressed", "unhappy", "angry", "miserable"]
starterEncouragements = ["Cheer up!", "Hang in there", "You are a great person/bot!"]
words = ["wassup", "Wassup", "Whats up", "whats up"]
helpWords = ["queries", "problem", "complaint"]


db.get("encouragements").then(encouragements => {
  if(!encouragements || encouragements < 1){
    db.set("encouragements", starterEncouragements)
  }
})

db.get("responding").then(value=>{
  if(value == null){
    db.set("responding", true)
  }
})

function getQuote(){
  return fetch("https://zenquotes.io/api/random")
    .then(res => {
      return res.json()
    })
    .then(data => {
      return data[0]["q"] + " -" + data[0]["a"]
    })
}

function updateEncouragements(encouragingMessage) {
  db.get("encouragements").then(encouragements => {
    encouragements.push([encouragingMessage])
    db.set("encouragements", encouragements)
  })
}

function deleteEncouragment(index) {
  db.get("encouragements").then(encouragements => {
    if (encouragements.length > index) {
      encouragements.splice(index, 1)
      db.set("encouragements", encouragements)
    }
  })
}

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on("message", msg => {
  if(msg.content === "$inspire"){
    getQuote().then(quote => msg.channel.send(quote))
  }

  db.get("responding").then(responding => {
    if (responding && sadWords.some(word => msg.content.includes(word))) {
      db.get("encouragements").then(encouragements => {
        const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
        msg.reply(encouragement)
      })
    }
  })

  if (msg.content.startsWith("$new")) {
    encouragingMessage = msg.content.split("$new ")[1]
    updateEncouragements(encouragingMessage)
    msg.channel.send("New encouraging message added.")
  }

  if (msg.content.startsWith("$del")) {
    index = parseInt(msg.content.split("$del ")[1])
    deleteEncouragment(index)
    msg.channel.send("Encouraging message deleted.")
  }

  if (msg.content.startsWith("$list")) {
    db.get("encouragements").then(encouragements => {
      msg.channel.send(encouragements)
    })
  }
    
  if (msg.content.startsWith("$responding")) {
    value = msg.content.split("$responding ")[1]

    if (value.toLowerCase() == "true") {
      db.set("responding", true)
      msg.channel.send("Responding is on.")
    } else {
      db.set("responding", false)
      msg.channel.send("Responding is off.")
    }
  }

  if (msg.content.includes("shit")){
    msg.reply("No foul language!")
  }

  if(msg.content.includes("help")){
    msg.reply("Is there anything I can aide you with?")
  }

   if(msg.content.includes("yes")){
      msg.channel.send("What is it that I can do?")
    }else if(msg.content.includes("no")){
      msg.channel.send("Okay")
    }

  for(var i = 0; i < helpWords.length; i++){
    if(msg.content.includes(helpWords[i])){
      msg.channel.send("Visit discord's customer service website: https://support.discord.com/hc/en-us")
    }
  }
    
  if((msg.content.includes("bot") || msg.content.includes("Bot")) && !((msg.content.includes("Hi")) || (msg.content.includes("hi")))){
    msg.channel.send(`Yes ${msg.author.username}?`)
  }

  if(msg.content.includes("Hi bot") || msg.content.includes("hi bot")){
    msg.channel.send(`Hello ${msg.author.username}`)
  }

  for(var i = 0; i < words.length; i++){
    if(msg.content.includes(words[i])){
      msg.reply("Nothing much, boss")
    }
  }
})

client.on('guildMemberAdd', member => {
  const channel = member.guild.channels.cache.find(ch => ch.name === 'member-log');

  if(!channel) return;

  channel.send(`Welcome to the server, ${member}`);
})

keepAlive()
client.login("ODY4ODM2Mjk3NTYzODQ0NjA4.YP1c2w.P4er0zWq2n0M1Q-HbvwuNStHxUo")