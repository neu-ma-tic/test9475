const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send('Hello World!'));

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`));


const { Collection, Client, Discord, MessageEmbed } = require('discord.js');
const config = require('./config.json');

const prefix = config.prefix;
const token = config.token;

const fs = require('fs');
const bot = new Client();

bot.commands = new Collection();
bot.aliases = new Collection();
bot.categories = fs.readdirSync("./commands/");

["command"].forEach(handler => {

    require(`./handlers/${handler}`)(bot);

});

bot.on('ready', () => {

    console.log(`Bot ready !`);
    bot.user.setActivity(`Surveille modcraftmc`);

});


bot.on('message', async message => {

    if (message.author.bot) return;

    if (config.mentiondisabled.includes(message.content)) {
        message.reply("Cette personne n'accepte pas les mentions.").then(msg => msg.delete({ timeout: config.timeout }));
        bot.channels.fetch(`714556428278431844`).then(channel => {
            const userMentionned = message.mentions.users.first().id;

            bot.users.fetch(userMentionned).then(user => { channel.send(`Nouvelle mention de ${message.author.username} dans <#${message.channel.id}> envers ${user.username}`) })
        })
        message.delete();
    }


    //DELETE MESSAGE IF NOT ALLOWED
    if (message.channel.id === config.propositionChannelID) if (!message.content.startsWith("&proposition")) message.delete();

    if (!message.content.startsWith(prefix)) return;
    if (!message.guild) return;
    if (!message.member) member.member = await message.guild.fetchMember(message);
    const args = message.content.slice(prefix.length).trim().split(/ +/g);
    const cmd = args.shift().toLowerCase();

    if (cmd.length == 0) return;
    let command = bot.commands.get(cmd);
    if (!command) command = bot.commands.get(bot.aliases.get(cmd));

    console.log(`${new Date()} : new command from ${message.author.username} -> ${command.name} with args -> ${args}`)

    if (command) command.run(bot, message, args, config);

});

bot.on('guildMemberAdd', async member => {

    bot.channels.fetch(`660166493681745980`).then(channel => {


        const embed = new MessageEmbed()
        .setTitle(`Bienvenue !`)
        .setDescription(`Bienvenue <@${member.id}> sur ModcraftMC !`)
        .setColor(`FFA500`);

        channel.send(embed).then(message => {

            message.react("👋");

        });
        

    });

});

bot.login(token);


