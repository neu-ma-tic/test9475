const { Client, Collection, Intents } = require('discord.js');
const fs = require("fs");
const { connect, connection: db } = require('mongoose');
const chalk = require("chalk");
const keepAlive = require('../utils/Server');

module.exports = class BotClient extends Client { 
    constructor() {
        super({
            intents: [
                Intents.FLAGS.GUILDS,
                Intents.FLAGS.GUILD_MESSAGES,
                Intents.FLAGS.GUILD_INVITES,
                Intents.FLAGS.GUILD_MEMBERS,
                Intents.FLAGS.GUILD_PRESENCES,
                Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
                Intents.FLAGS.GUILD_VOICE_STATES,
            ],
            partials: ["USER", "MESSAGE", "REACTION"],
            allowedMentions: {
                parse: ['roles', 'users'],
                repliedUser: false,
            },
        });
        this.slashCommands = new Collection();
        this.cooldowns = new Collection();

        this.logger = require('../utils/Logger');
        this.colors = require('../assets/colors.json');

        this.database = require('../database/mongoose');

        keepAlive(this);


        db.on('connected', async () => this.logger.log(`Successfully connected to the database! (Latency: ${Math.round(await this.databasePing())}ms)`));
        db.on('disconnected', () => this.logger.error('Disconnected from the database!'));
        db.on('error', (error) => this.logger.error(`Unable to connect to the database!\nError: ${error}`));
        db.on('reconnected', async () => this.logger.log(`Reconnected to the database! (Latency: ${Math.round(await this.databasePing())}ms)`));
    }
    /*
    * Load all commands for the bot.
    */
    async loadCommands() {
        const commandFolders = fs.readdirSync('./src/commands');
        for (const folder of commandFolders) {
            const commandFiles = fs.readdirSync(`./src/commands/${folder}`).filter(file => file.endsWith('.js'));
            for (const file of commandFiles) {
                let pull = require(`../commands/${folder}/${file}`);
                const command = new pull(this);
                if(command.name){ 
                    this.slashCommands.set(command.name, command);
                }
            }
        }
        this.logger.log(`Succesfully loaded ${chalk.redBright(this.slashCommands.size)} commands`)
    }
    /*
    * Load all events for the bot.
    */
    async loadEvents() {
        const eventFolders = fs.readdirSync('./src/events');
        for (const folder of eventFolders) {
            const eventFiles = fs.readdirSync(`./src/events/${folder}`).filter(file => file.endsWith('.js'));
            for (const file of eventFiles) {
                let eventFunc = require(`../events/${folder}/${file}`);
                let eventName = file.split(".")[0];
                this.on(eventName, (...args) => eventFunc.run(this, ...args));
            }
        }   
        this.logger.log(`Loaded all the events!`)
    }
    /*
    * Load database.
    */
    async loadDatabase() {
        if(!process.env['mongoURL']) this.logger.error('No mongoURL found!')
        connect(, {
            keepAlive: true,
            useNewUrlParser: true,
            useUnifiedTopology: true,
        });

        
    }
    /* 
    * Get database ping 
    */
    async databasePing() {
        const cNano = process.hrtime();
        await db.db.command({ ping: 1 });
        const time = process.hrtime(cNano);
        return (time[0] * 1e9 + time[1]) * 1e-6;
    }

    /*
    * Load the slash commands!
    */
    async initializeSlash(guildID){
        const slashCommandsArray = [];
        this.slashCommands.forEach(command => {
            const cmd = {
                name: command.name,
                description: command.description || "No description provided",
                options: command.options || [],
            };
            slashCommandsArray.push(cmd);
        });
        const guild = this.guilds.cache.get(guildID);
        if(!guild) return;
        await guild.commands.set(slashCommandsArray);
    }

    /* 
    * Start the bot 
    */
    async start(token) {
        this.logger.log('Starting the discord bot..')
        await this.loadEvents();
        await this.loadCommands();
        await this.loadDatabase();
        return super.login(token);
    }
}