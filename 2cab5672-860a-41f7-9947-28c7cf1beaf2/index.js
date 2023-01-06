const Discord = require("discord.js");
const config = require("./config.json");

const client = new Discord.Client();
const prefix = "!";

// client.on("message", function(message) {
//   console.log("demdoemdoe", message)
//   if (message.author.bot) return;
//   if (!message.content.startsWith(prefix)) return;

//   const commandBody = message.content.slice(prefix.length);
//   const args = commandBody.split(' ');
//   const command = args.shift().toLowerCase();

//   if (command === "ping") {
//     const timeTaken = Date.now() - message.createdTimestamp;
//     message.reply(`Pong! This message had a latency of ${timeTaken}ms.`);
//   }

//   else if (command === "sum") {
//     const numArgs = args.map(x => parseFloat(x));
//     const sum = numArgs.reduce((counter, x) => counter += x);
//     message.reply(`The sum of all the arguments you provided is ${sum}!`);
//   }
// });

// client.login(config.BOT_TOKEN);
// console.log(client.channels.cache.toJSON())
const list = client.guilds.cache.get("968399882392072202"); 

console.log(list)
// client.on('ready', () => {
//   console.log("demdoemdoemd")
//   console.log(client.channels.cache.toJSON())
// });
