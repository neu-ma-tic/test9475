const Discord = require('discord.js');

const { TicTacToe } = require('weky');

module.exports = {
    name: "ttt",
    description: "ttt command",

    async run (bot, message, args) {
        const opponent = message.mentions.users.first();
        if (!opponent) return message.reply(`Please mention a user who you would like to play with!`);
        const game = new TicTacToe({
            message: message,
            opponent: opponent,
            xColor: 'gray', 
            oColor: 'gray',
            xEmoji: '🟢',  
            oEmoji: '❌' 
        })
        game.start()
    }
}