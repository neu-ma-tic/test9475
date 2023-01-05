const Discord = require('discord.js');

const { Snake } = require('weky')

module.exports = {
    name: "snake",
    description: "the snake game",

     async run(bot, message, args) {
        new Snake({
            message: message,
            embed: {
            title: 'Snake', 
            color: "#ff4267", 
            gameOverTitle: "Game Over", 
            },
            emojis: {
              empty: '⬛', 
              snakeBody: '🟢', 
              food: '🍎', 
              up: '🔼', 
              right: '◀️',
              down: '🔽',
              left: '▶️',
              },
            }).start()
        }
    }