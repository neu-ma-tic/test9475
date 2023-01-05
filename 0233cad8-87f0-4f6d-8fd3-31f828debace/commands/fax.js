module.exports = {
    name: 'fax',
    description: "Just a command to see the truth",
    execute(client, message, args){
        message.channel.send('Pineapple does not belong on pizza!');
    }
}