const Discord = require('discord.js');

const bot = new Discord.Client();

const prefix = '+';

const fetch = require('node-fetch');

const disbut = require('discord-buttons');

const { readdirSync, read } = require('fs');

const { join } = require('path');

disbut(bot);


const mongoose = require('mongoose');
mongoose.connect('mongodb+srv://<username>:<password>@cluster0.gvn2n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', {
    useUnifiedTopology: true,
    useNewUrlParser: true,
    useFindAndModify: false
}).then(console.log('bot has connected to mongo!'));

const Levels = require('discord-xp');
Levels.setURL('mongodb+srv://<username>:<password>@cluster0.gvn2n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority');


bot.commands = new Discord.Collection();

const commandFiles = readdirSync(join(__dirname, "commands")).filter(file => file.endsWith(".js"));

for (const file of commandFiles) {
    const  command = require(join(__dirname, "commands", `${file}`));
    bot.commands.set(command.name, command);
}

bot.on("error", console.error);

bot.on('ready', () => {
    console.log('Logged in as ' + bot.user.tag);
    bot.user.setActivity('dumb people', { type: "WATCHING" }).catch(console.error)
})

bot.on("message", async message => {

    if(message.author.bot) return;
    if(message.channel.type === 'dm') return;

    if(message.content.startsWith(prefix)) {

        //Levels 

        if(!message.author.bot){
            const randomAmountOfXp = Math.floor(Math.random() * 29) + 1; 
            const hasLeveledUp = await Levels.appendXp(message.author.id, message.guild.id, randomAmountOfXp);
            if (hasLeveledUp) {
                const user = await Levels.fetch(message.author.id, message.guild.id);
                message.channel.send(`${message.author}, congratulations! You have reached Level **${user.level}**!`);
            }
        }

        //End of Levels 
      
        const args = message.content.slice(prefix.length).trim().split(/ +/);

        const command = args.shift().toLowerCase();

        if(!bot.commands.has(command)){ message.react('❌'); message.reply('Invalid command fam'); }


        try {
            bot.commands.get(command).run(bot, message, args);
        } catch (error){
            console.error(error);
        }
    } 
})
bot.login('BOT TOKEN');
