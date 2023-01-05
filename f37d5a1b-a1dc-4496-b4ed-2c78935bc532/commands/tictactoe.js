const { tictactoe } = require('reconlx')

module.exports = {
    name: "tictactoe",
    description: "tic tac toe command",

    async run (bot, message, args) {
        const member = message.mentions.members.first()
        if(!member) return message.channel.send('Please specify a user to play against!');

        new tictactoe({
            player_two: member,
            message: message
        })
    }
}