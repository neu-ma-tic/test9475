

let config = {
      "id": "368834969356861450", //DevBot's ID
       "DaveID": "218550507659067392",
       "Channels": {
         "BotWorld": {
           "general": "332028861149609985"
         }
       }
}

const emojis = ["❌"
,"1⃣"
,"2⃣"
,"3⃣"
,"4⃣"
,"5⃣"
]


// Set up discord.js client
let ME;
const Discord = require('discord.js');
const client = new Discord.Client({
    autoReconnect: true
});


/**
 * Setup Function section
 */

const clean = text => {
  if (typeof(text) === "string")
    return text.replace(/`/g, "`" + String.fromCharCode(8203)).replace(/@/g, "@" + String.fromCharCode(8203));
  else
      return text;
}


/**
 * @function replyPing
 * @argument message "the message being replied to"
 */
function replyPing(message){
  message.channel.send("pong").then((message) =>{
    message.reply()
    addCountReact(message)
     console.log(message)}).catch((err) => console.error(err))
  
}

async function addCountReact(message){
  for (emoji in emojis) {
    try {
      await message.react(emojis[emoji])
      } 
    catch (err)
    {
      console.error(err);
    }
  }
}

//Message Recieved
client.on('message', message => {
    // bot shouldn't check it's own stuff)
    if (message.author.id != client.user.id) {
      if (message.content == "ping"){
        replyPing(message)
      }
      else if (message.content.startsWith("!eval")) {
    if(message.author.id !== config.DaveID) return;
    try {
      const args = message.content.split(" ").slice(1);
      const code = args.join(" ");
      let evaled = eval(code);
 
      if (typeof evaled !== "string")
        evaled = require("util").inspect(evaled);
 
      message.channel.send(clean(evaled), {code:"xl"});
    } catch (err) {
      message.channel.send(`\`ERROR\` \`\`\`xl\n${clean(err)}\n\`\`\``); 
      }
    }
  }
})

 client.on("error", (e) => console.error(e));
  client.on("warn", (e) => console.warn(e));
  client.on("debug", (e) => console.info(e));

client.on('messageReactionAdd', (messageReaction, user) => {
  if (user != ME){
    console.log(`${user.username} added a reaction of ${messageReaction.emoji.name} to ${messageReaction.message.content}`)
    messageReaction.remove(user).then( (messageReaction) => {
      messageReaction.message.edit(messageReaction.message.content + "\n\t" + user.username + ": " + messageReaction.emoji.name)
      console.log(`removed ${user.username}`)
    }
      )}

  
})

// Connected!
client.on('ready', () => {
    console.log('DevBot is ready!');
    ME = client.user
    ME.setActivity("Beep Beep Beep")
});



// connect
console.log("Logging in!")
client.login(process.env.TOKEN)