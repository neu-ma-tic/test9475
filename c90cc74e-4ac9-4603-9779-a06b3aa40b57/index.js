const Discord = require("discord.js");
const Client = new Discord.Client();

client.once('ready', () => {
  console.log('Ready!');
});

client.on('message', message => {
  if (message.content === '!ping') {
    message.channel.send('Pong.');
}
});

client.logig("ODc0MjU5MjEwMjA3MTI1NTE0.YREXVg.EZ45QnoxiPisv-v6L6axmeVkY3E");