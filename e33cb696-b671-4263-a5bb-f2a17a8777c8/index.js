const Discord = require('discord.js');
const bot = new Discord.Client();


const token = "ve9RFqnIlVBEpJlQyZwXbOq4cr_FKakg"

bot.on('ready', () => {
  console.log("BOT IS ONLINEEEE!!!");
})
bot.login(token);