const Discord = require('discord.js');

const { RPS } = require('weky');

module.exports = {
    name: "rps",
    description: "to play rps",

    async run(bot, message, args) {
        const opponent = message.mentions.users.first();
        let user = message.author;
        if(!opponent){ message.react('😤'); return message.channel.send(`Please mention who you want to fight against`); }

        const game = new RPS({
        message: message,  
        opponent: opponent, 
        challenger: user, 
        acceptMessage: "Do you want to play Rock-Paper-Scissors with <@" + user + '>', // message sent to see if opponent accepts
        })

    game.start() 

    }
}