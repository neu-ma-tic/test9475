const Discord = require('discord.js');

const txtgen = require('txtgen');

const { FastType } = require('weky');

module.exports = {
    name: "fstype",
    description: "fast type",

    async run(bot, message, args) {
        const sentence = txtgen.sentence();
        console.log(sentence);
        const game = new FastType({
            message: message,
            winMessage: "GG you won!", 
            sentence: sentence, 
            loseMessage: 'You Lost :(', 
            time: 50000, 
            startMessage: 'Good Luck!' 
        });
    
    game.start(); 
    }
}