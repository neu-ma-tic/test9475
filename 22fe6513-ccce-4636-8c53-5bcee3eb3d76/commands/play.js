const ytdl = require('ytdl-core-discord');
const ytSearch = require('yt-search');
const ytpl = require('ytpl');
const queue = new Map();

module.exports = {
    name: 'play',
    aliases: ['skip', 'stop', 'loop', 'insert'],
    cooldown: 0,
    description: 'Advanced music bot',
    async execute(client, message, args, command) {
        try {
            if (!command) return;
            const voice_channel = message.member.voice.channel;

            //This is our server queue. We are getting this server queue from the global queue.
            const server_queue = queue.get(message.guild.id);

            //If the user has used the play command
            if (command === 'skip') await skip_song(message, server_queue);
            else if (command === 'stop') await stop_song(message, server_queue, queue);
            else if (command === 'shuffle') await shuffle_song(message, server_queue);
            else if (command === 'q' || command === 'queue') await show_songs(message, server_queue);
            else if (command === 'loop' || command === 'l') await loop_song(message, server_queue);
            else if (command === 'insert' || command === 'i') await insertSong(message, args[0], args[1]);
            else if (command === 'play' || command === 'p') {
                if (!voice_channel) return message.channel.send('你要加入左語音頻道先得㗎');
                const permissions = voice_channel.permissionsFor(message.client.user);
                if (!permissions.has('CONNECT')) return message.channel.send('You dont have the correct permissins');
                if (!permissions.has('SPEAK')) return message.channel.send('You dont have the correct permissins');

                if (!args.length) return message.channel.send('You need to send the second argument!');
                let song = {};
                //If the first argument is a link. Set the song object to have two keys. Title and URl.
                isPlaylist = false;
                if (ytdl.validateURL(args[0])) {
                    const song_info = await ytdl.getInfo(args[0]);
                    song = { title: song_info.videoDetails.title, url: song_info.videoDetails.video_url }
                } else if (ytpl.validateID(args[0])) {
                    isPlaylist = true;
                    playlistID = await ytpl.getPlaylistID(args[0]);
                }
                else {
                    //If there was no link, we use keywords to search for a video. Set the song object to have two keys. Title and URl.
                    const video_finder = async (query) => {
                        const video_result = await ytSearch(query);
                        return (video_result.videos.length > 1) ? video_result.videos[0] : null;
                    }
                    const video = await video_finder(args.join(' '));
                    if (video) {
                        song = { title: video.title, url: video.url }
                    } else {
                        message.channel.send('Sorry, 穩唔到條片.');
                        return;
                    }
                }

                //If the server queue does not exist (which doesn't for the first video queued) then create a constructor to be added to our global queue.
                if (!server_queue) {
                    const queue_constructor = {
                        voice_channel: voice_channel,
                        text_channel: message.channel,
                        message: null,
                        connection: null,
                        songs: [],
                        looping: false
                    }
                    queue.set(message.guild.id, queue_constructor);
                    if (isPlaylist) {
                        await addListSongsToQueue(message, playlistID, queue_constructor);
                    }
                    else {
                        //Add our key and value pair into the global queue. We then use this to get our server queue.
                        queue_constructor.songs.push(song);
                    }
                    //Establish a connection and play the song with the vide_player function.
                    try {
                        const connection = await voice_channel.join();
                        queue_constructor.connection = connection;
                        video_player(message.guild, queue_constructor.songs[0]);
                    } catch (err) {
                        queue.delete(message.guild.id);
                        message.channel.send('有内鬼，終止運作!');
                        throw err;
                    }
                } else {
                    if (isPlaylist) {
                        return await addListSongsToQueue(message, playlistID, server_queue);
                    } else {
                        server_queue.songs.push(song);
                        return message.channel.send(`👍幫你加左 **${song.title}** 入條list啦!`);
                    }
                }
            }
            // client.on('voiceStateUpdate',async (oldState, newState) => {
            //     if(oldState.id != '795973178987511838') {
            //         var q = queue.get(oldState.guild.id);
            //         if(q && q.voice_channel.members.size <= 1){
            //             await q.connection.dispatcher.end();
            //             await q.voice_channel.leave();
            //             queue.delete(oldState.guild.id);
            //         }
            //     }
            // });
        } catch (e) {
            console.log("97", e);
            return;
        }
    }

}
const insertSong = async (message, song, position)=> {
    try{
        const server_queue = queue.get(message.guild.id);
        if (!message.member.voice.channel) return message.channel.send('你要加入左語音頻道先得㗎');
        if (!server_queue) {
            return await message.channel.send(`你可以用格式\n'.play 歌曲名稱'\n去播歌`);
        }
        if (ytdl.validateURL(song)) {
            const song_info = await ytdl.getInfo(song);
            song = { title: song_info.videoDetails.title, url: song_info.videoDetails.video_url }
            if(song){
                if(position < 1){
                    position = 1;
                }
                else if(position > server_queue.songs.length){
                    return server_queue.songs.push(song);
                }
                server_queue.songs.splice(position, 0, song);
                return await message.channel.send(`👍幫你放左**${song.title}**去第${position}首啦`);
            }else{
                return await message.channel.send('Sorry, 穩唔到條片.');
            }
        }else {
           return await message.channel.send('Sorry, 目前插歌只支援youtube link');
        }
    }catch{
        console.log("114", e);
        return await message.channel.send('Sorry, 有error');
    }        
}

