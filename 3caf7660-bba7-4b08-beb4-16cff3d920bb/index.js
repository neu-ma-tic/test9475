const Discord = require('discord.js');
const client = new Discord.Client();
const ytdl = require('ytdl-core');
 
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
 
client.on('message', async message => {
  // Voice only works in guilds, if the message does not come from a guild,
  // we ignore it
  if (!message.guild) return;

  if (message.content === '/join') {
    // Only try to join the sender's voice channel if they are in one themselves
    if (message.member.voice.channel) {
      const connection = await message.member.voice.channel.join();
      connection.play(ytdl('https://www.youtube.com/watch?v=ZlAU_w7-Xp8', { filter: 'audioonly' }));
      console.log("Starting")
    } else {
      message.reply('You need to join a voice channel first!');
    }
  }
});
 
client.login(process.env.TOKEN);