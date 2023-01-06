module.exports = {
    name: 'lame',
    Description: "this is a lame command!",
    execute(message, args){
        message.channel.send(':mirror:');
    }
}