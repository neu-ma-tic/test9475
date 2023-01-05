module.exports = {
    name: 'youtube',
    description: "sends the youtube link",
    execute(message, args, Discord){
        const newEmbed = new Discord.MessageEmbed()
        .setColor('#304281')
        .setAuthor('YouTube', 'https://logos-world.net/wp-content/uploads/2020/04/YouTube-Emblem.png')
        .setTitle('Retro Guy')
        .setURL('https://www.youtube.com/retroguy')
        .setDescription('Watch a Taking Apart, Fixing, Modern Gaming, Retro Gaming, and Streams With Retro Guy!')
        .setImage('https://i.imgur.com/4M1lSdA.jpg')

        message.channel.send(newEmbed);
    }
}