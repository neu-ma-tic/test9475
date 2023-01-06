global.config = require("./config.json")
const Discord = require('discord.js'); // Import the discord.js module
// const {Collection, Discord} = require('discord.js')
const bot = new Discord.Client(); // Create an instance of a Discord bot
const chalk = require('chalk'); // print colorful text

const serverStatsCounter = require("./utils/serverstats")
// const roleclaim = require("./utils/roleclaim")
const ticketSystem = require("./utils/ticketsystem")
const welcomer = require("./utils/welcomer")
const giveawaysystem = require("./utils/giveawaysystem")

bot.on('ready', () => {
    console.log(chalk.green("[DISCORD BOT] [INFO]") + ` Logged in as ${bot.user.tag} ✅`);
    bot.user.setActivity(config.SERVER_NAME, { type: config.BOT_ACTIVITY, url: confirm.BOT_ACTIVITY_URL })
    // roleclaim(bot)
    serverStatsCounter(bot, (60000 * 15)); // 60000 milisec * 15 = 15 min refresh time
    ticketSystem(Discord, bot)
    welcomer(bot)
    giveawaysystem(Discord, bot)
});


// Log our bot in using the token from https://discord.com/developers/applications
bot.login(config.BOT_TOKEN);