const addListSongsToQueue = async (message, playlistID, server_queue) => {
    try {
        const playlist = await ytpl(playlistID, { limit: Infinity });
        songs = playlist.items;
        for (var i = 0; i < songs.length; i++) {
            server_queue.songs.push({ title: songs[i].title, url: songs[i].shortUrl });
        }
        return await message.channel.send(`👍歌單 **${playlist.title}** 入面成 **${songs.length}** 首歌都同你加左入條list啦!`);
    }
    catch (e) {
        console.log("114", e);
        return;
    }
}

const skip_song = async (message, server_queue) => {
    try {
        if (!message.member.voice.channel) return message.channel.send('你要加入左語音頻道先得㗎');
        if (!server_queue) {
            return await message.channel.send(`你都無播緊歌=.=`);
        }
        server_queue.looping = false;
        server_queue.songs.shift();
        video_player(message.guild, server_queue.songs[0]);
    } catch (e) {
        console.log("130", e);
        return;
    }
}

const loop_song = async (message, server_queue) => {
    try {
        if (!message.member.voice.channel) return message.channel.send('你要加入左語音頻道先得㗎');
        if (!server_queue) {
            return await message.channel.send(`你都無播緊歌=.=`);
        }
        server_queue.looping = !server_queue.looping;
        if (server_queue.looping) {
            return await message.channel.send(`單曲循環開左。:ok_hand: `);
        } else {
            return await message.channel.send(`單曲循環熄左。:ok_hand: `);
        }
    }
    catch (e) {
        console.log("149", e);
        return;
    }
}

const stop_song = async (message, server_queue, queue) => {
    try {
        if (!message.member.voice.channel) return message.channel.send('你要加入左語音頻道先得㗎');
        if (server_queue) {
            if (server_queue.connection.dispatcher) {
                await server_queue.connection.dispatcher.end();
                message.channel.send(`走先啦，係咁先啦`);
            }
            queue.delete(message.guild.id);
            return await server_queue.voice_channel.leave();
        } else {
            queue.delete(message.guild.id);
            return await server_queue.voice_channel.leave();
        }
    }
    catch (e) {
        console.log("170", e);
        return;
    }

}

const show_songs = async (message, server_queue) => {
    try {
        if (!server_queue) {
            return message.channel.send(`你都無播緊歌=.=`);
        } else {
            song = ""
            songs = server_queue.songs;
            if (songs.length > 8) {
                for (var i = 0; i < 8; i++) {
                    if(i==0){
                        song += `${i + 1}. (現正播放)🎶 **${songs[i].title}**\n`;
                    }else{
                        song += `${i + 1}. 🎶 **${songs[i].title}**\n`;
                    }
                }
            } else {
                for (var i = 0; i < songs.length; i++) {
                    if(i==0){
                        song += `${i + 1}. (現正播放)🎶 **${songs[i].title}**\n`;
                    }else{
                        song += `${i + 1}. 🎶 **${songs[i].title}**\n`;
                    }
                }
            }
            if(song != ""){
                return await message.channel.send(song);
            }
        }
    }
    catch (e) {
        console.log("196", e);
        return;
    }
}

const shuffle_song = async (message, server_queue) => {
    try {
        if (!message.member.voice.channel) return message.channel.send('你要加入左語音頻道先得㗎');
        if (!server_queue) return message.channel.send('你都無播緊歌=.=');
        songs = server_queue.songs;
        let currentIndex = songs.length, randomIndex;
        while (currentIndex != 0) {
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex--;
            [songs[currentIndex], songs[randomIndex]] = [
                songs[randomIndex], songs[currentIndex]];
        }
        await message.channel.send(`Shuffle左`);
        return songs;
    }
    catch (e) {
        console.log("217", e);
        return;
    }

}

const video_player = async (guild, song) => {
    try {
        const song_queue = queue.get(guild.id);
        if (!song) {
            await song_queue.voice_channel.leave();
            queue.delete(guild.id);
            return;
        }
        if(song_queue){
            await song_queue.voice_channel.join();
            const stream = await ytdl(song.url);
            song_queue.connection.play(stream, { type: 'opus' })
                .on('finish', async () => {
                    if (!song_queue.looping) {
                        song_queue.songs.shift();
                    }
                    await video_player(guild, song_queue.songs[0]);
                });
            if (song_queue.message) {
                await song_queue.message.delete();
            }
            song_queue.message = await song_queue.text_channel.send(`🎶 宜家播緊嘅係 **${song.title}**`);
        }
    }
    catch (e) {
        console.log("246", e);
        return;
    }
    //If no song is left in the server queue. Leave the voice channel and delete the key and value pair from the global queue.
}

