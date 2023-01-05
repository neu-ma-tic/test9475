module.exports = {
    name: 'rep',
    description: "Just a command to give players a reputation.",
    execute(client, message, args, Discord){
        const comingsoon = new Discord.MessageEmbed()
        .setColor('#8210B6')
        .setTitle('Coming Soon!')

        message.channel.send(comingsoon);
    }
}