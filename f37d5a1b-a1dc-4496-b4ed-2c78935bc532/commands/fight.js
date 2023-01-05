const Discord = require('discord.js');

const { fight } = require('weky');

module.exports = {
    name: "fight",
    description: "lets users fight",

    async run(bot, message, args) {
        const opponent = message.mentions.users.first();
        if (!opponent) return message.channel.send(`Please mention who you want to fight!`);

        const battle = new fight({
        client: bot,
        message: message,
        acceptMessage: 'Click to fight with <@' + message.author + '>', //message sent to see if opponent accepts
        challenger: message.author, 
        opponent: opponent,  
        hitButtonText: 'HIT', 
        hitButtonColor: 'red', 
        healButtonText: 'HEAL', 
        healButtonColor:  'green', 
        cancelButtonText: 'CANCEL', 
        cancelButtonColor: 'blurple', 
    });
    battle.start(); 
    }
}