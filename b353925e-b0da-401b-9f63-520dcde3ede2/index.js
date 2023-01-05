require("dotenv").config();
const fs = require("fs")
const { Client, Collection, Intents } = require("discord.js");

const client = new Client({intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MEMBERS, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.GUILD_MESSAGE_REACTIONS, Intents.FLAGS.GUILD_MESSAGE_TYPING]});




client.once("ready", () => {
    console.log(`Ready! Logged in as ${client.user.tag}! I'm on ${client.guilds.cache.size} guild(s)!`);
    client.user.setActivity({name: "Glauben sie, dass ich verrückt bin?", type: "PLAYING"});
})






// Register an event to handle incoming messages
client.on('messageCreate', async msg => {
// This block will prevent the bot from responding to itself and other bots
        if(msg.author.bot) {
          return
        }
      
 // Check if the message starts with '!hello' and respond with 'world!' if it does.
        if(msg.content.startsWith("!hello")) {
          msg.reply("world!")
        }

// Info for Karuta Bot
if(msg.content.startsWith("kinfo")) {
    msg.reply("...")
  }


if(msg.content.includes("elonmusk")) {
    msg.reply("Glauben sie, dass ich verrückt bin? Diese Frage stellte mir Elon Musk gegen Ende eines langen Abendessens in einem edlen Fischrestaurant im Silicon Valley. Ich war zuerst dort und hatte es mir mit einem Gin Tonic gemütlich gemacht, weil ich wusste, dass Musk, wie üblich, zu spät kommen würde.")
  }

  if(msg.content.startsWith("digga")) {
    msg.reply("Digga wallah Film heute. Saß mit Kartell am Tisch. Hast du schon mal gesehen das 20 Leute mit gezogener Waffe auf Gesicht stehen und dann bricht Schlägerei aus. Wallah ich dachte alles vorbei jetzt Ich habe alle beruhigt auf Englisch Sonst wäre Massengrab gewesen bro.")
  }

  
  if(msg.content.startsWith("💀")) {
    msg.reply("💀💀💀")

    
  }
  
      
        if(msg.content.startsWith("!dm")) {
          var messageContent = msg.content.replace("!dm", "Bei Seite mit dir du fette Wanze digga")
          msg.member.send(messageContent)
        }
      



        if(msg.content.startsWith("!collector")){
          var filter = (msg) => !msg.author.bot
          var options = {
            max: 2,
            time: 15000
          }

          var collector = msg.channel.createMessageCollector(filter, options)

          collector.on('collect', (msg) => {
            console.log(`Collected ${msg.content}`)
          })

          collector.on('end', (colected) => {
            console.log(`Collected ${collected.size} items`)
          })

          msg.reply('What is your favourite color?')  
        }

        


      })  // ENDING




client.on("interactionCreate", async (interaction) => {
    if(!interaction.isCommand()) return

    const command = client.commands.get(interaction.commandName)


    if(command) {
        
        try {
            await command.execute(interaction)
        } catch(error) {
            console.error(error)

            if(interaction.deferred  || interaction.replied){
                interaction.editReply("There was an error while loading this command!")
            }else {
                interaction.    Reply("There was an error while loading this command!")
            }
        }
    }
})




client.login(process.env['DISCORD_BOT_TOKEN']);