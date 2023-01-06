module.exports = {
    name: 'ping',
    Description: "this is a ping command!",
    execute(message, args){
        message.channel.send('pong!');
    }
}