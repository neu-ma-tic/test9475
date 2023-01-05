const Discord = require ("discord.js");

module.exports = {
    name: 'ping',
    aliases: [],
    description: 'Returns ping Latency.',
    execute(client, message, args) {
        let newEmbed = new Discord.MessageEmbed()
        .setTitle('Calculating Ping...')
        .setDescription('This may take some time.')
        .setColor('RANDOM')
        message.channel.send(newEmbed).then((resultMessage) => {
                const ping = resultMessage.createdTimestamp - message.createdTimestamp;

                let resultEmbed = new Discord.MessageEmbed()
                .setTitle('🏓 Pong!')
                .setDescription(`Bot latency: ${ping}ms`)
                .setColor('RANDOM')

                console.log(`${ping}ms`);

                resultMessage.edit(resultEmbed)
                
            })
        }
    }
