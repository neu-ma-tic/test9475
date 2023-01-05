module.exports = {
    name: 'command',
    description: "Embeds!",
    execute(message, args, Discord){
        const newEmbed = new Discord.MessageEmbed()
        .setColor('#304281')
        .setTitle('Rules')
        .setURL('https://www.youtube.com/retroguy')
        .setDescription('This is a embed for the server rules')
        .addFields(
            {name: 'Rule 1', value: 'Be nice'},
            {name: 'Rule 2', value: 'Subscribe on YouTube and follow on Twitch'},
            {name: 'Rule 3', value: 'no memes'}
        )
        .setImage('https://static.toiimg.com/thumb/msid-67586673,width-800,height-600,resizemode-75,imgsize-3918697,pt-32,y_pad-40/67586673.jpg')
        .setFooter('Make sure to check out the rules channel');

        message.channel.send(newEmbed);
    }
}