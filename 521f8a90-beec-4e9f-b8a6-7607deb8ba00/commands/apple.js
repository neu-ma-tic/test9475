module.exports = {
    name: 'apple',
    description: 'This is an apple command!',
    execute(client, message, args){

        if(message.member.roles.cache.has('842326667216158741')){
            message.channel.send('banana!')
        } else {
            message.channel.send('You do not have the correct permissions to use that command');
        }
    }
}