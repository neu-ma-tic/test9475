module.exports = {
    name: 'ping',
    description: "Just a test command to see if the bot is online.",
    execute(client, message, args){
        message.channel.send('pong!');
    }
}