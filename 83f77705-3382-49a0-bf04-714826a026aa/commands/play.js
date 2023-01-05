const ytdl = require('ytdl-core');
const ytSearch = require('yt-search');

module.exports = {
  name: 'play',
  description: 'Joins and plays a vidio from youtube',
  async execute(message, args) {
    const voiceChannel = message.member.voice.channel;

    if (!voiceChannel) return message.channel.send('You nned to be in a channel to execute this command!');
    const permissions = voiceChannel.permissionsFor(message.client.user);
    if (!permissions.has('CONNECT')) return message.channel.send('you dont have the correct Permissions');
    if (!permissions.has('SPEAK')) return message.channel.send('you dont have the correct Permissions');
    if (!args.length) return message.channel.send('You need to send the second argument!');

    const  connection = await voiceChannel.join();

    const vidioFinder = async (query) => {
      const vidioResult = await ytSearch(query);
      
      return(vidioResult.videos.length > 1) ? vidioResult.videos[0] : null;
       
       } 

       const vidio = await vidioFinder(args.join(' '));

       if(video){
         const stream = ytdl(video.url, {filter: 'audioonly'});
         connection.play(stream, {seek: 0, volume: 1})
         .on('finish', () =>{ 
              voiceChannel.leave();
         });


         await message.reply(`:thumbsup: Now Playing ***${video.title}***`)
       } else {
           message.channel.send('No video results found');

      }
  }
}